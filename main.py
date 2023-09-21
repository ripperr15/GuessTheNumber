import random
import time

print("Hello again, Welcome to the guessing game, Gonna pick a number b/w 1 to 100  ")
time.sleep(2)
print("Hold on bruh, gimme a minute!")
time.sleep(2)

guess = int(input("Go ahead guess the num:  "))
corr_num = random.randint(1,100)
guess_count = 1

while guess != corr_num:
  guess_count += 1
  if guess < corr_num:
    
    guess = int(input("wrong go a bit higher mate, Guess the num again :  "))
  else:
    guess = int(input("wrong go a bit lower mate, Guess the num again:  "))

    
print(f"correct ans bruh {corr_num} took you {guess_count} tries tho!!")