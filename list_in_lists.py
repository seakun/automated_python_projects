arr = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
for _ in range(int(input())):
    name = input()
    score = float(input())
    arr.append([score, name])

sortedArr = sorted(arr)    
sortedArr.pop(0)
for x in range(len(arr)):
    if arr[x][0] == arr[0][0]:
        print(arr[0][x])
