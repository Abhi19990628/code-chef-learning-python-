
# Python program for searching in
# unsorted array


def findElement(arr, n, key):
	for i in range(n):
		if (arr[i] == key):
			return i
		
	# If the key is not found
	return -1


# Driver's code
if __name__ == '__main__':
	arr = [12, 34, 10, 6, 40]
	key = 40
	n = len(arr)

	# search operation
	index = findElement(arr, n, key)
	if index != -1:
		print("Element Found at position: " + str(index + 1))
	else:
		print("Element not found")

	# Thanks to Aditi Sharma for contributing
	# this code


#   next qution   $$$$$ -----------



# Write a Python program to create an array of 5 integers and display the array items.
# Access individual elements through indexes.

from array import *
array_num = array('i', [1,3,5,7,9])
for i in array_num:
    print(i)
print("Access first three items individually")
print(array_num[0])
print(array_num[1])
print(array_num[2])




# access any num from anywhere if you want 


from array import *
array_num = array('i', [1,2,3,4,5])

for i in array_num:
  print(i)

print("access the first three items")

print(array_num [0])
print(array_num [4])
print(array_num [3])

# append program in array

 
list = [1,2,3,4,5]
x= [6,7,8]
list.append(x)
print(list)

# secound program in append 

from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Append 11 at the end of the array:")
array_num.append(11)
print("New array: "+str(array_num))



import numpy as np

x=np.arange(3)
print("Array x : ", x)

y=np.arange(10,15)
print("Array y : " ,y)

result= np.append(x,y)
print("result after appending x and y:",result)


# simple caculater

a=50
b=3

print( "the value of", a , " + " , b , "is:" , a+b)
print( "the value of", a , " * " , b , "is:" , a*b)
print( "the value of", a , " - " , b , "is:" , a-b)
print( "the value of", a , " / " , b , "is:" , a/b)

# type casting

a="1" # one is string becouse we use this ("")
b="3" # 3 num is also string 
#print (a+b)

# we got the result  13

# if want 1+3=4

#a=1
#b=3
#print(a+b)

# so we use type of casting 
print(int(a)+int (b))
#first tell computer int is value 

string="5"
number = 3
string_number=int (string)
sum = string_number+number
print (sum)

# input method

a=input("Enter your first name: ")
b=input("Enter your lastname: ")
print("my name is : ", a+b )

# on math

X = input("Enter your first num: ")
y = input("Enter your second num : ")
print(x + y)