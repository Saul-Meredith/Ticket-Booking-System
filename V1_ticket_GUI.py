"""
This is the general layout of how the design will look for the ticket booking system
07/05/2024
Saul Meredith
V1: The layout
"""

from tkinter import *

root = Tk()

root.title("Ticket Booking")

w1 = Label(root, text="Ticket Booking System", bg= "green", fg="white", 
           font=("Arial", 50))
w1.grid(row = 0)

adult = Button(root, text = "Adult", bg = "black", fg = "white",
               font=("Arial", 30))
adult.grid(row = 1, column = 0)

child = Button(root, text = "Child", bg = "black", fg = "white",
               font=("Arial", 30))
child.grid(row = 2, column = 0)

student_senior = Button(text = "Student/Senior", bg = "black", fg = "white",
               font=("Arial", 30))
student_senior.grid(row = 3, column = 0)

ticket = Entry(root, width= 30, textvariable="Enter ticket amount",
               font= ("Arial", 30))
ticket.grid(row = 2, column = 1)


root.mainloop()