import math
lamda = int(input("Enter the arrival rate of individuals/hour, (λ)  :"))
miu = int(input("Enter the service rate of the system/hour, (μ)  :"))
c = int(input("Enter the Number of servers, (c)  :"))

row = lamda/miu
row_by_c = row/c
sum = 0

for n in range(0,c):
    f =math.factorial(n)
    a =(row**n)/f
    sum= sum+ a
second = ((row**c)/math.factorial(c))
third = (1/(1-row_by_c))
final = 1/(sum+second*third)

print(f"The probability of no person (P0) {final} or {final*100} % ")

# determining lq
lq = ((row ** (c + 1)) * final) / ((math.factorial(c - 1)) * ((c - row) ** 2))
print(f"The length of the queue (Lq) : {lq} ")

# determining ls
ls = lq + row
print(f"The length of the system (Ls) : {ls}")

# determining Wq
wq = lq / lamda
print(f"The waiting time in the system (Ws) : {wq*60}  minutes")

# determining Ws
ws = ls / lamda
print(f"The waiting time in the system (Ws) : {ws*60}  minutes")


