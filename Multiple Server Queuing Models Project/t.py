import math
lamda = int(input("Enter the arrival rate of individuals/hour, (λ)  :"))
miu = int(input("Enter the service rate of the system/hour, (μ)  :"))

row = lamda/miu

# Determining P0
p_val = 1- row

print(f"The probability of no person (P0) {p_val} or {p_val*100} % ")

# Determining Ls
ls = (row/(1-row))
print(f"The length of the system (Ls) : {ls}  or {round(ls,2)}")

# determining lq
lq = ls - row
print(f"The length of the queue (Lq) : {lq} or {round(lq,2)} ")

# determining Wq
wq = lq / lamda
print(f"The waiting time in the system (Ws) : {round(wq,2)} hours or {wq*60}  minutes")

# determining Ws
ws = ls / lamda
print(f"The waiting time in the system (Ws) : {round(ws,2)} hours or {ws*60}  minutes")


