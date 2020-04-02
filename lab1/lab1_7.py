"""
Write a password generator function in Python. Be creative with how you generate passwords - strong passwords have a mix
of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
every time the user asks for a new password.
"""
import string, random

def printPass(chars):
    password = ""
    for x in range(12):
        password += chars[random.randrange(1,len(chars))]
    return password

def main():
    for x in range(1, 11):
        print ("Password {0:>2d}: {1}".format(x, printPass(string.punctuation + string.ascii_letters + string.digits)))

if __name__ == '__main__':
    main()