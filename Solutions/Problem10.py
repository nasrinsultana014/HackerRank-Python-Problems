if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    scoreCard = list(arr)
    scoreCard.sort(reverse=True)

    # Determining the first index of runner up score in the list.
    posOfRunnerupScore = 1
    while posOfRunnerupScore < len(scoreCard):
      if scoreCard[0] == scoreCard[posOfRunnerupScore]:
        posOfRunnerupScore = posOfRunnerupScore + 1
      else:
        break 

    print(scoreCard[posOfRunnerupScore])