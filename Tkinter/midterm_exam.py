from tkinter import *

#root widget
root = Tk()
root.title("Simple Point of Sale System")

#Define Functions Here
def calculate():
    #calculate total
    total_item_1 = int(price_entry_1.get()) * int(quantity_entry_1.get())
    total_var_1.set(total_item_1)

    total_item_2 = int(price_entry_2.get()) * int(quantity_entry_2.get())
    total_var_2.set(total_item_2)

    finalTotal = total_item_1 + total_item_2
    finalTotal_var.set(finalTotal)

    #set variables from entries
    productName_var_1.set(productName_entry_1.get())
    productName_var_2.set(productName_entry_2.get())

    price_var_1.set(price_entry_1.get())
    price_var_2.set(price_entry_2.get())

    quantity_var_1.set(quantity_entry_1.get())
    quantity_var_2.set(quantity_entry_2.get())

    #create new window for receipt
    receipt = Toplevel()
    receipt.title("Receipt for POS")
    receipt.config(bg = "#faf3f3")
    mainTitle = Label(receipt, text = "SIMPLE POINT OF SALE SYSTEM", font = ("Arial", 25, "bold"), fg = "#da7f8f", bg = "#faf3f3")
    
    productName_Lbl = Label(receipt, text = "Product Name", font = ("Arial", 15, "bold"), fg = "#da7f8f", bg = "#faf3f3")
    price_Lbl = Label(receipt, text = "Price", font = ("Arial", 15, "bold"), fg = "#da7f8f", bg = "#faf3f3")
    quantity_Lbl = Label(receipt, text = "Quantity", font = ("Arial", 15, "bold"), fg = "#da7f8f", bg = "#faf3f3")
    total_Lbl = Label(receipt, text = "Total", font = ("Arial", 15, "bold"), fg = "#da7f8f", bg = "#faf3f3")

    productName_label_1 = Label(receipt, textvariable = productName_var_1, font = ("Arial", 13, "bold"), fg = "#205778", bg = "#faf3f3")
    productName_label_2 = Label(receipt, textvariable = productName_var_2, font = ("Arial", 13, "bold"), fg = "#205778", bg = "#faf3f3")

    price_label_1 = Label(receipt, textvariable = price_var_1, font = ("Arial", 13, "bold"), fg = "#205778", bg = "#faf3f3")
    price_label_2 = Label(receipt, textvariable = price_var_2, font = ("Arial", 13, "bold"), fg = "#205778", bg = "#faf3f3")

    quantity_label_1 = Label(receipt, textvariable = quantity_var_1, font = ("Arial", 13, "bold"), fg = "#205778", bg = "#faf3f3")
    quantity_label_2 = Label(receipt, textvariable = quantity_var_2, font = ("Arial", 13, "bold"), fg = "#205778", bg = "#faf3f3")

    total_item_label_1 = Label(receipt, textvariable = total_var_1, font = ("Arial", 13, "bold"), fg = "#205778", bg = "#faf3f3")
    total_item_label_2 = Label(receipt, textvariable = total_var_2, font = ("Arial", 13, "bold"), fg = "#205778", bg = "#faf3f3")

    grandTotal_Lbl = Label(receipt, text = "Grand Total:", font = ("Arial", 15, "bold"), fg = "#da7f8f", bg = "#faf3f3")
    finalTotal_label = Label(receipt, textvariable = finalTotal_var, font = ("Arial", 13, "bold"), fg = "#205778", bg = "#faf3f3")

    #display widgets
    mainTitle.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 5)
    
    productName_Lbl.grid(row = 1, column = 0, pady = 5)
    price_Lbl.grid(row = 1, column = 1, pady = 5)
    quantity_Lbl.grid(row = 1, column = 2, pady = 5)
    total_Lbl.grid(row = 1, column = 3, pady = 5)

    productName_label_1.grid(row = 2, column = 0, pady = 5)
    price_label_1.grid(row = 2, column = 1, pady = 5)
    quantity_label_1.grid(row = 2, column = 2, pady = 5)
    total_item_label_1.grid(row = 2, column = 3, pady = 5)

    productName_label_2.grid(row = 3, column = 0, pady = 5)
    price_label_2.grid(row = 3, column = 1, pady = 5)
    quantity_label_2.grid(row = 3, column = 2, pady = 5)
    total_item_label_2.grid(row = 3, column = 3, pady = 5)

    grandTotal_Lbl.grid(row = 4, column = 2, pady = 10)
    finalTotal_label.grid(row = 4, column = 3, pady = 10)

def clear_entries():
    productName_entry_1.delete(0, END)
    productName_entry_1.insert(0, "")
    
    productName_entry_2.delete(0, END)
    productName_entry_2.insert(0, "")
    
    price_entry_1.delete(0, END)
    price_entry_1.insert(0, "")

    price_entry_2.delete(0, END)
    price_entry_2.insert(0, "")

    quantity_entry_1.delete(0, END)
    quantity_entry_1.insert(0, "")

    quantity_entry_2.delete(0, END)
    quantity_entry_2.insert(0, "")

    productName_entry_1.focus()
    
#Initialize Variables Here
productName_var_1 = StringVar()
productName_var_2 = StringVar()

price_var_1 = StringVar()
price_var_2 = StringVar()

quantity_var_1 = StringVar()
quantity_var_2 = StringVar()

total_var_1 = StringVar()
total_var_2 = StringVar()
finalTotal_var = StringVar()

#Create widgets
mainFrame = LabelFrame(root, padx = 20, pady = 10, bg = "#faf3f3")
mainTitle = Label(mainFrame, text = "SIMPLE POINT OF SALE SYSTEM", font = ("Arial", 25, "bold"), fg = "#da7f8f", bg = "#faf3f3")

contentFrame = LabelFrame(mainFrame, padx = 20, pady = 10, bg = "#e1e5ea")
productName_Lbl = Label(contentFrame, text = "Product Name", font = ("Arial", 13, "bold"), fg = "#da7f8f", bg = "#e1e5ea")
price_Lbl = Label(contentFrame, text = "Price", font = ("Arial", 13, "bold"), fg = "#da7f8f", bg = "#e1e5ea")
quantity_Lbl = Label(contentFrame, text = "Quantity", font = ("Arial", 13, "bold"), fg = "#da7f8f", bg = "#e1e5ea")

productName_entry_1 = Entry(contentFrame, font = ("Arial", 13, "bold"), bg = "#a7bbc7", fg = "#faf3f3")
productName_entry_2 = Entry(contentFrame, font = ("Arial", 13, "bold"), bg = "#a7bbc7", fg = "#faf3f3")
price_entry_1 = Entry(contentFrame, font = ("Arial", 13, "bold"), bg = "#a7bbc7", fg = "#faf3f3")
price_entry_2 = Entry(contentFrame, font = ("Arial", 13, "bold"), bg = "#a7bbc7", fg = "#faf3f3")
quantity_entry_1 = Entry(contentFrame, font = ("Arial", 13, "bold"), bg = "#a7bbc7", fg = "#faf3f3")
quantity_entry_2 = Entry(contentFrame, font = ("Arial", 13, "bold"), bg = "#a7bbc7", fg = "#faf3f3")

calculateButton = Button(contentFrame, text = "Calculate", font = ("Arial", 15, "bold"), command = calculate, bg = "#da7f8f", fg = "#faf3f3")
clearButton = Button(contentFrame, text = "Clear Entries", font = ("Arial", 15, "bold"), command = clear_entries, bg = "#da7f8f", fg = "#faf3f3")

#Pack / Display widgets
mainFrame.pack()
mainTitle.pack()

contentFrame.pack()
productName_Lbl.grid(row = 0, column = 0)
price_Lbl.grid(row = 0, column = 1)
quantity_Lbl.grid(row = 0, column = 2)

productName_entry_1.grid(row = 1, column = 0, padx = 10, pady = 10)
price_entry_1.grid(row = 1, column = 1, padx = 10, pady = 10)
quantity_entry_1.grid(row = 1, column = 2, padx = 10, pady = 10)

productName_entry_2.grid(row = 2, column = 0, padx = 10, pady = 10)
price_entry_2.grid(row = 2, column = 1, padx = 10, pady = 10)
quantity_entry_2.grid(row = 2, column = 2, padx = 10, pady = 10)

calculateButton.grid(row = 3, column = 1)
clearButton.grid(row = 3, column = 2)
#end root widget
root.mainloop()