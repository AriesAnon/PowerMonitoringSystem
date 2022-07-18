from tkinter import *

#root widget
root = Tk()
root.title("Add Room")

#Define Functions Here
def addRoomBtn_Click():
    root.destroy()
    #add to database
  
#Create widgets
mainFrame = LabelFrame(root, padx = 20, pady = 10, bg = "#1b1b2f")
mainTitle = Label(mainFrame, text = "ADD ROOM", font = ("Arial", 25), fg = "#e43f5a", bg = "#1b1b2f")

contentFrame = LabelFrame(mainFrame, padx = 20, pady = 10, bg = "#162447") 
roomNameLbl = Label(contentFrame, text = "Room Name: ", fg = "white", bg = "#162447")
roomNameEntry = Entry(contentFrame, width = 20, bg = "#1f4068", fg = "white")
addRoomBtn = Button(contentFrame, text = "Add Room", width = 20, command = addRoomBtn_Click, fg = "white", bg = "#1b1b2f")

#Pack / Display widgets
mainFrame.pack()
mainTitle.pack()

contentFrame.pack()
roomNameLbl.grid(row = 0, column = 0)
roomNameEntry.grid(row = 0, column = 1)
addRoomBtn.grid(row = 1, column = 1)

#end root widget
root.mainloop()