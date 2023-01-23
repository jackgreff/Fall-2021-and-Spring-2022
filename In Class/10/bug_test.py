def add_underscore(word:str) ->str:
    new_word = "_"
    for i in range(len(word)):
        new_word = new_word+word[i] + "_"
    return new_word

# print(add_underscore("hello"))

number = 5
my_list = {-1,5,2,12,7,3,8,1,2,3,3,0, -1}
low = []

for element in my_list:
    if element < number:
        low.append(element)
    print(element, low)


print(low)

def calculate(weight,height):
    return weight/(height**2)

patients = [[70,1.8],[80,1.9],[50,1.6],[173/2.2,1.85]]

# for i in range(len(patients)):
#     bmi = calculate(patients[i][0],patients[i][1])
#     print(bmi)

for patient in patients:
    bmi = calculate(patient[0], patient[1])
    print("Patient's bmi is %f" % bmi)