from sys import stdin, stdout 
cin = lambda : stdin.readline().strip()
cout = stdout.write 

A, B= map(int, cin().split())
cout(str(A ** B + B ** A))