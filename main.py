#WAP to calculate the scholarship of a candidate.
def f(n):
    if n==entr:
        if n>=0 and n<=30:
            return "Fail-0% Scholarship"
        elif n>=31 and n<=50:
            print("Now, you need to pay",(80/100)*fees,"instead of",fees)
            return "Pass-20% Scholarship"
        elif n>=51 and n<=80:
            print("Now, you need to pay",(70/100)*fees,"instead of",fees)
            return "Pass-30% Scholarship"
        elif n>=81 and n<=100:
            print("Now, you need to pay",(50/100)*fees,"instead of",fees)
            return "Pass-50% Scholarship"

    else:
        if n>=0 and n<=50:
            return "0% Scholarship"
        else:
            print ("Now, you need to pay", (50/ 100) * fees, "instead of", fees)
            return "50% Scholarship"

check=int(input("If you have appeared for entrance, type 1 else type 2: "))
if check==1:
    fees,entr,x,xii=float(input("Enter Total Fees:")),float(input("Enter Entrance Percentage:")),float(input("Enter Xth Percentage:")),float(input("Enter XIIth Percentage:"))
    if entr>x and entr>xii:
        print(f(entr))
    elif x>xii and x>entr:
        print(f(x))
    else:
        print(f(xii))
else:
    print("Apply for the entrance")
