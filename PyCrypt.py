#imports
import time #for setting delay
import os #for importing pyperclip, if not installed
import string #for encrypting
import base64 #for encrypting

#will try to import pyperclip
try:
    import pyperclip
    
#if pyperclip isn't installed, install it
except ImportError:
    os.system("pip install pyperclip")   
    
    
#Max key size for the Simple Encryptor
MAX_KEY_SIZE = 26

#Greeting Message
print('''
██████╗░██╗░░░██╗  ░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░█████╗░██████╗░
██╔══██╗╚██╗░██╔╝  ██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██████╔╝░╚████╔╝░  ██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║░░██║██████╔╝
██╔═══╝░░░╚██╔╝░░  ██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║░░██║██╔══██╗
██║░░░░░░░░██║░░░  ╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░╚█████╔╝██║░░██║
╚═╝░░░░░░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
''')
#Wait for 0.5 seconds
time.sleep(0.5)



#██████╗░███████╗███████╗██╗███╗░░██╗██╗████████╗██╗░█████╗░███╗░░██╗░██████╗
#██╔══██╗██╔════╝██╔════╝██║████╗░██║██║╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
#██║░░██║█████╗░░█████╗░░██║██╔██╗██║██║░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
#██║░░██║██╔══╝░░██╔══╝░░██║██║╚████║██║░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
#██████╔╝███████╗██║░░░░░██║██║░╚███║██║░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
#╚═════╝░╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░

#Defines what exit_program does
def exit_program():
    print("This program will exit in 5 seconds...") #Tell user that program will exit
    time.sleep(5) #Set delay to exit
    print("Exiting...")
    time.sleep(1)
    exit() #Exit Python program


#Figure out whether user wants to encrypt or decrypt
def getMode():
    while True:
        print('Enter whether you would like to encode or decode a message:')
        mode = input().lower()
        if mode in 'encrypt encode e decrypt decode d'.split():
            return mode
        else:
            time.sleep(0.5)
            print()
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')
            print()
            time.sleep(0.5)

            
#Get user to enter the key number. It will determain the convertion method
def getKey():
    key = 0
    while True:
        print()
        time.sleep(0.25)
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key


#Get user to enter message to be encrypted
def getMessage():
    time.sleep(0.5)
    print()
    print('Enter your message:')
    return input()

#Translate message into the converted message
def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd': #If user wants to decrypt, give them decrypted message
        key = -key
    translated = ''
    
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

#Asks if user wants to copy translated text
def copyTextQ1():
    print()
    ask1 = input("Would you like to copy your text? (y/n): ")
    if ask1 == "y": #If user answers "yes",
        pyperclip.copy(translated_message) #Copy the message
        print()
        print("Your message has been copied!")
        return
    
    else: #Otherwise, return
        return
    
#Asks if user wants to copy translated text
def copyTextQ2():
    ask2 = input("Would you like to copy your text? (y/n): ")
    if ask2 == "y": #If user answers "yes",
        pyperclip.copy(binary_converted) #Copy the message
        print()
        print("Your message has been copied!")
        return
    
    else: #Otherwise, return
        return

#Asks if user wants to copy translated text
def copyTextQ3():
    ask3 = input("Would you like to copy your text? (y/n): ")
    if ask3 == "y": #If user answers "yes",
        pyperclip.copy(base64_result) #Copy the message
        print()
        print("Your message has been copied!")
        return
    
    else: #Otherwise, returm
        return


#░█████╗░██╗░░██╗░█████╗░░█████╗░░██████╗███████╗
#██╔══██╗██║░░██║██╔══██╗██╔══██╗██╔════╝██╔════╝
#██║░░╚═╝███████║██║░░██║██║░░██║╚█████╗░█████╗░░
#██║░░██╗██╔══██║██║░░██║██║░░██║░╚═══██╗██╔══╝░░
#╚█████╔╝██║░░██║╚█████╔╝╚█████╔╝██████╔╝███████╗
#░╚════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═════╝░╚══════╝

#Get user to choose convertion method
print("Here are some different conversion methods:")
time.sleep(0.5)
print('''
1. Simple Encryptor
2. String to binary
3. String to Base64
4. String to Numbers
5. String to ASCII
''')
time.sleep(0.5)

#Asks user what method they want
get_method = int(input("Enter the number corresponding to the conversion method you would like: "))


#███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░  ░░███╗░░
#████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗  ░████║░░
#██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║  ██╔██║░░
#██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║  ╚═╝██║░░
#██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝  ███████╗
#╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░  ╚══════╝

#If you choose 1, execute Simple Encryptor
if get_method == 1:
    print()
    print('''
    
    ░██████╗██╗███╗░░░███╗██████╗░██╗░░░░░███████╗
    ██╔════╝██║████╗░████║██╔══██╗██║░░░░░██╔════╝
    ╚█████╗░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░
    ░╚═══██╗██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░
    ██████╔╝██║██║░╚═╝░██║██║░░░░░███████╗███████╗
    ╚═════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝
    ''')
    time.sleep(0.5)
    mode = getMode()
    message = getMessage()
    key = getKey()
    translated_message = getTranslatedMessage(mode, message, key)


                
    time.sleep(0.5)
    print()
    print('Your translated text is:')
    print(getTranslatedMessage(mode, message, key)) #print the translated msg
    copyTextQ1()
    time.sleep(1)
    print()
    exit_program()


#███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░  ██████╗░
#████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗  ╚════██╗
#██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║  ░░███╔═╝
#██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║  ██╔══╝░░
#██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝  ███████╗
#╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░  ╚══════╝

#If user chooses 2, convert string to bianary
if get_method == 2:
    print()
    print('''
    
    ██████╗░██╗███╗░░██╗░█████╗░██████╗░██╗░░░██╗
    ██╔══██╗██║████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝
    ██████╦╝██║██╔██╗██║███████║██████╔╝░╚████╔╝░
    ██╔══██╗██║██║╚████║██╔══██║██╔══██╗░░╚██╔╝░░
    ██████╦╝██║██║░╚███║██║░░██║██║░░██║░░░██║░░░
    ╚═════╝░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░
    ''')
    string = input("Enter your string to convert into Binary: ")
    binary_converted = ' '.join(format(ord(c), 'b') for c in string)
    print("The Binary Representation is:", binary_converted)
    copyTextQ2()
    time.sleep(1)
    print()
    exit_program()
    
#███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░  ██████╗░
#████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗  ╚════██╗
#██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║  ░█████╔╝
#██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║  ░╚═══██╗
#██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝  ██████╔╝
#╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░  ╚═════╝░

if get_method == 3:
    print()
    print('''

    ██████╗░░█████╗░░██████╗███████╗░█████╗░░░██╗██╗
    ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔═══╝░░██╔╝██║
    ██████╦╝███████║╚█████╗░█████╗░░██████╗░██╔╝░██║
    ██╔══██╗██╔══██║░╚═══██╗██╔══╝░░██╔══██╗███████║
    ██████╦╝██║░░██║██████╔╝███████╗╚█████╔╝╚════██║
    ╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝░╚════╝░░░░░░╚═╝
    ''')
    sample_string = input("Enter your text you would like to convert to Base64: ")
    sample_string_bytes = sample_string.encode("ascii")
  
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    base64_result = (f"{base64_string}")
    print(f"Encoded string: {base64_string}")
    copyTextQ3()
    time.sleep(1)
    print()
    exit_program()

#███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░  ░░██╗██╗
#████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗  ░██╔╝██║
#██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║  ██╔╝░██║
#██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║  ███████║
#██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝  ╚════██║
#╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░  ░░░░░╚═╝

if get_method == 4:
    print()
    print('''

    ███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░░██████╗
    ████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗██╔════╝
    ██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝╚█████╗░
    ██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗░╚═══██╗
    ██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║██████╔╝
    ╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░
    ''')
    text = input("Enter your text to convert into numbers: ")

    # elegant way using list comprehension
    num_list = [ord(x) - 96 for x in text]

    # print the converted letters as numbers in list
    print("Your text to numbers is:", *num_list, sep=' ')
    time.sleep(1)
    print("This text cannot be copied")
    print()
    exit_program()

#███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░  ███████╗
#████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗  ██╔════╝
#██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║  ██████╗░
#██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║  ╚════██╗
#██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝  ██████╔╝
#╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░  ╚═════╝░
    
if get_method == 5:
    print()
    print('''

    ░█████╗░░██████╗░█████╗░██╗██╗
    ██╔══██╗██╔════╝██╔══██╗██║██║
    ███████║╚█████╗░██║░░╚═╝██║██║
    ██╔══██║░╚═══██╗██║░░██╗██║██║
    ██║░░██║██████╔╝╚█████╔╝██║██║
    ╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝╚═╝
    ''')
    gettext = input("Enter your text to convert into ASCII: ")
    ascii_values = []
    for character in gettext:
        ascii_values.append(ord(character))
    print("Your text in ASCII is:", *ascii_values, sep=' ')
    time.sleep(1)
    print("This text cannot be copied")
    print()
    exit_program()
