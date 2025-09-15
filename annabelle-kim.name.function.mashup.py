import time 
import random


def reverse(string):
    reversestring = string[::-1]
    print (reversestring)

def vowels(word):
    a_count=0
    e_count=0
    i_count=0
    o_count=0
    u_count=0
    for character in word:
        if character in ["a"]:
            a_count += 1
        if character in ["e"]:
            e_count += 1
        if character in ["i"]:
            i_count += 1
        if character in ["o"]:
            o_count += 1
        if character in ["u"]:
            u_count += 1
    print(f"a = {a_count}")
    print(f"e = {e_count}")
    print(f"i = {i_count}")
    print(f"o = {o_count}")
    print(f"u = {u_count}") 

def consonant(word):
    consonant_count=0
    for character in word:
        if character in ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]:
            consonant_count += 1

def title(word):
    full = str.lower(word)
    split_name = full.split(" ")
    for string in split_name:
        if string in ["dr.", "sir", "esq", "ph.d"]:
            print (True)
            break
        else:
            print (False)
            break


def hyphen(full_name):
    if "-" in full_name:
        print (True)
    else:
        print (False)

def palindrome(full_name):
    if full_name == full_name[::-1]:
        print (True)
    else:
        print (False)

def first (name):
    name_out=""
    for char in name:
        if char == " ":
            break
        else:
            name_out=name_out+char
    return name_out
            
def last(name):
    name_out = ""
    for char in name[::-1]:
        if char ==" ":
            break
        else:
            name_out=name_out+char
    first_name = name_out[::-1]
    return first_name

def lowercase(name):
    name_out = " "
    for letter in name:
        if ord(letter)>64 and ord(letter)<91:
            num = ord(letter)
            num = num+32
            letter = chr(num)
            name_out = name_out + letter
        else:
            name_out = name_out + letter
    return name_out

def uppercase(name):
    name_out = " "
    for letter in name:
        if ord(letter)>96 and ord(letter)<112:
            num = ord(letter)
            num = num-32
            letter = chr(num)
            name_out = name_out + letter
        else:
            name_out = name_out + letter
    return name_out

def uppercase(full_name):
    print(str.upper(full_name))

def main():
    full_name = input("Insert your full name (first middle and last): ")

    while True:
        option = input("""
What would you like to do?

1. Reverse name
2. Count the vowels
3. Count the consonants
4. Convert name to all lowercase
5. Convert name to all uppercase
6. Mix up letters to make a new name
7. Is there a title/distiction
8. Return first name
9. Return last name
10. Is there a hyphen
11. Is name a palindrome
                    
""")
        if option == "1":
            reverse(full_name)
            time.sleep(1)
        elif option == "2":
            vowels(full_name)
            time.sleep(1)
        elif option == "3":
            consonant(full_name)
            time.sleep(1)
        elif option == "4":
            lowercase(full_name)
            time.sleep(1)
        elif option == "5":
            uppercase(full_name)
            time.sleep(1)
        elif option == "7":
            title(full_name)
        elif option == "8":
            first(full_name)
        elif option == "9":
            last(full_name)
        elif option == "10":
            hyphen(full_name)
        elif option == "11":
            palindrome(full_name)
main()