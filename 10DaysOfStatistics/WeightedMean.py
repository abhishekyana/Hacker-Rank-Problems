# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = list(map(int, input().split(" ")))
W = list(map(int, input().split(" ")))

mw = 0
for a,w in zip(A, W):
    mw+=a*w
print(f"{mw/sum(W):.1f}")
