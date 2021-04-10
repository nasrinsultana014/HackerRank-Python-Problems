if __name__ == '__main__':
    n = int(input())
    collection = []
    for i in range(n):
        collection.append(i+1)
        
    length = len(collection)
    for i in range(length):
        print(collection[i], end="")