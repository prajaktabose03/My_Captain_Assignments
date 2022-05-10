list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

 
print("Input: " +str(list1))
# using list comprehension
pos_nos = [num for num in list1 if num >= 0]
  
print("Output: " , *pos_nos)





print("Input: " +str(list2))  
# using list comprehension
pos_noss = [num1 for num1 in list2 if num1 >= 0]
  
print("Output: ", *pos_noss)
