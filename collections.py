my_list=[1,2,3,4,5]
print(len(my_list))

nums = [3,1,4,1,5,9,2]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

words=["banana", "apple", "cherry"]
words.sort(key=len)
print(words)

sorted_nums = sorted(nums)
print(sorted_nums)

sorted_nums_desc=sorted(nums, reverse= True)
print(sorted_nums_desc)

sorted_words= sorted(words, key=len)
print(sorted_words)

s = "Hello"
print(s.upper())
s="Some Text"
print(s.lower())
s="Bill Jons"
print(s.startswith("Bi"))
s="hello.jpg"
print(s.endswith("jpg"))

name='John'
print('Hello, {}!'.format(name))
age=25
print('Hello,{}. You are {} years old.'.format(name, age))
print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))
print('Hello, {1}. You are {0} years old.'.format(age,name))

numbers=[1,2,3,4,5,6,7,8,9,10]
reverse_numbers=numbers[::-1]
print(reverse_numbers)
copy_numbers=numbers[:]
print(copy_numbers)

num=15
if num > 10:
    print("num is bigger than 10")
else:
    print("num is not bigger than 10")

money=0
if money:
    print(f"You have {money} on your bank account")
else:
    print("You have no money and no debts")

result= None
if result:
    print(result)
else:
    print("Result is None, do something")

a=[1,2,3]
b=a
c=[1,2,3]
print(a is b)
print(a is c)

name="Taras"
age=22
has_driver_license=True

if name and age >= 18 and has_driver_license:
    print(f"User {name} can rent a car")

num= int(input(10))
if num % 3==0 and num %5== 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")  
else:
    print(num) 

if x >=0:
    if y>=0: # x > 0, y > 0
        print("First Quarter")
    else: # x > 0, y < 0
        print("Fourth Qaurter")
else:
    if y >= 0: # x < 0, y > 0
        print("Second Quarter")
    else: # x < 0, y < 0
     print("Third Quarter")      
     