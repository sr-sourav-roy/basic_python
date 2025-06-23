# #pattan of * python
# def pattern(s):
#     for i in range(0,s):
#         for j in range(0,i + 1):
#             print("I ❤️ Piku", end="")
#         print("\r")
#     for i in range(s, 0, -1):
#         for j in range(0,i +1):
#             print("I ❤️ Piku", end="")
#         print("\r")
#
# pattern(10)

def pattern(n):
    k = n - 2
    for i in range(n, -1 ,-1):
        for j in range(k, 0, -1):
            print(end=" ")
        k +=1
        for j in range(0, i+1):
           print("Good Morning💙 ", end=" ")
        print("\r")
    k = 2 * n - 2
    for i in range(0, n+1):
        for j in range(0, k):
            print(end=" ")

        k = k -1
        for j in range(0, i + 1):
            print("Jannnnnnnnnn❤️❤️", end=" ")
        print("\r")

pattern(10)
