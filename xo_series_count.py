t = int(input())
if (t<1 or t>1000): 
    print ("t should be in range: 1 <= t <= 1000")
    exit()
for _ in range(t):
    m, n, k = map(int, input().split())
    if (m<1 or m>100): 
        print ("m should be in range: 1 <= m <= 100")
        exit()
    if (n<1 or n>100): 
        print ("n should be in range: 1 <= n <= 100")
        exit()
    if (k<2 or k>10): 
        print ("k should be in range: 2 <= k <= 10")
        exit()
    mat = []
    for r in range(m):
        _r = []
        _cols = input().split()
        for c in range(len(_cols)):
            _r.append(_cols[c])
        mat.append(_r)
    x_ser = 0
    o_ser = 0
    xArr = list('x' * k)
    oArr = list('o' * k)
    check_diag = False
    if k<=n:
        #check in rows
        for r in range(m):
            for c in range(n-k+1):
                if mat[r][c:c+k] == xArr: x_ser += 1
                if mat[r][c:c+k] == oArr: o_ser += 1
        check_diag = True
    if k<=m:
        #check in cols
        zmat=zip(*mat)
        for c in range(n):
            for r in range(m-k+1):
                if zmat[c][r:r+k] == tuple(xArr): x_ser += 1
                if zmat[c][r:r+k] == tuple(oArr): o_ser += 1
        check_diag = True
    if check_diag:
        #check diags
        for r in range(m):
            row = r
            row2 = m-r-1
            col = 0
            temp = []
            temp2 = []
            while True:
                if row<0 or col>=n or row2>=m:
                    break
                temp.append(mat[row][col])
                temp2.append(mat[row2][col])
                col+=1
                row-=1
                row2+=1
            if len(temp) == k:
                if temp == xArr: x_ser += 1
                if temp == oArr: o_ser += 1
                if temp2 == xArr: x_ser += 1
                if temp2 == oArr: o_ser += 1
            elif len(temp) > k:
                for c in range(len(temp)-k+1):
                    if temp[c:c+k] == xArr: x_ser += 1
                    if temp[c:c+k] == oArr: o_ser += 1
                    if temp2[c:c+k] == xArr: x_ser += 1
                    if temp2[c:c+k] == oArr: o_ser += 1
        for c in range(1,n):
            row = m-1
            col = c
            row2 = 0
            temp = []
            temp2 = []
            while True:
                if row<0 or col>=n or row2>=m:
                    break
                temp.append(mat[row][col])
                temp2.append(mat[row2][col])
                col+=1
                row-=1
                row2+=1
            if len(temp)==k:
                if temp == xArr: x_ser += 1
                if temp == oArr: o_ser += 1
                if temp2 == xArr: x_ser += 1
                if temp2 == oArr: o_ser += 1
            elif len(temp) > k:
                for c in range(len(temp)-k+1):
                    if temp[c:c+k] == xArr: x_ser += 1
                    if temp[c:c+k] == oArr: o_ser += 1
                    if temp2[c:c+k] == xArr: x_ser += 1
                    if temp2[c:c+k] == oArr: o_ser += 1
    print('{} {}'.format(x_ser, o_ser))
