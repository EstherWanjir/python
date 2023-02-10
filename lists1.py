#my second python lists
numbers= [45,96,56,89,45]

print(len(numbers))#get the length of my list

print(sum(numbers))#get the sum of my list

for i in range ( len(numbers)):
    print(numbers[i])
print(numbers.index(56))

# Index
#append-adds an element to the end of a list
#sort-arranges the list in an ascending order
#count- returns the number of times an element occurs in the list
#pop- removes an element at a given index and returns that element
#insert-puts element x at index y
#remove-gets rid of the first occurrence of an element from a list



# before appending
for i in  range (len(numbers)):
    print(numbers[i])

print("/n") 
numbers.append(90)   

# after appending
for i in  range (len(numbers))  :
    print(numbers[i])  

print(numbers.count(45))
print(numbers.pop(2))

# print("n/") - add a new line for formatted output
numbers.insert(2,100)

for i in range (len(numbers)):
    print(numbers[i])

numbers.remove(45)

for i in range (len(numbers)):
    print(numbers[i])
numbers.sort()
print(numbers)

# tips and tricks

# multiplying a list

numbers=[0]*5
print(numbers)

# adding one list to an other
list1=[45,96]
list2=[56,80]
list3=list1+list2
print(list3)

# to split/slice a list
nums= [12,67,45,36,78]
nums[2:]
print(nums[2:])

#creating lists
nums=[]#empty list
for i in range(5):
    #insert elements  in the list
    nums.append(i)

for i in range (len (nums)):
    print (nums[i]) 
# find the max number 
print(list3) 

# exercises
print(10%2)
for num in range (20):
 if (num%2)==0:
  nums .append(num)