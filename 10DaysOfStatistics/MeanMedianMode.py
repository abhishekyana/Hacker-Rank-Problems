# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
N = sorted(list(map(int,input().split())))
mean = sum(N)/len(N)
if n%2==0:
    med = (N[n//2] + N[n//2 -1 ])/2
else:
    med = N[n//2 -1 ]
if len(N)==len(set(N)):
    mode = N[0]
else:
    K = Counter(N)
    mode = K.most_common()[0][0]
    #print(K)
print(mean)
print(med)
print(mode)
