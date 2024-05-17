"""
This is the main code of the ticket booking system
12/05/2024
Saul Meredith
V1: Working code, doesnt count for too many tickets
"""

class ticket_booth: # Gets the amount of tickets for 
    def __init__(self, adult, child, student_senior):
        self.adult = adult
        self.child = child
        self.student_senior = student_senior

    def calculate(self):
        total = (self.adult * 15) + (self.child * 5) + (self.student_senior * 10)
        return total
    
    def __str__(self):
        print(price)
        


ticket_option = {"adult" : 15,
                 "child" : 10,
                 "student senior" : 5}

amount = []


for option, price in ticket_option.items(): # Gets the amount of tickets for every type
    ticket = amount.append(int(input(f"Enter number of {option.title()} tickets: ${price} ")))

price = ticket_booth(amount[0], amount[1], amount[2])

print(f"The total amount for the tickets is ${price.calculate():.2f}")



 