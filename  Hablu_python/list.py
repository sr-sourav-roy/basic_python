# #Int type data
# # list = [1,2,3,4]
# # print(list)
# # print(type(list))
# # list[2] = 8
# # print(list)
#
# # #String type data
# # list = ["sourav","rintu","antto","badhon"]
# # print(type(list))
# # print(list)
# # list[2] = "labib"
# # print(list)
#
# #boolean type data
#
# list = [True, True, False, False]
# print(type(list))
# print(list)
#
# sourav = ["rintu","ffff","sourav","badhon","kkk"]
# #accces list items
# print(sourav[1])
# sourav[1] = "liton"
# sourav[4] = "forid"
# print(sourav)
#
# #append
# sourav.append(12)
# print(sourav)
#
# #insart
# sourav.insert(4,"annto")
# print(sourav)
#
# new_sourav = ["rintu","ffff","sourav","badhon",97]
# #The revove() mathod the specified item.
# new_sourav.remove(97)
# print(new_sourav)
#
# #pop mathod
# new_sourav.pop(1)
# print(new_sourav)
#
# #clear mathod
# sourav.clear()
# print(sourav)

#You can loop through the list items by using a for loop:
#looplist = ["bristy","keya","puja1","jui","puja","akhi","asha"]

# for magi in looplist:
#     print(magi)

#Use the range() and len() function to create a sutable iteraable
# for i in range(len(looplist)):
#     print(i)
#
# #print all items, using a shile loop to go through all the index numbers
# looplist = ["bristy","keya","puja1","jui","puja","akhi","asha"]
# y = 0
# while y < len(looplist): # len(looplist) = number type(7) # conditon
#     print(looplist[y])
#     y = y + 1

# # list comprehensions
# numbers = [2,3,4,5,6]
# new_list = [i *5 for i in numbers] # one line answer
# print(new_list)
#
#
# #Or
# numbers = [1,2,3,4,5,6]
# for i in numbers:
#     print(i *2)

# #sort list
# numbers =[8,5,2,1,7,4,3,5,6,9,10]
# numbers.sort()
# print(numbers)
# #agin
# eng = ["d","c","b","a"]
# eng.sort()
# print(eng)
#
# num = [1,2,3,4,5,7,8,9]
# num.sort(reverse=True)
# print(num)
#
# sourav = ["d","c","b","a"]
# sourav.reverse()
# print(sourav)

sourav = ["A","B","C"]
rintu =[10,20,30]

sourav.extend(rintu)
print(sourav)



















