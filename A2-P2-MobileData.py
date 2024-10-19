#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #:     
#Student Name:  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    print("\nHi, welcome to your data calculator!\n")

    # input usage, if over 1 gb first
    #then elif/and 200-500 & 500-1gb
    usage = float(input("Enter data usage (Mb): "))
    #For furture, if a value is in "" is is a str
    if usage > 1000:
        Total = 118
    elif usage > 200 and ( usage <= 500):
        Total = usage * 0.105
    elif usage > 500 and ( usage <= 1000):
        Total = usage * 0.110
    else:
        Total = 20

    print("\nTotal charge is: ${0:.2f}".format(Total))

    # else is flate rate

    # YOUR CODE ENDS HERE

main()