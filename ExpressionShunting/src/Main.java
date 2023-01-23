/**
 * Jack Greff
 * 3/24/22
 * Lab 3
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        LinkedQueue<String> exp = shuntingYard(args);//takes arguments and puts them in post fix
        //print args
        String printInput = "";
        for(String arg: args){printInput = printInput+arg+" ";}
        System.out.println("Input Equation: "+printInput);

        System.out.println("Result: "+ (double) postfix(exp));//takes postfix, computes value, and prints it
    }

    /**
     * Checks if it can convert to double
     * @param checkString: String checked
     * @return true or false if a number
     */
    public static boolean isNumeric(String checkString) {
        if (checkString == null) {return false;}//if nothing in string return false
        try {double d = Double.parseDouble(checkString);}
        catch (NumberFormatException E) {return false;}
        return true;
    }

    static List<String> operator = Arrays.asList("^","*","/","+","-");//important to use .contains method below
    /**
     * Checks if it can convert to operator
     * @param checkString: String checked
     * @return true or false if an operator
     */
    public static boolean isOperator(String checkString) {return operator.contains(checkString);}

    /**
     * Checks if it can convert to parentheses
     * @param checkString: String checked
     * @return true or false if parentheses
     */
    public static boolean isParentheses(String checkString) {return checkString.equals("(") ||checkString.equals(")");}

    /**
     * Says precedence of an operator (or if an operator is not entered will return 0)
     * @param checkString: String checked for priority
     * @return: an integer used as a reference for priority
     */
    public static int precedence(String checkString) {
        if (checkString.equals("^")) {return 10;}//
        else if (checkString.equals("*") || checkString.equals("/")) {return 5;}
        else{return 0;}//not in list
    }

    /**
     * Given an infix expression, returns a postfix expression
     * @param stringArray: infix expression
     * @return: postfix expression
     */
    public static LinkedQueue<String> shuntingYard(String[] stringArray){
        LinkedQueue queue = new LinkedQueue();
        LinkedStack stack = new LinkedStack();

        for(String item: stringArray){//go through each term in array
            if(!isNumeric(item) && !isOperator(item) && !isParentheses(item)) {//checks if an illegal argument was entered
                throw new IllegalArgumentException("You entered something that wasn't a number, operation, or parentheses");
            }
                if (isNumeric(item)) {//if a number add to queue
                    queue.enqueue(item);
                } else if (isOperator(item)) {
                    if (stack.isEmpty() || stack.peek().equals("(") || precedence(item) >= precedence(stack.peek().toString())) {//if empty, first term in stack is parentheses, or the operator takes precedence over first term in stack
                        stack.push(item);
                    } else {
                        queue.enqueue(stack.pop());//queue previous term
                        stack.push(item);//enter operator in stack
                    }
                } else if (isParentheses(item)) {
                    if (item.equals("(")) {//if open parentheses, add to stack
                        stack.push(item);
                    } else {
                        while (!stack.isEmpty() && !stack.peek().equals("(")) {//add every term until open bracket to queue, not including  closed parentheses
                            queue.enqueue(stack.pop());
                        }
                        stack.pop();
                    }
                }
            }

        while (!stack.isEmpty()){//add stack to queue

                queue.enqueue(stack.pop());
        }

        return queue;

    }

    /**
     * Will calculate solution given two numbers and an operation
     * @param operation: operation
     * @param number1: first number (will be subtracted from or divided in those cases)
     * @param number2: second number (will subtract from or divide in those cases)
     * @return answer to operation
     */
    public static int doOperation(String operation, int number1, int number2){
        if (operation.equals("^")) {double d2 = number2; return (int) Math.pow(number1,d2);}//E
        else if (operation.equals("*")){return number1 * number2;}
        else if (operation.equals("/")){return number1 / number2;}
        else if (operation.equals("+")){return number1 + number2;}
        else if (operation.equals("-")){return number1 - number2;}
        else{
            return 0;
        }
    }

    public static int postfix(LinkedQueue<String> linkedString){

        LinkedStack stack = new LinkedStack();

        while (!linkedString.isEmpty()){
            String item = linkedString.first().toString();
            linkedString.dequeue();

            if (isNumeric(item)){//if a number add to stack
                stack.push(item);
            }else if (isOperator(item)){//removes numbers and uses operation item on them
                int num1 = Integer.parseInt(stack.pop().toString());
                int num2 = Integer.parseInt(stack.pop().toString());
                stack.push(doOperation(item,num2,num1));//then adds new product

            }
        }
        return Integer.parseInt(stack.pop().toString());//will only be one number
    }


}

