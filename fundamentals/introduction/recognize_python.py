num1 = 42  #declaring variable integer/number
num2 = 2.3 #declaring variable float/decimal
boolean = True #declaring variable, boolean
string = 'Hello World' #declaring variable, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #declaring variable/list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #declaring variable, dictionary
fruit = ('blueberry', 'strawberry', 'banana') #declaring variable, tuple
print(type(fruit)) #print to console and state type check tuple
print(pizza_toppings[1]) #print to console and print sausage in the list
pizza_toppings.append('Mushrooms') # add mushrooms to the list at the end
print(person['name']) #print to console John in the dictionary 
person['name'] = 'George' #change John to George in the dictionary 
person['eye_color'] = 'blue' #add eye color to the dictionary because the key value does not have a pair
print(fruit[2]) #print to console banana

if num1 > 45: #conditional if statment, if num1 is greater than 45 print to console conditional else, print to console
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: #conditional if statement, print to console, else if print to console, else print to console
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop print 0,1,2,3,4,5
    print(x)
for x in range(2,5):#for loop print 2,3,4,5
    print(x)
for x in range(2,10,3): #for loop print 2 up to 10 by 3's 2,5,8
    print(x)
x = 0 #while loop variable x declared as 0
while(x < 5): #while x < 5 print to console
    print(x)
    x += 1 #and increment x by 1

pizza_toppings.pop() #delete last value olives
pizza_toppings.pop(1) #delete index 1 sausage

print(person) #print to console John Salt Lake 37 false
person.pop('eye_color') #remove eye color from dictionary 
print(person) #print to console John Salt lake 37 false

for topping in pizza_toppings: #for loop pizza toppings 
    if topping == 'Pepperoni': #conditional if statement. if topping = pepperoni continue and print to consolde
        continue
    print('After 1st if statement')
    if topping == 'Olives': #if topping equals olives stop the for loop
        break

def print_hello_ten_times(): #declares function
    for num in range(10): #for loop starts 0-10
        print('Hello') #print to console hello

print_hello_ten_times() #function call

def print_hello_x_times(x): #declares function wtih parameter x
    for num in range(x): #for loop given number x
        print('Hello') #print to console hello

print_hello_x_times(4) #function call agrument of 4 so x becomes 4

def print_hello_x_or_ten_times(x = 10): #declares function with parameter
    for num in range(x): #for loop 
        print('Hello') #print to console

print_hello_x_or_ten_times() #function call goes to 10
print_hello_x_or_ten_times(4) #function call goes to 4


"""
Bonus section
"""

# print(num3) #72
# num3 = 72
# fruit[0] = 'cranberry' #tuples cannot be changed this could return blueberry not replace blueberry with cranberry
# print(person['favorite_team']) #favorite team is added to the dictionary
# print(pizza_toppings[7]) 
#   print(boolean) 
# fruit.append('raspberry') tuples cannot be changed
# fruit.pop(1)  tuples cannot be changed