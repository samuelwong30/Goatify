# Here's where we put the gui stuff
from tkinter import *

root = Tk()
root.title("Goatify")
root.geometry('400x250')

frame1 = Frame(root)


# Switch Frames
# Frame 1 Buttons
def from1goto2():
	frame1.grid_forget()
	root.title("Friend")
	# Get info

	frame2.grid()

def from1goto3():
	frame1.grid_forget()
	root.title("Add Friend")
	frame3.grid()

# Frame 2 Buttons
def from2goto1():
	frame2.grid_forget()
	root.title("Goatify")
	frame1.grid()

# Frame 3 Buttons
def from3goto1():
	frame3.grid_forget()
	root.title("Goatify")
	frame1.grid()

def from3add():
	frame3.grid_forget()
	root.title("Goatify")
	# Write to file
	frame1.grid()



# Display widgets
# ----------------------------------------------------------------
# Frame 1: Search for friend
l1_1 = Label(frame1, text="Welcome!").grid(row=1, column=1)
l2_1 = Label(frame1, text="Enter friends name").grid(row=2, column=1)

e1_1 = Entry(frame1)
e1_1.grid(row=2, column=2)

b1_1 = Button(frame1, text="Search", command=from1goto2).grid(row=2, column=3)
b1_2 = Button(frame1, text="Add a friend", command=from1goto3).grid(row=3, column=2)

# Frame 2: Display friend's information
frame2 = Frame(root)
l1_2 = Label(frame2, text="Friend: ").grid(row=1, column=1)
l2_2 = Label(frame2, text="Instagram:").grid(row=2, column=1)
l3_2 = Label(frame2, text="Twitter:").grid(row=3, column=1)
l4_2 = Label(frame2, text="Phone Number:").grid(row=4, column=1)
l5_2 = Label(frame2, text="Email: ").grid(row=5, column=1)

b1_2 = Button(frame2, text="Back to Search", command=from2goto1).grid(row=5, column=1)

# Frame 3: Add a friend
frame3 = Frame(root)
l1_3 = Label(frame3, text="Friend information").grid(row=1, column=1)
l1_3 = Label(frame3, text="Enter name:").grid(row=2, column=1)
l2_3 = Label(frame3, text="Enter instagram:").grid(row=3, column=1)
l3_3 = Label(frame3, text="Enter twitter").grid(row=4, column=1)
l4_3 = Label(frame3, text="Enter phone number").grid(row=5, column=1)
l5_3 = Label(frame3, text="Enter email:").grid(row=6, column=1)

e1_3 = Entry(frame3)
e1_3.grid(row=2, column=2)
e2_3 = Entry(frame3)
e2_3.grid(row=3, column=2)
e3_3 = Entry(frame3)
e3_3.grid(row=4, column=2)
e4_3 = Entry(frame3)
e4_3.grid(row=5, column=2)
e5_3 = Entry(frame3)
e5_3.grid(row=6, column=2)

b1_3 = Button(frame3, text="Back to Menu", command=from3goto1).grid(row=7, column=1)
b1_3 = Button(frame3, text="Add Friend", command=from3add).grid(row=7, column=2)









frame1.grid()


root.mainloop()