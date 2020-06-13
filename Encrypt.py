"""
This is a text encryption program made by Zhiyang Zuo
How to use:
1. create a .txt file
2. copy and past .txt file location to code
3. copy and past text to .txt file
4. run the method encrypt (A two digit password will be copied to your machine and printed out, memorize it!)
5. encrypted text will be written to your original file
6. to decrypt, run decrypt method with the two digit password
7. decrypted text will be written to your original file
-------------------------------------------------------------------------------------------
----------THIS IS NOT THE SAFEST WAY TO ENCRYPT YOUR TEXT, USE AT YOUR OWN RISK !----------
-----------------------------------------ENJOY!--------------------------------------------
-------------------------------------------------------------------------------------------
"""


import pyperclip
import random
import sys

file_path = "C:\George\PyCharm_Files\Text_Encryption\\text.txt"


def read():
    file = open(file_path, 'r')
    pars = []
    for line in file:
        pars.append(line.strip("\n"))
    file.close()
    return pars


def write(pars):
    file = open(file_path, 'w')
    term = len(pars) - 1
    for i in range(len(pars)):
        file.write(pars[i])
        if i != term:
            file.write("\n")
    file.close()


def get_password():
    i = int(input("Please enter password to decrypt your text: "))
    while i <= 20 or i % 10 == 0 or i >= 100:
        print("Password " + str(
            i) + " does not make sense. It should be a two digit number between 20 and 100 that is not divisible by 10")
        i = get_password()
    return i


def helper(string, i, mode):  # mode=true --> encrypting # mode=false --> decrypting
    result = ''
    row = int(i / 10)
    col = int(i % 10)
    ind = 0
    while ind + row * col < len(string):
        result += fill(i, string[ind:ind + row * col], mode)
        ind += row * col
    result += fill(i, string[ind:len(string)], mode)
    return result


def fill(i, substring, mode):  # mode=true --> encrypting # mode=false --> decrypting
    row = int(i / 10)
    col = int(i % 10)
    arr = [[0 for x in range(col)] for y in range(row)]
    i = 0
    result = ""
    for r in range(len(arr)):  # r = 0-->len(arr)-1
        for c in range(len(arr[r])):  # c = 0-->len(arr[r])-1
            if i >= len(substring):
                arr[r][c] = '*'
            else:
                arr[r][c] = substring[i]
            i = i + 1
    for c in range(len(arr[0])):  # c = 0-->len(arr[0])-1
        for r in range(len(arr)):  # r = 0-->len(arr)
            if mode is False and arr[r][c] == '*':
                pass
            else:
                result += arr[r][c]
    return result


def encrypt():
    pars = read()
    result = []
    i = 0
    while i % 10 == 0:
        i = random.randint(21, 99)
    for string in pars:
        result.append(helper(string, i, True))
    password = (i % 10 * 10) + int(i / 10)
    print("REMEMBER your password is: " + str(password))
    pyperclip.copy(password)
    write(result)


def decrypt():  # this i is reverse of what user inputs
    pars = read()
    result = []
    i = get_password()
    for string in pars:
        result.append(helper(string, i, False))
    write(result)


# ------------------------------------------------------------------------------------------------------------------------------------
# This part of the code is optional. It can be useful if you are planning to create a batch file and run this program on command line.
# ------------------------------------------------------------------------------------------------------------------------------------


if len(sys.argv) < 2:
    print('Usage: py Encrypt.py [keyphrase] - encrypt, decrypt, set, exit')
    sys.argv.append(input("what do you want to do?").lower())
keyphrase = sys.argv[1].lower()  # first command line arg is the keyphrase

while keyphrase not in {'encrypt', 'decrypt', 'exit', 'set'}:
    keyphrase = input(
        'Input ' + keyphrase + ' is incorrect. What do you want to do? (encrypt, decrypt, set, exit): ').lower()

if keyphrase == 'exit':
    sys.exit()
elif keyphrase == 'set':
    file_path = input("what is the new file path? ")
    keyphrase = input("what is your next action? (encrypt, decrypt) ")

if keyphrase == 'encrypt':
    encrypt()
elif keyphrase == 'decrypt':
    decrypt()
else:
    pass
