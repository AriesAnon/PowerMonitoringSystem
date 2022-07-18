from tkinter import *

#root widget
root = Tk()
root.title("User Login")

#Define Functions Here
def loginBtn_Click():
    root.destroy()
    import dashboard
  
#Create widgets
mainFrame = LabelFrame(root, padx = 20, pady = 10, bg = "#1b1b2f")
mainTitle = Label(mainFrame, text = "POWER MONITORING SYSTEM", font = ("Arial", 25), fg = "#e43f5a", bg = "#1b1b2f")
subTitle = Label(mainFrame, text = "USER LOGIN", font = ("Arial", 15), fg = "#e43f5a", bg = "#1b1b2f")

contentFrame = LabelFrame(mainFrame, padx = 20, pady = 10, bg = "#162447")
userLbl = Label(contentFrame, text = "Username: ", fg = "white", bg = "#162447")
passLbl = Label(contentFrame, text = "Password: ", fg = "white", bg = "#162447")
userEntry = Entry(contentFrame, width = 50, bg = "#1f4068", fg = "white")
passEntry = Entry(contentFrame, width = 50, bg = "#1f4068", fg = "white")

loginBtn = Button(contentFrame, text = "Login", width = 20, command = loginBtn_Click, fg = "white", bg = "#1b1b2f")
cancelBtn =  Button(contentFrame, text = "Cancel", width = 20, fg = "white", bg = "#1b1b2f")

#Pack / Display widgets
mainFrame.pack()
mainTitle.pack()
subTitle.pack()

contentFrame.pack()
userLbl.grid(row = 0, column = 0)
passLbl.grid(row  = 1, column = 0)
userEntry.grid(row = 0, column = 1, columnspan = 2)
passEntry.grid(row = 1, column = 1, columnspan = 2)

loginBtn.grid(row = 2, column = 1)
cancelBtn.grid(row = 2, column = 2)

#end root widget
root.mainloop()