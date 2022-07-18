from tkinter import *
from room_manage import selectedID

#root widget
root = Tk()
root.title("List of Appliances")

#Define Functions Here
def addAppBtn_Click():
    root.destroy()
    import add_appliances
    #add to database and display
  
#Create widgets
mainFrame = LabelFrame(root, padx = 20, pady = 10, bg = "#1b1b2f")
mainTitle = Label(mainFrame, text = "LIST OF APPLIANCES", font = ("Arial", 25), fg = "#e43f5a", bg = "#1b1b2f")

contentFrame = LabelFrame(mainFrame, padx = 20, pady = 10, bg = "#162447") 
deleteLabel = Label(contentFrame, text = selectedID, fg = "white")
'''
appliance1_Lbl = Label(contentFrame, text = "Aircon: ", fg = "white", bg = "#162447")
appliance1_Entry = Entry(contentFrame, width = 30, bg = "#1f4068", fg = "white")
addAppBtn = Button(contentFrame, text = "Add Appliances", width = 15, command = addAppBtn_Click, fg = "white", bg = "#1b1b2f")
'''

#Pack / Display widgets
mainFrame.pack()
mainTitle.pack()

contentFrame.pack()

'''
appliance1_Lbl.grid(row = 1, column = 0)
appliance1_Entry.grid(row = 1, column = 1)
addAppBtn.grid(row = 0, column = 0, pady = 15)
'''

#end root widget
root.mainloop()