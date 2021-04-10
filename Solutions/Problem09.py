def sortingCriteria(record):
  return record['score']
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # Preparing the list.
        students.append({'name': name, 'score': score})
    
    # Sorting the list depending on score.
    students.sort(key=sortingCriteria)

    # Determining the first index of second lowest score in the list.
    posOfSecondLowest = 1
    while posOfSecondLowest < len(students):
      if students[0]['score'] == students[posOfSecondLowest]['score']:
        posOfSecondLowest = posOfSecondLowest + 1
      else:
        break 

    # Searching for one or more than one lowest score holder.
    secondLowest = []
    secondLowest.append(students[posOfSecondLowest]['name'])
    pos = posOfSecondLowest + 1
    while pos < len(students):
      if students[posOfSecondLowest]['score'] < students[pos]['score']:
        break
      else:
        secondLowest.append(students[pos]['name'])
      pos = pos + 1

    # Sorting the list of second lowest score holder by name
    secondLowest.sort()

    for i in range(len(secondLowest)):
        print(secondLowest[i])
    