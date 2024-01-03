# input as intnger

#and how get input 

# x=input("enter fst num : ")
# y=input("enter sec num : ")
# print(x+y)
# print(int(x)+int(y))

# str='''Klmlm Lmo is on Facebook. Join Facebook to connect with Klmlm Lmo and others you may know. Facebook gives people the power to share and makes the world.'''
# print(str)


a = "abhishek"
print(len(a))
# print(a.upper())
# print(a.replace ("abhishek","ramnath"))


#if else condition   
x =int(input("enter your age :"))
print ("your age is :",x)
if (x>=18):
        print("you r good")
else :
        print("you r not good")

# num = int(input("enter the num :"))
# if (num<0):
#     print("negitive num")
# elif(num>0):
#     print("postive num")
# elif(num==0):
#     print("equal")
    
    
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)

thislist =["apple", "banana" ,"yellow" ,"red"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)

# remove in list 


thislist =["yellow","banana","red"]
thislist.remove("red")
print(thislist)

thislist =["yellow","banana","red"]
thislist.pop(1)
print(thislist)

thislist =["yellow","banana","red"]
del thislist[0]
print(thislist)

  
