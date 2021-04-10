def parseCommand(line, collection):
  indexOfParamEnd = len(line)
  # print("indexOfParamEnd : ", indexOfParamEnd)

  if line.find("insert") != -1:
    indexOfParamStart = line.index("t")
    # print("indexOfParamStart : ", indexOfParamStart)

    params = line[(indexOfParamStart+1):indexOfParamEnd]
    params = params.strip();
    # print("params :", params)
    
    indexOfComma = params.index(" ")
    pos = params[0:indexOfComma]
    # print("pos : ", pos)

    numberToInsert = params[(indexOfComma+1):(len(params))]
    # print("numberToInsert : ", numberToInsert)

    collection.insert(int(pos),int(numberToInsert))
  
  elif line.find("append") != -1:
    indexOfParamStart = line.index("d")
    # print("indexOfParamStart : ", indexOfParamStart)

    params = line[(indexOfParamStart+1):indexOfParamEnd]
    params = params.strip();
    # print("params :", params)

    collection.append(int(params))
  
  elif line.find("remove") != -1:
    indexOfParamStart = line.index("e ")
    # print("indexOfParamStart : ", indexOfParamStart)

    params = line[(indexOfParamStart+1):indexOfParamEnd]
    params = params.strip();
    # print("params :", params)

    collection.remove(int(params))
  
  elif line.find("reverse") != -1:
    collection.reverse()
   
  elif line.find("sort") != -1:
    collection.sort()

  elif line.find("pop") != -1:
    collection.pop(len(collection)-1)
  elif line.find("print") != -1:
    print(collection)
  
if __name__ == '__main__':
  N = int(input())
  inputedLines = []
  collection=[]
  for l in range(N):
    inputedLines.append(input())
    parseCommand(inputedLines[l], collection)