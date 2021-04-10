def count_substring(string, sub_string):
    lengthSubstring = len(sub_string)
    lengthString = len(string)
    count = 0
    for i in range(lengthString - lengthSubstring + 1):
        if sub_string == string[i:i+lengthSubstring]:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)