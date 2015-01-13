def flightexpenses():
    print("Hello! Welcome to flightdeals.com, we currently have the following rates for each plane flight: ")
    print("United: 125 per flight ticket, 10 dollars per extra 30 miles from remote location")
    print("Spirit: 200 per flight ticket, 7.5 dollars per extra 30 miles from remote location")
    print("American: 250 per flight ticket, 5.0 dollars per extra 30 miles from destination")
    print("Delta: 350 per flight ticket, standalone in USA")
    

def findflightcost():
    poke = str("yes")
    while poke == "yes":
        flightname = str(input("What is the flight you want to calculate? please use lowercase: "))
        miles = float(input("Using a distance program, how many miles is the flight going to be?: "))
        if flightname == "united":
            flightcost = miles / 30 * 10
            flightcost = flightcost + 125
        if flightname == "spirit":
            flightcost = miles / 30 * 7.5
            flightcost = flightcost + 200
        if flightname == "american":
            flightcost = miles / 30 * 5.0
            flightcost = flightcost + 250
        if flightname == "delta":
            flightcost = 350
        poke = str(input("Would you like to run the script again?: "))
        return(float(flightcost))

        
    
def main():
    flightexpenses()
    functionone = findflightcost()
    cost = functionone.flightcost
    print(cost)

main()
