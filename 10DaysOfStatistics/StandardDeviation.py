# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = list(map(int, input().split(" ")))

m = sum(A)/n

s = []
for i in range(n):
    s.append((A[i]-m)**2)
print(f"{(sum(s)/n)**(1/2):.1f}")
