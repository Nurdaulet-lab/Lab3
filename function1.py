
#Example 4

from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [n for n in numbers if is_prime(n)]

numbers = list(map(int, input().split()))
print(filter_prime(numbers))

# Example 5
from itertools import permutations

def print_permutations(s):
    for perm in permutations(s):
        print("".join(perm))

string = input("Enter a string: ")
print_permutations(string)

#Example 6
def sozder(nou):
    for i in range(len(words)-1,-1,-1):
        print(words[i],end=" ")

words=list(input().split())
sozder(words)
# example 7
def has_33(nums):
    for i in range(1,len(nums)):
        if nums[i-1]==3 and nums[i]==3:
            return True
    return False
sandar=list(map(int,input().split()))
print(has_33(sandar))
# example 8
def spy_game(nums):
    for i in range(1,len(nums)):
        if nums[i-1]==0 and nums[i]==0 and nums[i+1]==7:
            return True
    return False
sandar=list(map(int,input().split()))
print(spy_game(sandar))

# example 9
from math import pi

def volume(nums):
    return pi*nums**3*(4/3)
radius=int(input())
print(volume(radius))
# example 10
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:  
            unique_lst.append(item)  
    return unique_lst

nomer=list(map(int,input().split()))
print(unique_elements(nomer))
 # example 11
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
word_or_phrase = input()
if is_palindrome(word_or_phrase):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
    # example 12
    def histogram(lst):
          for value in lst:
            print('*' * value)
nomer=list(map(int,input().split()))
histogram(nomer())
       #example 13 
       import random

def guess_the_number():
    
    number_to_guess = random.randint(1, 20)
    name = input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    guesses_taken = 0
    while True:
        guess = int(input("Take a guess.\n"))
        guesses_taken += 1
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
guess_the_number()
     
          #example 14
          def histogram(lst):
    for value in lst:
        print('*' * value)
histogram([4, 9, 7])













