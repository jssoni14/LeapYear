def main():
    yearEntered = int(input("Enter a year: ").replace(" ",""))
    
    if(yearEntered % 4 !=0):
        leapstring = "The year " + str(yearEntered) + " is not a leap year"
        print(leapstring)
    elif(yearEntered %100 !=0):
        leapstring = "The year " + str(yearEntered) + " is a leap year"
        print(leapstring)
    elif(yearEntered %400 !=0):
        leapstring = "The year " + str(yearEntered) + " is not a leap year"
        print(leapstring)
    else:
        leapstring = "The year " + str(yearEntered) + " is a leap year"
        print(leapstring)
    
if __name__ == "__main__":
    main()
