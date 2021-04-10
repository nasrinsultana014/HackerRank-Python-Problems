if __name__ == '__main__':
    s = input()
    characters = list(s)
    statusOne = False
    statusTwo = False 
    statusThree = False
    statusFour = False
    statusFive = False
    for i in range(len(characters)):
        if characters[i].isalnum():
            statusOne = "True"
            break

    for i in range(len(characters)):
        if characters[i].isalpha():
            statusTwo = "True"
            break

    for i in range(len(characters)):
        if characters[i].isdigit():
            statusThree = "True"
            break

    for i in range(len(characters)):
        if characters[i].islower():
            statusFour = "True"
            break

    for i in range(len(characters)):
        if characters[i].isupper():
            statusFive = "True"
            break

    print(statusOne)
    print(statusTwo)
    print(statusThree)
    print(statusFour)
    print(statusFive)