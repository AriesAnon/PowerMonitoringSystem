from tkinter import *

#root widget
root = Tk()
root.title("Dashboard")

#Define Functions Here
def roomMngBtn_Click():
    root.destroy()
    import room_manage
  
#Create widgets
mainFrame = LabelFrame(root, padx = 20, pady = 10, bg = "#1b1b2f")
mainTitle = Label(mainFrame, text = "DASHBOARD", font = ("Arial", 25), fg = "#e43f5a", bg = "#1b1b2f")

contentFrame = LabelFrame(mainFrame, padx = 20, pady = 10, bg = "#162447") 
roomMngBtn = Button(contentFrame, text = "Room Management", width = 20, command = roomMngBtn_Click, fg = "white", bg = "#1b1b2f")

#Pack / Display widgets
mainFrame.pack()
mainTitle.pack()

contentFrame.pack()
roomMngBtn.pack()

#end root widget
root.mainloop()