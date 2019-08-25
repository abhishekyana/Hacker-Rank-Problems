# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
A = sorted(list(map(int, input().split(" "))))
# print(A)
if n%2==0:
    med = (A[(n//2)-1] + A[n//2])/2
    ns = n//2
    Al = A[:(n//2)]
    Au = A[(n//2):]
    if ns%2==0:
        Q1 = (Al[(ns//2)-1] + Al[ns//2])/2
        Q2 = (Au[(ns//2)-1] + Au[ns//2])/2
    else:
        Q1 = Al[(ns//2)]
        Q2 = Au[(ns//2)]
else:
    med = A[n//2]
    ns = n//2
    Al = A[:ns]
    Au = A[ns+1:]
    if ns%2==0:
        Q1 = (Al[(ns//2)-1] + Al[ns//2])/2
        Q2 = (Au[(ns//2)-1] + Au[ns//2])/2
    else:
        Q1 = Al[(ns//2)]
        Q2 = Au[(ns//2)]

if Q1==int(Q1):
    Q1 = int(Q1)
if Q2==int(Q2):
    Q2 = int(Q2)
if med==int(med):
    med = int(med)
# print(Al, Au)
print(Q1)
print(med)
print(Q2)
