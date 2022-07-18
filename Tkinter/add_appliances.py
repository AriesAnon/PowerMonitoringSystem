from tkinter import *

#root widget
root = Tk()
root.title("Add Appliances")

#Define Functions Here
def addAppBtn_Click():
    root.destroy()
    #add to database
  
#Create widgets
mainFrame = LabelFrame(root, padx = 20, pady = 10, bg = "#1b1b2f")
mainTitle = Label(mainFrame, text = "ADD APPLIANCES", font = ("Arial", 25), fg = "#e43f5a", bg = "#1b1b2f")

contentFrame = LabelFrame(mainFrame, padx = 20, pady = 10, bg = "#162447") 
applianceLbl = Label(contentFrame, text = "Appliance Name: ", fg = "white", bg = "#162447")
applianceEntry = Entry(contentFrame, width = 40, bg = "#1f4068", fg = "white")
addAppBtn = Button(contentFrame, text = "Add Appliance", width = 20, command = addAppBtn_Click, fg = "white", bg = "#1b1b2f")

#Pack / Display widgets
mainFrame.pack()
mainTitle.pack()

contentFrame.pack()
applianceLbl.grid(row = 0, column = 0)
applianceEntry.grid(row = 0, column = 1)
addAppBtn.grid(row = 1, column = 1)

#end root widget
root.mainloop()