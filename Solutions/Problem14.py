def swap_case(s):
    characters = list(s)
    convertedCharacters = []
    convertedStr = ""

    for i in range(len(characters)):
        if characters[i].isupper():
            convertedCharacters.append(characters[i].lower())
        elif characters[i].islower():
            convertedCharacters.append(characters[i].upper())
        else:
            convertedCharacters.append(characters[i])

    return convertedStr.join(convertedCharacters)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)