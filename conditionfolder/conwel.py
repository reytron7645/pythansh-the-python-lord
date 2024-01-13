#Write a program that takes a single character as input and determines whether it is a vowel or a consonant.
letter=input('give an alphabet :')
vowels=['a','e','i','o','u']
if letter in vowels:
    print('it is a vowel')
else:
    print("it is a consonant")