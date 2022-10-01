from pip import main
print("Input a text to Encrypt/Decrypt: ")
inputString = input()
length=len(inputString)
asciiLetters=[]
rotLetters=[]
for i in inputString:
    asciiLetters.append(ord(i))
for i in range(length):
    if((asciiLetters[i] in range(97,110)) or (asciiLetters[i] in range(65,78))):
        rotLetters.append(asciiLetters[i]+13)
    elif((asciiLetters[i] in range(110,123)) or (asciiLetters[i] in range(78,91))):
        rotLetters.append(asciiLetters[i]-13)
    else:
        rotLetters.append(asciiLetters[i])
print("Result:")
for i in range(0,len(rotLetters)):
    print(chr(rotLetters[i]),end="")