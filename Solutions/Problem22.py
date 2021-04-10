if __name__ == '__main__':
    params = input()
    paramsInt = params.split(" ")
    
    height, width = int(paramsInt[0]), int(paramsInt[1])

    if width == (height*3):
        # First half
        for i in range(1, height, 2):
          string = []
          for j in range(i):
            string.append(".|.")
          line = "".join(string)
          print(line.center(width, '-'))
        print("WELCOME".center(width, '-'))

        # Second half
        for i in range(height-2, 0, -2):
          string = []
          for j in range(i):
            string.append(".|.")
          line = "".join(string)
          print(line.center(width, '-'))