def ADF(interest_rate, no_of_periods, payment_amt):
    pv = payment_amt * (1-(1+interest_rate)**(-no_of_periods))/interest_rate
    return pv

def ACF(interest_rate, no_of_periods, payment_amt):
    fv = payment_amt * ((1+interest_rate)**no_of_periods - 1)/interest_rate
    return fv

def Payment(interest_rate, no_of_periods, future_value):
    return future_value/(((1+interest_rate)**no_of_periods - 1)/interest_rate)

def EAR(nominal_ir, periods):
    return (1+nominal_ir/periods)**periods - 1

while(True):
    print("\nEnter choice: ")
    print("1.Present Value of Annuity\n2.Future Value of Annuity\n3.Annuity Payment\n4. Effective Annual Rate\n5.Exit")
    choice = int(input())
    if choice == 1:
        ir = float(input("Enter interest rate: "))
        np = float(input("Enter no of periods: "))
        pmt = float(input("Enter annuity payment: "))
        print("Present Value is: ", ADF(ir,np,pmt))
    elif choice == 2:
        ir = float(input("Enter interest rate: "))
        np = float(input("Enter no of periods: "))
        pmt = float(input("Enter annuity payment: "))
        print("Future Value is: ", ACF(ir,np,pmt))
    elif choice == 3:
        ir = float(input("Enter interest rate: "))
        np = float(input("Enter no of periods: "))
        amt = float(input("Future amount: "))
        print("Annuity Payments: ",Payment(ir,np,amt))
    elif choice == 4:
        n_ir = float(input("Enter nominal interest rate: "))
        periods = int(input("Enter number of times compounded in a year: "))
        print("Effective Annual Interest Rate: ", round(EAR(n_ir, periods) * 100,2))
    else:
        break
