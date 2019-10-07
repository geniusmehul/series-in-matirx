# series-in-matirx
Find the number of series in a given matrix

Given a matix with values 'x' and 'o'; and length of series, find the number of time series occurs in the matrix

e.g. given a matrix:
x x x
x o x
x x x
and series length of 3, the output should be 4 0

Explaination: there are 4 series of x with lenght=3 and there are 0 such series of o

Input should be:
1. Number of test cases t (1 <= t <= 1000 )
2. 3 space seperated numbers representing rows, columns and series lenth (1 <= r,c <= 100 ; 2 <= l <= 10)
3. r lines with c space seperated 'x' or 'o' representing the matrix

e.g. Input:
4
3 3 3
x x x
x o x
x x x
1 1 2
o
2 2 2
x o
o x
4 3 3
x x o
o x o
x o x
o x x

Expected output:
4 0
0 0
1 1
1 1
