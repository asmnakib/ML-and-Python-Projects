import math
lamda = int(input("Enter the arrival rate of individuals/hour, (λ)  :"))
miu = int(input("Enter the service rate of the system/hour, (μ)  :"))

row = lamda/miu

# Determining P0
p_val = 1- row

print(f"The probability of no person (P0) {p_val} or {p_val*100} % ")

# Determining Ls
ls = (row/(1-row))
print(f"The length of the system (Ls) : {ls}")

# determining lq
lq = ls - row
print(f"The length of the queue (Lq) : {lq} ")

# determining Wq
wq = lq / lamda
print(f"The waiting time in the system (Ws) : {wq} hours or {wq*60}  minutes")

# determining Ws
ws = ls / lamda
print(f"The waiting time in the system (Ws) : {ws} hours or {ws*60}  minutes")


