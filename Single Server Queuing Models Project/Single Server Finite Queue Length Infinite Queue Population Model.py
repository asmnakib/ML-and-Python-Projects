lamda = int(input("Enter the arrival rate of individuals/hour, (λ)  :"))
miu = int(input("Enter the service rate of the system/hour, (μ)  :"))
n = int(input("Enter the Maximum No of individuals in the system  :"))

row = lamda/miu

# Determining P0
p_val = (1- row)/(1-(row**(n+1)))

print(f"The probability of no person (P0) {p_val} or {p_val*100} % ")

# Determining Ls
lls1 = (row / ((1 - row) * (1 - (row ** (n + 1)))))
lls2 = 1 + (n * (row ** (n + 1))) - ((n + 1) * (row ** n))

ls = lls1 * lls2
print(f"The length of the system (Ls) : {ls}")

# determining effective arrival rate
p_n = (row ** n) * p_val
p_joining = 1 - p_n

lamda_k = lamda * p_joining

# determining lq
lq = ls-(lamda_k/miu)
print(f"The length of the queue (Lq) : {lq} ")

# determining Wq
wq = lq / lamda_k
print(f"The waiting time in the system (Ws) : {wq} hours or {wq*60}  minutes")

# determining Ws
ws = ls / lamda_k
print(f"The waiting time in the system (Ws) : {ws} hours or {ws*60}  minutes")


