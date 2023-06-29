def BD_Construction(MatrixA, District):
    total = 0
    for i in range(len(MatrixA)):
        for j in MatrixA[i]:
            if j == 1:
                total += 1
    if total < 9:
        a={'N': None, 'S': None, 'W': None, 'E': None, 'center': None, 'district': District}
        return a
    elif total >= 9 and total < 15:
        #取極北位置
        countn = 0
        dicn = {}
        for i in range(len(MatrixA)):
            for j in range(len(MatrixA[i])):
                if MatrixA[i][j] == 1:
                    NX = i
                    NY = j
                    countn += 1
                    dicn[countn]=(NX,NY)
        NX,NY=dicn[1]
        #取極南位置
        for i in range(len(MatrixA)):
            for j in range(len(MatrixA[i])):
                if MatrixA[i][j] == 1:
                    SX = i
                    SY = j
        #把MatrixA行列互換
        A = list(map(list,zip(*MatrixA)))
        #取極西位置
        count = 0
        dic = {}
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    WX = j
                    WY = i
                    count += 1
                    dic[count]=(WX,WY)
        WX,WY=dic[1]
        #取極東位置
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    EX = j
                    EY = i
        a={'N': (NX, NY), 'S': (SX, SY), 'W': (WX, WY), 'E': (EX, EY), 'center': None, 'district': District}
        return a
    else:
        #取極北位置
        countn = 0
        dicn = {}
        for i in range(len(MatrixA)):
            for j in range(len(MatrixA[i])):
                if MatrixA[i][j] == 1:
                    NX = i
                    NY = j
                    countn += 1
                    dicn[countn]=(NX,NY)
        NX,NY=dicn[1]
        #取極南位置
        for i in range(len(MatrixA)):
            for j in range(len(MatrixA[i])):
                if MatrixA[i][j] == 1:
                    SX = i
                    SY = j
        #把MatrixA行列互換
        A = list(map(list,zip(*MatrixA)))
        #取極西位置
        count = 0
        dic = {}
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    WX = j
                    WY = i
                    count += 1
                    dic[count]=(WX,WY)
        WX,WY=dic[1]
        #取極東位置
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    EX = j
                    EY = i
        #取center位置(CX, CY)
        CX = (NX+SX)/2
        CY = (WY+EY)/2
        if CX - (NX+SX)//2 > 0:
            CX = (NX+SX)//2+1
        if CY - (WY+EY)//2 > 0:
            CY = (WY+EY)//2+1
        a={'N': (NX, NY), 'S': (SX, SY), 'W': (WX, WY), 'E': (EX, EY), 'center': (CX, CY), 'district': District}
        return a

lst = []
while True:
    n = input()
    if n.isalpha():
        dist = n
        break
    n = [eval(i) for i in n.split()]
    lst.append(n)

total = 0
for i in range(len(lst)):
    for j in lst[i]:
        if j == 1:
            total += 1
#print(total)
a = BD_Construction(lst, dist)

if total < 9:
    print("None")
elif total >= 9 and total < 15:
    print("District-%c\nN(%d,%d)\nS(%d,%d)\nW(%d,%d)\nE(%d,%d)" %(dist,a["N"][0],a["N"][1],a["S"][0],a["S"][1],a["W"][0],a["W"][1],a["E"][0],a["E"][1]))
else:
    print("District-%c\nN(%d,%d)\nS(%d,%d)\nW(%d,%d)\nE(%d,%d)\nCommand center(%.0f,%.0f)" %(dist,a["N"][0],a["N"][1],a["S"][0],a["S"][1],a["W"][0],a["W"][1],a["E"][0],a["E"][1],a["center"][0],a["center"][1]))