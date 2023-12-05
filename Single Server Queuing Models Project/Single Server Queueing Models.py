import math
print("                  Single Server Queueing Models ")
print("")
print("")
print("")
print("Options: ")
print("    1. Single Server Finite Queue Length Infinite Queue Population Model")
print("    2. Single Server Infinite Queue Length Infinite Queue Population Model")
print("    3. Exit")
print("")
print("")
print('''

Model 1:  Single Server Finite Queue Length Infinite Queue Population Model

The Inputs for the Model:
        i) The arrival rate of individuals/hour, (λ)
       ii) The service rate of the system/hour, (μ)
      iii) The maximum number that the system will hold, (N)

The Outputs for the Model:
        i) The probability of no person (P0)
       ii) The length of the queue (Lq)	
      iii) The effective arrival rate (λ_k)
       iv) The length of the system (Ls)
        v) The waiting time in the queue (Wq)
       vi) The waiting time in the system (Ws)
        
       
       
Model 2 :Single Server Finite Queue Length Infinite Queue Population Model

The Inputs for the Model:
        i) The arrival rate of individuals/hour, (λ)
       ii) The service rate of the system/hour, (μ)
      
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
        print("         Single Server Finite Queue Length Infinite Queue Population Model")

        lamda = int(input("Enter the arrival rate of individuals/hour, (λ)  :"))
        miu = int(input("Enter the service rate of the system/hour, (μ)  :"))
        n = int(input("Enter the Maximum No of individuals in the system  :"))

        row = lamda / miu

        # Determining P0
        p_val = (1 - row) / (1 - (row ** (n + 1)))

        print(f"The probability of no person (P0) {p_val} or {p_val * 100} % ")

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
        lq = ls - (lamda_k / miu)
        print(f"The length of the queue (Lq) : {lq} ")

        # determining Wq
        wq = lq / lamda_k
        print(f"The waiting time in the system (Ws) : {wq} hours or {wq * 60}  minutes")

        # determining Ws
        ws = ls / lamda_k
        print(f"The waiting time in the system (Ws) : {ws} hours or {ws * 60}  minutes")




    elif choice == 2:
        print("         Single Server Infinite Queue Length Infinite Queue Population Model")


        lamda = int(input("Enter the arrival rate of individuals/hour, (λ)  :"))
        miu = int(input("Enter the service rate of the system/hour, (μ)  :"))

        row = lamda / miu

        # Determining P0
        p_val = 1 - row

        print(f"The probability of no person (P0) {p_val} or {p_val * 100} % ")

        # Determining Ls
        ls = (row / (1 - row))
        print(f"The length of the system (Ls) : {ls}")

        # determining lq
        lq = ls - row
        print(f"The length of the queue (Lq) : {lq} ")

        # determining Wq
        wq = lq / lamda
        print(f"The waiting time in the system (Ws) : {wq} hours or {wq * 60}  minutes")

        # determining Ws
        ws = ls / lamda
        print(f"The waiting time in the system (Ws) : {ws} hours or {ws * 60}  minutes")




    elif choice == 3:
        print("Thank you")
        break

    else:
        print(" Please enter the right option no")