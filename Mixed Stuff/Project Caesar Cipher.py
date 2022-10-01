'''

implement helper function encrypt_char(char,key) to encrypt a single character, char, with key.
implement encrypt_message (message,key), it should use the helper function.
Implement decrypt function

'''

message=[]

def encrypt_char(char, key):
    for i in char:
        message.append(ord(i)+key)
    return message


def encrypt_message(char, key):
    message = encrypt_char(char,key)
    message = [chr(x) for x in message]
    for x in range(len(message)):
        if message[x] == "#":
            message[x] = " "
    encrypted_message = "".join(message)
    return encrypted_message


def decrypt_message(message, key):
    decrypted_message = []
    for i in message:
        decrypted_message.append(chr(i - key))
        for x in message:
            if x == "#":
                x.replace("#", "")
    return "".join(decrypted_message)


if __name__ == '__main__':
    try:
        char = input("Bitte einen Satz eingeben: ")
        key = int(input("Bitte eine Zahl eingeben: "))
        print(encrypt_message(char, key))
        print(decrypt_message(message, key))
    except ValueError:
        print("First Input has to be a string, Second Input has to be a Number")
