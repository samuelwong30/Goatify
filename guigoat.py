# Here's where we put the gui stuff
from tkinter import *

root = Tk()
root.title("Goatify")
root.geometry('400x250')

frame1 = Frame(root)


# Switch Frames
def goto2():
	frame1.grid_forget()
	root.title("Friend")
	frame2.grid()

def goto1():
	frame2.grid_forget()
	root.title("Goatify")
	frame1.grid()



# Display widgets
# ----------------------------------------------------------------
# Frame 1: Search for friend
l1_1 = Label(frame1, text="Welcome!").grid(row=1, column=1)
l2_1 = Label(frame1, text="Enter friends name").grid(row=2, column=1)

e1_1 = Entry(frame1)
e1_1.grid(row=2, column=2)

b1_1 = Button(frame1, text="Search", command=goto2).grid(row=2, column=3)

# Frame 2: Display friend's information
frame2 = Frame(root)
l1_2 = Label(frame2, text="Friend: ").grid(row=1, column=1)
l2_2 = Label(frame2, text="Instagram:").grid(row=2, column=1)
l3_2 = Label(frame2, text="Twitter:").grid(row=3, column=1)
l4_2 = Label(frame2, text="Phone Number:").grid(row=4, column=1)
l5_2 = Label(frame2, text="Email: ").grid(row=5, column=1)
b1_2 = Button(frame2, text="Back to Search", command=goto1).grid(row=5, column=1)





frame1.grid()


root.mainloop()