#HR Calculator
x=0
y=[] 

def main():
        
    HR=191.5
    Heartrate=float(HR)
    A=input("Enter your age: ") 
    Age=float(A)
    

    HRI=Heartrate-(0.007*Age*Age)

       
    print("Your HR is", HRI)
    if HRI<160:
        print("You must take care more.")
    elif HRI>180:
        print("You should exercise more.")
    else:
        print("It indicates you are within normal bounds")

    y.append(HRI)

while x==0:
    main()
    again=input("Try again? y/n:" )
    if x=="y":
        print("")
        main()
    if again !="y":
        print("Your Max Heart rate value was:", max(y))
    



    

    
    

