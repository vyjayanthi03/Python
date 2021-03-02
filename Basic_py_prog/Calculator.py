                                    ###############Cal With LIST########

select = input('select one operator(Addition;Subtraction;Multiplication;Division): ')
if select in ('Addition','Subtraction','Multiplication','Division'):
    num = int(input('Size of the list1:'))
    li1 = []
    for i in range(num):
        list1 = float(input('Input list no:'))
        li1.append(list1)
    num = int(input('Size of the list2:'))
    li2 = []
    for i in range(num):
        list2 = float(input('Input list no:'))
        li2.append(list2)
    output = []
    if select == 'Addition':
        for l in range(num):
            output = (li1[l]+li2[l])
            print(li1[l],'+',li2[l], '=', output)
    if select == 'Subtraction':
        for l in range(num):
            output = (li1[l]-li2[l])
            print(output)
    if select == 'Multiplication':
        for l in range(num):
            output = (li1[l]*li2[l])
            print(output)
    if select == 'Division':
        for l in range(num):
            output = (li1[l]/li2[l])
            print(output)
else:
    print('Invalid input')




                                    ###############Cal##############

# def add(x, y):
#     return x + y
#
#
# def subtract(x, y):
#     return x - y
#
#
# def multiply(x, y):
#     return x * y
#
# def divide(x, y):
#     return x / y
#
#
# print("Select operation.")
# print("Add:Addition")
# print("Subtract:Subtraction")
# print("Multiply:Multiplication")
# print("Divide:Division")
#
# while True:
#     select = input("select operator to do(Addition;Subtraction;Multiplication;Division): ")
#
#     if select in ('Addition', 'Subtraction', 'Multiplication', 'Division'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#
#         if select == 'Addition':
#             print(num1, "+", num2, "=", add(num1, num2))
#
#         elif select == 'Subtraction':
#             print(num1, "-", num2, "=", subtract(num1, num2))
#
#         elif select == 'Multiplication':
#             print(num1, "*", num2, "=", multiply(num1, num2))
#
#         elif select == 'Division':
#             print(num1, "/", num2, "=", divide(num1, num2))
#         break
#     else:
#         print("Invalid Input")
