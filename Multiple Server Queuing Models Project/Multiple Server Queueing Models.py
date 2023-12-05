import math
print("                  Multiple Server Queueing Models ")
print("")
print("")
print("")
print("Options: ")
print("    1. Multiple Server Finite Queue Length Infinite Queue Population Model")
print("    2. Multiple Server Infinite Queue Length Infinite Queue Population Model")
print("    3. Exit")
print("")
print("")
print('''

Model 1:  Multiple Server Finite Queue Length Infinite Queue Population Model

The Inputs for the Model:
        i) The arrival rate of individuals/hour, (λ)
       ii) The service rate of the system/hour, (μ)
      iii) The Number of servers, (c)
       iv) The maximum number that the system will hold, (N)

The Outputs for the Model:
        i) The probability of no person (P0)
       ii) The length of the queue (Lq)	
      iii) The effective arrival rate (λ_k)
       iv) The length of the system (Ls)
        v) The waiting time in the queue (Wq)
       vi) The waiting time in the system (Ws)
        
       
       
Model 2 :Multiple Server Finite Queue Length Infinite Queue Population Model

The Inputs for the Model:
        i) The arrival rate of individuals/hour, (λ)
       ii) The service rate of the system/hour, (μ)
      iii) The Number of servers, (c)
      
The Outputs of the Model:  
        i) The probability of no person (P0)
       ii) The length of the system (Ls)
      iii) The length of the queue (Lq)	
       iv) The waiting time in the queue (Wq)
        v) The waiting time in the system (Ws)
       
        

''')



while(3):
    print("")
    print("")
    choice = int(input("Enter the choice no from the previous options :  "))

    if choice == 1:
        print("         Multiple Server Finite Queue Length Infinite Queue Population Model")


        lamda = int(input("Enter the arrival rate of individuals/hour, (λ)  :"))
        miu = int(input("Enter the service rate of the system/hour, (μ)  :"))
        c = int(input("Enter the Number of servers, (c)  :"))
        l = int(input("Enter the maximum number that the system will hold, (N) :"))

        row = lamda / miu
        row_by_c = row / c
        sum = 0

        for n in range(0, c):
            f = math.factorial(n)
            a = (row ** n) / f
            sum = sum + a
        second = ((row ** c) / math.factorial(c))
        third = ((1 - ((row_by_c) ** (l - c + 1))) / (1 - row_by_c))
        final = 1 / (sum + second * third)
        print(" ")
        print(f"The probability of no person (P0) {final} or {final * 100} % ")

        # determining lq
        lq_1 = ((row ** (c + 1)) * final) / ((math.factorial(c - 1)))
        lq_2 = 1 - ((row_by_c) ** (l - c + 1)) - ((l - c + 1) * (1 - row_by_c) * ((row_by_c) ** (l - c)))
        lq_3 = (c - row) ** 2

        lq = lq_1 * (lq_2 / lq_3)
        print(f"The length of the queue (Lq) : {lq} ")

        # determining lamda_k
        p_n = (((row) ** l) / ((math.factorial(c)) * (c ** (l - c)))) * final
        lamda_k = lamda * (1 - p_n)
        print(f"Effective arrival rate (λ_k) : {lamda_k}")

        # determining ls
        ls = lq + (lamda_k / miu)
        print(f"The length of the system (Ls) : {ls}")

        # determining Wq
        wq = lq / lamda_k
        print(f"The waiting time in the queue (Wq) : {wq * 60}  minutes")

        # determining Ws
        ws = ls / lamda_k
        print(f"The waiting time in the system (Ws) : {ws * 60}  minutes")

    elif choice == 2:
        print("         Multiple Server Infinite Queue Length Infinite Queue Population Model")

        lamda = int(input("Enter the arrival rate of individuals/hour, (λ)  :"))
        miu = int(input("Enter the service rate of the system/hour, (μ)  :"))
        c = int(input("Enter the Number of servers, (c)  :"))

        row = lamda / miu
        row_by_c = row / c
        sum = 0

        for n in range(0, c):
            f = math.factorial(n)
            a = (row ** n) / f
            sum = sum + a
        second = ((row ** c) / math.factorial(c))
        third = (1 / (1 - row_by_c))
        final = 1 / (sum + second * third)
        print(" ")
        print(f"The probability of no person (P0) {final} or {final * 100} % ")

        # determining lq
        lq = ((row ** (c + 1)) * final) / ((math.factorial(c - 1)) * ((c - row) ** 2))
        print(f"The length of the queue (Lq) : {lq} ")

        # determining ls
        ls = lq + row
        print(f"The length of the system (Ls) : {ls}")

        # determining Wq
        wq = lq / lamda
        print(f"The waiting time in the queue (Wq) : {wq * 60}  minutes")

        # determining Ws
        ws = ls / lamda
        print(f"The waiting time in the system (Ws) : {ws * 60}  minutes")

    elif choice == 3:
        print("Thank you")
        break

    else:
        print(" Please enter the right option no")