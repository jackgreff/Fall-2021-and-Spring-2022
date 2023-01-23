file_handle = open("words.txt", "r")
# inp = "not empty"
# while inp != "":
#     inp = input("what string do you want to add?")
#     file_handle.write(inp+"\n")
#     # for a in range(len(filehandle)):
#     #     print(file_handle.readline())

top_length = 0
top_word = "a"
amount_right = 0
amount_total = 0

for a in file_handle:
    a = a[:-1]
    if len(a) == 3:
        print(a)
    if len(a) > top_length:
        top_word = a
        top_length = len(a)
    if (a[0] == "g" or a[0] == "k") and a[1] == "n":
        print(a)
    if a[0] == "a" or a[0] == "e" or a[0] == "i" or a[0] == "o" or a[0] == "u":
        amount_right += 1
        amount_total += 1
    else:
        amount_total += 1

print(amount_right*100//amount_total)

file_handle.close()