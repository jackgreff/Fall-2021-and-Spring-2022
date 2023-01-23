//Jack Greff, 1/23/22, Week 1 Lab/Basic Coding
package basic;

public class Main {
	public enum Standing {FIRST_YEAR, SOPHOMORE, JUNIOR, SENIOR};


	public static void main(String[] args) {
		/*
		TODO: You should call the functions you create from this function in order
		to test them. You can check that your Eclipse setup is correct by running
		this file - you should see the below printout in the Console window. After
		that, you may remove it.
		*/

		//EXAMPLES:
		System.out.println(power(3.50,2));//non-integer base too
		System.out.println(gcd(25,5));//includes one that includes itself
		System.out.println(isPrime(27));
		System.out.println(round(5.49));//gave one close to .5
		System.out.println(classYear(Standing.SENIOR)); //chose one of 4


	}

	public static double power(double x, int exp){
		//multiplies 1 by x 'exp' number of times
		double answer = 1;
		while (exp > 0){
			answer = answer * x;
			exp--;
		}
		return answer;

	}

	public static float gcd(int num1, int num2){
		//will go through every integer between 1 and either number, then both numbers are checked for remainders
		//if both have none the current level is the new gcd
		float gcd = -1; //will be changed immediately by 1, current value arbitrary
		int currentLevel = 1;//starts at 1
		while (currentLevel <= num1){//<= because can include self
			if ((num1 % currentLevel == 0) && (num2 % currentLevel == 0)){
				gcd = currentLevel;
			}
			currentLevel++;
		}
		return gcd;

	}

	public static boolean isPrime(int num){
		//if every integer between 2 and itself doesn't divide evenly, then it is prime
		boolean prime = true;
		if (num == 1){
			prime = false;		//turns out 1 is not prime, so if one will not go through loop and now say false

		}
		int currentLevel = 2;//1 always divides evenly, so start at 2.
		while (currentLevel < num){//doesn't include itself since dividing it would be 1
			if (num % currentLevel == 0){//if divides evenly
				prime = false;
				break;
			}
			currentLevel++;
		}
		return prime;

	}

	public static double round(double num){
		//rounds number to nearest whole number

		double base = num - num % 1; //use modulo to find remainder, create base
		double remainder = num % 1;

		if (remainder >= .5){//if remainder is above .5, round up
			base = base + 1;
		}
		return base;
	}


	public static String classYear(Standing st){
		//Given each year, will return year of graduation
		if (st == Standing.FIRST_YEAR){
			return "Class of 2025";
		}else if (st == Standing.SOPHOMORE){
			return "Class of 2024";
		} if (st == Standing.JUNIOR){
			return "Class of 2023";
		} if (st == Standing.SENIOR){
			return "Class of 2022";
		}else
			return "Invalid Input";
	}

}
