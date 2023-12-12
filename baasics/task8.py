def make_rug(m, n, proc):
    return [proc * n for _ in range(m)]
m=int(input("Enter your input: "))
n=int(input("Enter your input: "))
proc=input()
print(make_rug(m,n,proc))