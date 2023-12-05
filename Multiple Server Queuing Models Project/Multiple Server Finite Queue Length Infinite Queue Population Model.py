import math
lamda = int(input("Enter the arrival rate of individuals/hour, (λ)  :"))
miu = int(input("Enter the service rate of the system/hour, (μ)  :"))
c = int(input("Enter the Number of servers, (c)  :"))

row = lamda/miu
row_by_c = row/c
sum = 0
l = 7 # value of N
for n in range(0,c):
    f =math.factorial(n)
    a =(row**n)/f
    sum= sum+ a
second = ((row**c)/math.factorial(c))
third = ((1-((row_by_c)**(l-c+1)))/(1-row_by_c))
final = 1/(sum+second*third)

print(f"The probability of no person (P0) {final} or {final*100} % ")

# determining lq
lq_1 = ((row ** (c + 1)) * final) / ((math.factorial(c - 1)))
lq_2 = 1 - ((row_by_c)**(l-c+1)) -((l-c+1)*(1-row_by_c)*((row_by_c)**(l-c)))
lq_3 = (c - row)**2

lq = lq_1*(lq_2/lq_3)
print(f"The length of the queue (Lq) : {lq} ")

# determining lamda_k
p_n =(((row)**l)/((math.factorial(c))*(c**(l-c))))*final
lamda_k = lamda*(1-p_n)
print(f"Effective arrival rate (λ_k) : {lamda_k}")

# determining ls
ls = lq + (lamda_k/miu)
print(f"The length of the system (Ls) : {ls}")

# determining Wq
wq = lq / lamda_k
print(f"The waiting time in the system (Ws) : {wq*60}  minutes")

# determining Ws
ws = ls / lamda_k
print(f"The waiting time in the system (Ws) : {ws*60}  minutes")


