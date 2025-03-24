import random
import statistics
import sys
import cowsay

number1 = random.choice(["heads", "tails"])



#the other way of the doing it
"""from random import choice
coin = choice(["heads", "tails"])"""

#random number between a and b inclusive
number2 = random.randint(1,10)

cards = ["Car", "House", "Value"]
random.shuffle(cards)

print(statistics.mean([100, 90]))

#sys.
print("hello, my name is", sys.argv[1])

#sys.exit
if len(sys.argv) < 2:
    sys.exit("Too many arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguemnt")
    
print("Hello, my name is", sys.argv[1])

#slice of a list
for arg in sys.argv[1:]:
    print("Hello my name is", arg)
    
if len(sys.argv) == 2:
    cowsay.cow("Hello", sys.argv[1])
    #cowsay.cow("Hello", sys.argv[1])

