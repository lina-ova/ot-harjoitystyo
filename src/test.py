# Import module 
from tkinter import *
  
# Create object 
root = Tk()
  
# Adjust size 
root.geometry("700x300")
  
# Add image file
bg = PhotoImage(file = "hello.png")
  
# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
  
  
# Create Frame
frame1 = Frame(root)
  
# Add buttons
button1 = Button(frame1,text="Exit")

  
button2 = Button( frame1, text = "Start")

  
button3 = Button( frame1, text = "Reset")

frame1.pack()
  
# Execute tkinter
root.mainloop()