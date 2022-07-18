from tkinter import *

#root widget
root = Tk()
root.title("Ohm's Law Calculator")

#Define Functions Here
def change_dropdown(event):
    if (selection.get() == "Voltage"):
        label_var_1.set("Current")
        label_var_2.set("Resistance")
        finalResult_var.set("")

    elif (selection.get() == "Current"):
        label_var_1.set("Voltage")
        label_var_2.set("Resistance")
        finalResult_var.set("")

    elif (selection.get() == "Resistance"):
        label_var_1.set("Voltage")
        label_var_2.set("Current")
        finalResult_var.set("")

def calculate():
    if (selection.get() == "Voltage"):
       finalResult = int(entry_1.get()) * int(entry_2.get())
       finalResult_var.set(finalResult)

    elif (selection.get() == "Current"):
        finalResult = int(entry_1.get()) / int(entry_2.get())
        finalResult_var.set(finalResult)

    elif (selection.get() == "Resistance"):
        finalResult = int(entry_1.get()) / int(entry_2.get())
        finalResult_var.set(finalResult)

#Initialize Variables Here
options = [
    "Voltage",
    "Current",
    "Resistance"
]

selection = StringVar()
selection.set(options[0])

label_var_1 = StringVar()
label_var_1.set("Current")

label_var_2 = StringVar()
label_var_2.set("Resistance")

finalResult_var = StringVar()

#Create widgets
mainFrame = LabelFrame(root, padx = 20, pady = 10, bg = "#17706e")
mainTitle = Label(mainFrame, text = "OHM'S LAW CALCULATOR", font = ("Arial", 25, "bold"), fg = "#fb7813", bg = "#17706e")

contentFrame = LabelFrame(mainFrame, padx = 20, pady = 10, bg = "#17706e")
instructionLbl = Label(contentFrame, text = "Choose which unit you would like to get the value of.", font = ("Arial", 15), fg = "#f7f7ee", bg = "#17706e")
result_DropdownMenu = OptionMenu(contentFrame, selection, *options, command = change_dropdown)
result_DropdownMenu.config(fg = "#f7f7ee", bg = "#fb7813", font = ("Arial", 13, "bold"))
result_DropdownMenu['menu'].config(bg = "#b6eb7a", font = ("Arial", 10, "bold"))

label_1 = Label(contentFrame, textvariable = label_var_1, fg = "#f7f7ee", bg = "#17706e", font = ("Arial", 13))
entry_1 = Entry(contentFrame, bg = "#b6eb7a", fg = "#17706e", font = ("Arial", 13, "bold"))

label_2 = Label(contentFrame, textvariable = label_var_2, fg = "#f7f7ee", bg = "#17706e", font = ("Arial", 13))
entry_2 = Entry(contentFrame, bg = "#b6eb7a", fg = "#17706e", font = ("Arial", 13, "bold"))

dynamic_result = Label(contentFrame, textvariable = finalResult_var, fg = "#f7f7ee", bg = "#17706e", font = ("Arial", 13, "bold")) 

solveButton = Button(contentFrame, text = "Calculate", command = calculate, fg = "#f7f7ee", bg = "#fb7813", font = ("Arial", 13, "bold"))

#Pack / Display widgets
mainFrame.pack()
mainTitle.pack()

contentFrame.pack()
instructionLbl.grid(row = 0, column = 0, columnspan = 3)

label_1.grid(row = 1, column = 0, sticky = E)
entry_1.grid(row = 1, column = 1)

label_2.grid(row = 2, column = 0, sticky = E)
entry_2.grid(row = 2, column = 1)

result_DropdownMenu.grid(row = 3, column = 0, sticky = E)
dynamic_result.grid(row = 3, column = 1, sticky = W, padx = 15)

solveButton.grid(row = 1, column = 2, rowspan = 2)

#end root widget
root.mainloop()