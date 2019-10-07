# series-in-matirx
Find the number of series in a given matrix

Given a matix with values 'x' and 'o'; and length of series, find the number of time series occurs in the matrix

e.g. given a matrix:<br>
x x x <br>
x o x<br>
x x x<br>
and series length of 3, the output should be 4 0

Explaination: there are 4 series of x with lenght=3 and there are 0 such series of o

Input should be:
1. Number of test cases t (1 <= t <= 1000 )
2. 3 space seperated numbers representing rows, columns and series lenth (1 <= r,c <= 100 ; 2 <= l <= 10)
3. r lines with c space seperated 'x' or 'o' representing the matrix

e.g. Input:<br>
4<br>
3 3 3<br>
x x x<br>
x o x<br>
x x x<br>
1 1 2<br>
o<br>
2 2 2<br>
x o<br>
o x<br>
4 3 3<br>
x x o<br>
o x o<br>
x o x<br>
o x x<br>

Expected output:<br>
4 0<br>
0 0<br>
1 1<br>
1 1<br>
