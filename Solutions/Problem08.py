if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    permutationCollection = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                sum = i+j+k
                if sum != n:
                    oneCombo = "[" + str(i) + ", " + str(j) + ", " + str(k) + "]" 
                    permutationCollection.append(oneCombo)

    length = len(permutationCollection)
    print("[", end="")
    for i in range(length):
        if i == (length-1):
            print(permutationCollection[i], end="")
        elif i == 0:
            print(permutationCollection[i], end=", ")
        else:
            print(permutationCollection[i], end=", ")
    print("]", end="")    