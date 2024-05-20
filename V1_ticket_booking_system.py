"""
This is the general layout of how the design will look for the ticket booking system
07/05/2024
Saul Meredith
V1: The layout
"""

from tkinter import *

class ticket_booth:
    def __init__(self, adult, child, student_senior):
        self.adult = adult
        self.child = child
        self.student_senior = student_senior
        
    def ticket_total(self):
        total_ticket = self.adult + self.child + self.student_senior
        return total_ticket

    def ticket_price(self):
        total_price = (self.adult * 15) + (self.child * 10) + (self.student_senior * 5)
        return total_price



        

def main():

    all_ticket = ticket_booth(ticket1.get(), ticket2.get(), ticket3.get())

    print(all_ticket.ticket_price)

    total.set(all_ticket.ticket_total())
    cost.set(all_ticket.ticket_price())

    



root = Tk()




root.title("Ticket Booking")




w1 = Label(root, text="Ticket Booking System", bg= "green", fg="white", 
           font=("Arial", 50))
w1.grid(row = 0, column = 0, columnspan = 2, sticky = "WE")

adult = Label(root, text = "Adult", bg = "black", fg = "white",
               font=("Arial", 30), width= 13)
adult.grid(row = 1, column = 0)

ticket1 = IntVar()
ticket1.set("")
adult_ticket = Entry(root, width= 17, textvariable= ticket1,
               font= ("Arial", 30))
adult_ticket.grid(row = 1, column = 1)

# Child entry/label

child = Label(root, text = "Child", bg = "black", fg = "white",
               font=("Arial", 30), width= 13)
child.grid(row = 2, column = 0)

ticket2 = IntVar()
ticket2.set("")
child_ticket = Entry(root, width= 17, textvariable= ticket2,
               font= ("Arial", 30),)
child_ticket.grid(row = 2, column = 1)

# Student Senior Entry/Label

student_senior = Label(text = "Student/Senior", bg = "black", fg = "white",
               font=("Arial", 30), width= 13)
student_senior.grid(row = 3, column = 0)

ticket3 = IntVar()
ticket3.set("")
student_senior_ticket = Entry(root, width= 17, textvariable= ticket3,
               font= ("Arial", 30),)
student_senior_ticket.grid(row = 3, column = 1)

# Confirms the order from customer

confirm = Button(root, text= "CONFIRM", bg = "black", fg = "white",
                 font=("Arial", 30), command = main)
confirm.grid(row = 4, column = 2)

# Total ticket counter

total = IntVar()
total_amount = Label(root, textvariable= total, bg = "black", fg = "white",
               font=("Arial", 30), width= 13)
total_amount.grid(row = 4, column = 0)

# Total price counter
cost = IntVar()
price_total = Label(root, textvariable= cost, bg = "black", fg = "white",
                    font=("Arial", 30), width= 13)
price_total.grid(row = 4, column = 1)

# Tickets left counter

ticket_count = IntVar()
ticket_amount = Label(root, textvariable= ticket_count, bg = "black", fg = "white",
                    font=("Arial", 30), width= 13)



root.mainloop()





 