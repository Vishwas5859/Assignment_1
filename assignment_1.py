
# Interview coding questions--


#1. The included code stub will read an integer, , from STDIN.
#Without using any string methods, try to print the following: 123...n
#ex: n=5   o/p = 12345, n=3  o/p = 123.

n = int(input())
for i in range(1,n+1):
    print(i,end='')

# - - - - - - - - - - - - - -- - - - -  -- - -  -- -- - - - - - - - - - - - - - - - - - -
# 2. WAP a program to print i/p -> a4b4 o/p ->aaaabbbb

string = input('Enter a string: ')

output = ""
for i in string:
    if i.isalpha():
        temp = i 
    else:
        temp2 = int(i)
        output = output+temp*temp2
print(output)        
# - - - - - - - - - - - - - -- - - - -  -- - -  -- -- - - - - - - - - - - - - - - - - - -

# 3. Write a Python program to get a list, sorted in increasing order by the 
#last element in each tuple from a given list of non-empty tuples

Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def last_element(x):
    return x[-1]

def sorted_list(tuples):
    return sorted(tuples,key=last_element)

print(sorted_list(list1))    

# ------------------------------------------------------------------------------------------------------
# 4. WAP a program to skip 2 and 4 in a series of number from 1,2,3,4,5,5,6,7,8

for i in range(1,9):
    if i == 2 or i == 4:
        continue
    print(i)    
# ------------------------------------------------------------------------------------------------------    

# 5. WAP to reverse a string Ex: Edyoda to adoydE

string  = "Edyoda"
reverse = string[::-1]
print(reverse)
# ------------------------------------------------------------------------------------------------------    

# 6. WAP to find the highest number from the list

list1 = list(map(int,input("Enter a list: ").split()))
print(list1)

max_num = sorted(list1)
print(max_num[-1])

print(max(list1))
# ------------------------------------------------------------------------------------------------------    

# 7. WAP to convert a given tuple of positive integers to integer (1,2,3)
#I/P - (1,2,3), O/P - 123 

tuple1 = tuple(map(int,input("Enter a tuple: ").split()))
x = int(''.join(map(str,tuple1)))
print(x)
# ------------------------------------------------------------------------------------------------------    
# 8. WAP to print letter "L" in stars "*"

for i in range(8):
    if i == 7:
        print("* "*i)
    else:
        print("*")    
#---------------------------------------------------------------------------------------------------------    
# 9. WAP to remove empty tuples from a list
# [(),(),(","),('a','b'),('d'),('a','b','c')]

list1 = [(),(),(","),('a','b'),('d'),('a','b','c')]
result = []
for i in list1:
    if len(i) == 0:
        list1.remove(i)
    elif len(i) > 0:
        result.append(i)
print(result)
#--------------------------------------------------------------------------------------------------------
#10. Write a Python function to sum all the numbers in a list.

def summation(tuple1):
    result=sum(tuple1)
    print("Sum of tuple is: ",result)
    return 

tuple1 = tuple(map(int,input("enter a tuple: ").split()))
print(tuple1)
summation(tuple1)

# ---------------------------------------------------------------------------

#11. Write a Python program to reverse a string.

def reverse_string(string1):
    result = string1[::-1]
    print("reverse of the string is: ",result)
    return

string1 = input("Enter a string: ")
reverse_string(string1)

# ---------------------------------------------------------------------------

# 12. Write a Python function that accepts a string and calculate 
# the number of upper case letters and lower case letters.

def string_case(string1):
    upper_case = 0
    lower_case = 0
    for i in string1:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
        else:
            continue  
    print("Original string is: ",string1)
    print("No. of Upper case characters: ",upper_case)
    print("No. of Lower case characters: ",lower_case)
    return


# string1 = input("Enter a string: ")        
# string_case(string1)
# ---------------------------------------------------------------------------

# 13. WAP to build a dict, where its value must be a square of key:
# Ex: {1:1,2:4,3:9}

dict1 ={}
n = int(input())
for i in range(1,n+1):
    dict1[i] = i*i
print(dict1)
#-------------------------------------------------------------------------------------------
#14. Take input from 3 users and determine oldest and youngest among them
list1 =[]
age1 = int(input("Enter the age1: "))
age2 = int(input("Enter the age2: "))
age3 = int(input("Enter the age3: "))

x = list1.append(age1)
y= list1.append(age2)
z = list1.append(age3)
print('All age goups in list: ',list1)

sort = sorted(list1)
print('The youngest is: ',list1[0])
print('The oldest is: ',list1[-1])
#-------------------------------------------------------------------------------------------
#15. Find all the numbers from 1-1000 that are divisible by 7, using list comprehension.

for i in range(1,1001):
    if i%7==0:
        print(i,end=",")

x = list(range(1,1001))

output = [i for i in x if i%7==0]
print(output) 
#-------------------------------------------------------------------------------------------
# 16. Write a Python program to create a lambda function that adds 25 to a given 
# number passed in as an argument.
# sample input: 10
# sample output: 35

num = int(input("Enter a number: "))

add = lambda num: num+25

print("added number: ",add(num))
#--------------------------------------------------------------------------------------------------
#17. Write a Python program to triple all numbers of a given list of integers. Use Python map.
# sample list: [1, 2, 3, 4, 5, 6, 7]

# Triple of list numbers:

# [3, 6, 9, 12, 15, 18, 21]
list1 = list(map(int,input("Enter a numbers: ").split()))
print("The list of Integers is: ",list1)
def triple(num):
    return num*3

result = map(triple,list1)
print("The triple of list is: ",list(result))
#-----------------------------------------------------------------------------------------------------

#18. Write a Python program to square the elements of a list using map() function.

# Sample List: [4, 5, 2, 9]

# Square the elements of the list:

# [16, 25, 4, 81]


list1= list(map(int,input("Enter a list1: ").split()))

def square_list(num):
    return num**2

result = list(map(square_list,list1))
print("Square of a list1 is: ",result)
#-----------------------------------------------------------------------------------------------------

# 19. WAP to calculate area of circle based on radius as user input.


def circle_area(r):
    return 3.141*(r**2)

r = int(input("Enter the radius of circle: "))
print("Area of circle is ",circle_area(r))
#-----------------------------------------------------------------------------------------------------
# 20. WAP that accepts user first and last name and prints them in reverse way with sapce between them

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

x = last_name+" "+first_name
print("Reverse of first and last name is: ",x)
#-----------------------------------------------------------------------------------------------------
# 21. WAP to accept comma seperated numbers from user and convert it into list and tuple
# I/P = 1,2,3
#o/p = ['1','2','3'] and ('1','2','3')

list1 = list(map(str,input().split(',')))

tuple1 = tuple(map(str,input().split(',')))
print(list1)
print(tuple1)
#-----------------------------------------------------------------------------------------------------
#22 WAP to count No.4 in given list

list1 = [1,2,3,4,5,4,5,4]

list2 = []
for i in list1:
    if i == 4:
        list2.append(i)
print("count of No.4 in list1 is: ",len(list2))       
 
or

x = list1.count(4)
print(x)
#-----------------------------------------------------------------------------------------------------

#23. WAP to check whether a specified value is contained within a group of values.
# test date 3 -> [1,4,3,5] True , -1 -> in [1,4,3,5] False

list1 = list(map(int,input("Enter a list: ").split()))

x = int(input("Enter a value: "))

if x in list1:
     print("True")
else:
    print("False")     
#-----------------------------------------------------------------------------------------------------
# 24. WAP to concatenate the elements in a list to a string and returns

list1 = ["hi","this",'is',"Vishwas"]
join = " ".join(list1)
print(join)

list1 = input().split()
print(list1)
x = ' '.join(list1)
print(x)


#------------------------------------------------------------------------------------------------------
# 25. WAP to interchange first and last element of a list. list integers are provided by user.

def swapList(newList):
     
    newList[0], newList[-1] = newList[-1], newList[0]
 
    return newList

newList = list(map(int,input().split()))
print(newList)
print("Swap of newlist is: ",swapList(newList))