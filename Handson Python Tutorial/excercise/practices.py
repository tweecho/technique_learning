"""
Classic program to start learning programming
《Hands-on Python Tutorial》

Author: Xiaoling Zhang
Date: 2020-01-06
"""

"""First print statement"""

print("hello world") # A print statement


""" Greeting"""

person = input("Please enter your name: ")
print('Hello, ', person, "!", sep='')


"""Illustrate input and print."""

applicant = input("Enter the applicant's name: ")
interviewer = input("Enter the interviewer's name: ")
time = input("Enter the appointment time: ")
print(interviewer, "will interview", applicant, "at", time)


"""Error in addition from input"""

x = input("Enter a number: ")
y = input("Enter a second number: ")
print('The sum of ', x, ' and ', y, ' is ', x+y, sep="") # Error


"""Conversion of strings to int before addition"""

xString = input("Enter a number: ")
x = int(xString)
yString = input('Enter a second number: ')
y = int(yString)
print('The sum of ', x, ' and ', 'y', ' is ', x+y, '.', sep='')


"""Two numeric inputs, explicit sum"""

x = int(input("Enter an integer: "))
y = int(input("Enter another integer: "))
sum = x + y
print('The sum of ', x, ' and ', y, ' is ', sum, '.', sep='')
print('The sum of {} and {} is {}'.format(x, y, sum))


"""Add three numbers up"""

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
print("The sum of ", num1, ' , ', num2, ' and ', num3, ' is ', num1 + num2 + num3, sep='')


"""Division and Remainders"""

div1 = int(input("Enter the integer being divided: "))
div2 = int(input("Enter the integer that is the divisor"))
quotient = div1 // div2
remainder = div1 % div2
print("The quotient of ", div1, ' and ', div2, ' is ', quotient, sep='')
print("The remainder of ", div1, ' and ', div2, ' is ', remainder, sep='')


"""Hello to you! Illustrates format with {} in print"""

person = input("Enter your name: ")
greeting = 'Hello, {}!'.format(person)
print(greeting)


"""Compare print with concatenation and with format string."""

applicant = input("Enther the applicant's name: ")
interviewer = input("Enter the interviewer's name: ")
time = input("Enter the appointment time: ")
print(interviewer + ' will interview ' + applicant +  ' at ' + time + '.')
print(interviewer, ' will interview ', applicant, ' at ', time, '.', sep='')
print('{} will interview {} at {}.'.format(interviewer, applicant, time))
print('{0} will interview {1} at {2}.'.format(interviewer, applicant, time))


"""Illustrate braces in a formatted string."""

a = 5
b = 9

setStr = 'The set is {{{}, {}}}.'.format(a, b)
print(setStr)


"""
Facier format string example with parameter identification numbers
-- useful when some parameters are used several times.
"""

x = int(input("Enter an integer: "))
y = int(input("Enter another integer: "))
formatStr = '{0} + {1} = {2}; {0} * {1} = {3}'
equations = formatStr.format(x, y, x+y, x*y)
print(equations)


"""Verbose 'Happy birthday' song"""

print("Happy birthday to you.")
print("Happy birthday to you.")
print("Happy birthday, dear Emily")
print("Happy birthday to you!")


"""First function"""

def happyBirthdayEmily(): #program does nothing as written
    print("Happy birthday to you.")
    print("Happy birthday to you.")
    print("Happy birthday, dear Emily")
    print("Happy birthday to you!")


"""The significance of a line being indented"""

def f():
    print("In function f")
    print("When does this print?")
f()

def f():
    print("In function f")
print("When does this print?")
f()


"""Exercise Poem P34"""

def poem():
    print("To be")
    print("or not to be")
    print("That is the question")

poem()
poem()
poem()


"""function with parameters called in main"""

def happyBirthday(person):
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print("Happy birthday, dear " + person + '.')
    print("Happy birthday to you!")

def main():
    happyBirthday("Emily")
    happyBirthday("Andre")

main()


"""Quotient function exercise"""

def quotientProblem(x, y):
    quotient = x // y
    print(quotient)

    return "The quotient of {} and {} is {}.".format(x, y, quotient)

def main():
    quotientProblem(23, 34)
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    quotientProblem(a, b)
    print(quotientProblem(a, b))

main()


"""A change to badScope.py avoiding any error by passing a parameter"""

def main():
    x = 3
    f(x)

def f(x):
    print(x)

main()


"""Illustrate a global constant being used inside functions."""

PI = 3.14159265358979   # global constant -- only place the value of PI is set

def circleArea(radius):
    return PI * radius * radius     # Use value of global constant PI

def circleCircumference(radius):
    return 2 * PI * radius      # Use value of global constant PI

def main():
    print('Circle area with radius 5: ', circleArea(5))
    print('Circumference with radius 5: ', circleCircumference(5))

main()


"""
A tiny English to Spanish dictionary is created,
using the Python dictionary type dict.
Then the dictionary is used, briefly.
"""

def createDictionary():
    """Returns a tiny Spanish dictionary"""

    spanish = dict()
    spanish['hello'] = 'hola'
    spanish['yes'] = 'si'
    spanish['one'] = 'uno'
    spanish['two'] = 'dos'

    return spanish

def main():
    dictionary = createDictionary()
    print(dictionary['two'])
    print(dictionary['one'])
    print("Count in Spanish: " + dictionary['one'] + ' , ' + dictionary["two"] + ' , ' + ' ... ')

main()

numberFormat = 'Count in Spanish: {one}, {two}, {three}, ...'
withSubstitutions = numberFormat.format(one='uno', two='dos', three='tres')
print(withSubstitutions)


"""A tiny Python program -- Number Dictionary Exercise"""

def numDict():
    numDictionary = dict()

    numDictionary['one'] = 1
    numDictionary['two'] = 2
    numDictionary['three'] = 3
    numDictionary['four'] = 4

    return numDictionary

def main():
    dictionary = numDict()

    print(dictionary['one'], dictionary['two'], 'and', dictionary['three'])

main()


"""
String Substitution for a Mad Lib
Adapted from code by Kirby Urner
"""

storyFormat = """                                       
Once upon a time, deep in an ancient {place},
there lived a {animal}.  This {animal}
liked to eat {food}, but the jungle had
very little {food} to offer.  One day, an
explorer found the {animal} and discovered
it liked {food}.  The {agent} took the
{animal} back to {city}, where it could
eat as much {food} as it wanted.  However,
the {animal} became homesick, so the
{agent} brought it back to the jungle,
leaving a large supply of {food}.

The End
"""

def tellStory():
    userPicks = dict()
    addPick('animal', userPicks)
    addPick('food', userPicks)
    addPick('city', userPicks)
    addPick('agent', userPicks)
    addPick('place', userPicks)
    story = storyFormat.format(**userPicks)
    print(story)

def addPick(cue, dictionary):
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    prompt = 'Enter an example for ' + cue + ': '
    response = input(prompt).strip() # 3.2 Windows bug fix
    dictionary[cue] = response

tellStory()
input("Press Enter to end the program.")


"""Fancier format string example, with locals()."""

x = 20
y = 30
sum = x + y
prod = x * y
formatStr = '{x} + {y} = {sum}; x * y = {prod}.'
equations = formatStr.format(**locals()) # Locals() return a dictionary
                                         # containing all the current local
                                         # variables names as keys and all
                                         # their values as the corresponding
                                         # dictionary values.
print(equations)


"""Fancier f-string example for formatting"""

x = 20
y = 30
sum = x + y
prod = x * y
print(f'{x} + {y} = {sum}; {x} * {y} = {prod}.')
# automatically substituting local variable values


"""Quotient string dictionary exercise P47"""

def quotientDict():
    x = int(input("Enter an integer: "))
    y = int(input("Enter another integer: "))

    quotient = x // y
    formatStr = "The quotient of {x} and {y} is {quotient}."

    print(formatStr.format(**locals()))
    print(f"The quotient of {x} and {y} is {quotient}.")

quotientDict()


"""Updating variables"""
x = 3
y = x + 2
y = 2 * y
x = y - x
print(x, y)


"""Pattern Loop exercise"""

pattern_list = [2, 3.5, [], True, False]
for item in pattern_list:
    print(item, type(item))


"""Triple exercise"""

def tripleAll(nums):
    for num in nums:
        num *= 3
        print(num)

tripleAll([2,5,1,4])


"""Successive Modification Loops"""
items = ['red', 'orange', 'yellow', 'green']
number = 1
for item in items:
    print(number, item)
    number = number + 1


"""Accumulation loops"""

def sumList(nums):
    """Return the sum of the numbers in nums"""
    sum = 0

    for num in nums:
        sum += num
    print(sum)


"""Floating Point Exercise"""

def discount(original_price, discount_percentage):
    """Function for the calculation of the new price to the nearest cent after discount"""

    value = (1 - discount_percentage/100) * original_price
    print("The value after discount is {value:.2f}".format(**locals()))
    print(f"The value after discount is {value:.2f}")

    return value

def main():
    original_price = float(input("Enter the original price: "))
    discount_percentage = float(input("Enter the discount percentage provided: "))
    test1 = discount(original_price, discount_percentage)
    print(test1)

main()  # Invoke main function here


"""function, data, type are all objects"""

s = "Hello!"
x = s.lower()
y = s.upper()
xy = x + y
xx = xy.count('e')


"""Underscore exercise P79"""

sent = "This is the sentence for underscore"
seq = sent.split(" ")
underscore = "_".join(seq)


"""Acronym Exercise P79"""

string = input("Please enter the string for acronym exercise: ")
seq = string.split()
acronym = ''
for word in seq:    # First version of implementation
    first_letter = word[0].upper()
    acronym += first_letter

string = input("Please enter the string for acronym exercise: ")
seq = string.split()
acronym = []
acronyms = ''
for word in seq:
    first_letter = word[0].upper()
    acronym.append(first_letter)

acronyms = "".join(acronym)
print(acronyms)


"""Text Triangle Exercise"""

run_num = int(input("Enter a small positive integer: "))
for num in range(run_num + 1):
    print("#" * num)
print()
num = run_num
while num > 0:
    print("#" * num)
    num = num - 1


"""Congress Exercise P137"""

def houseRepresentative(age, citizen_years):
    """Return true if the age is at least 25 and has been citizen for 7 years"""

    return age >= 25 and citizen_years >= 7

def congressSenate(age, citizen_years):
    """Return true if the age is at least 30 and has been citizen for 9 years"""

    return age >= 30 and citizen_years >= 9

def main():
    age = int(input("Enter your age: "))
    years = int(input("The number of years being a citizen here: "))

    if houseRepresentative(age, years) and not congressSenate(age, years):
        print("You are only eligible for the House.")
    elif congressSenate(age, years):
        print("You are eligible for the both House and senate.")
    else:
        print("You are ineligible for Congress")

if __name__ == "__main__":
    main()


"""While loop"""

temparature = 115
while temparature > 112:
    print(temparature)
    temparature = temparature - 1

print("The tea is cold now")


"""While loop test"""

i = 4
while i < 9:
    print(i)
    i = i + 2


"""While loop test 2"""

i = 4
while i < 9:
    i = i + 2
    print(i)


"""Interactive Sum Exercise"""

sum = 0
input_num = int(input("Please enter an integer, the program will ends if you enter 0: "))
while input_num != 0:
    sum += input_num
    input_num = int(input("Please enter an integer, the program will ends if you enter 0: "))

print(sum)


""""""


