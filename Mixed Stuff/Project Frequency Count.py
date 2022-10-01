'''

Prompt the user for a line of text
Use a dictionary to make frequency count of the letters
print the frequencies

'''


count = {}

def freq_count():
    try:
        text = input("Please give me a line of text: ")
        for letter in text:
            letter = letter.lower()
            if letter == " ":
                continue
            count[letter] = count.get(letter, 0) + 1
        for key, value in count.items():
            print(f"{key}: {value}")
    except:
        print("Letters only! ")



if __name__ == '__main__':
    freq_count()