# def switch(dataType):
#     if dataType == "Integer":
#         return 4
#     elif dataType == "Character":
#         return 1
#     elif dataType == "Float":
#         return 4
#     elif dataType == "Long":
#         return 4
#     elif dataType == "Double":
#         return 8
#
#
#
#
# print(switch("Integer"))


# ----

# fruits = ['banan', 'apple', 'Mango']
# # for fruit in fruits:
# #     print(fruit,'\n')
# # print(x)
#
#
# for fruit in fruits:
#     if fruit == 'apple':
#         continue
#     print(fruit)
#
#


# --- Inverted Stars


# numberOfLine: int = int(input('How many Lines of starts do you want : '))
#
# for i in range(numberOfLine):
#     if i == 0:
#         print('*\n')
#         continue
#
#     for j in range(i + 2):
#         print("*", end='')
#
#     print('\n')


# ---- Palindrone Number
#
#
# palindroneNumber = int(input("Enter a Number: "))
#
# palindronearray = []
# isPalindrone = True
#
# while int(palindroneNumber) > 0:
#     palindronearray.append(palindroneNumber % 10)
#     palindroneNumber = int(palindroneNumber/10)
#
# for i in range(int(len(palindronearray)/2)):
#     if palindronearray[i] == palindronearray[len(palindronearray)-1-i]:
#         continue
#     else:
#         isPalindrone = False
#         print(False)
#         break
#
# if isPalindrone:
#     print(True)
#
#
#


# ----- GCF Greatest Common Factor/Divisor
#
# gcfArray = [2,3,5]
# isGcfFound = False
#
# inputValue1, inputValue2 = (input("Enter Two number : ").split())
#
# for value in gcfArray:
#     x = int(inputValue1) % value
#     y = int(inputValue2) % value
#
#     if x == 0 and y == 0:
#         print(True)
#         isGcfFound = True
#         break
#
# if not isGcfFound:
#     print(False)
#


# --- Sum of N using Recursion


# def Sum(n):
#     if n < 2:
#         return n
#     else:
#         return n + Sum(n-1)
#
# print(Sum(5))


def Fib(n):
    if n <= 1:
        return n

    return Fib(n - 1) + Fib(n - 2)


print(Fib(5))
