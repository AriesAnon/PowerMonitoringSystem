from re import search
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

#connection to the database

db_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "power_monitoring_system"
)

#create database cursor for performing SQL operations
db_cursor = db_connection.cursor()

#root widget
root = Tk()
root.title("Room Management")

#Define Functions Here
def addAppliances():
    recordSelection()
    
    #create new window for appliances
    appliances = Toplevel()
    appliances.title("Manage Appliances")
    appliances.config(bg = "#162447")

    #functions inside appliances window
    def addData_Appliances():
        insert_cmd = "INSERT INTO appliances_management (applianceName, applianceRating, roomID) VALUES (%s, %s, %s);"
        get_appName = add_applianceName_Entry.get()
        get_appRating = add_applianceRating_Entry.get()

        if (get_appName != "" and get_appRating != ""):
            value = (get_appName, get_appRating, selectedID)
            db_cursor.execute(insert_cmd, value)
            db_connection.commit()
            messagebox.showinfo("Information","Appliances added into the database.")
            appliances.lift()
            add_applianceName_Entry.delete(0, END)
            add_applianceRating_Entry.delete(0, END)
            readData_Appliances()
            
        else:
            messagebox.showinfo("Information","Blank field/s detected. Please fill up all fields.")
            appliances.lift()

    def searchData_Appliances():
        search_applianceID = search_applianceID_Entry.get()
        select_cmd = "SELECT * from appliances_management WHERE applianceID = '%s' AND roomID = '%s'" %(search_applianceID, selectedID)
        db_cursor.execute(select_cmd)
        data = db_cursor.fetchall()
        
        applianceID = ""
        applianceName = ""
        applianceRating = ""

        for record in appliances_tree.get_children():
            appliances_tree.delete(record)

        for x in data:
            applianceID = x[0]
            applianceName = x[1]
            applianceRating = x[2]
            appliances_tree.insert(parent = '', index = 'end', values = (applianceID, applianceName, applianceRating), tags = ('evenrow'))
        
        search_applianceID_Entry.delete(0, END)

    def updateData_Appliances():
        appID = search_applianceID_Entry.get()
        appName = add_applianceName_Entry.get()
        appRating = add_applianceRating_Entry.get()

        update_cmd = "UPDATE appliances_management SET applianceName = '%s', applianceRating = '%s' WHERE roomID = '%s' AND applianceID = '%s'" %(appName, appRating, selectedID, appID)
            
        if (appName != "" and appRating != "" and appID != ""):
            db_cursor.execute(update_cmd)
            db_connection.commit()
            messagebox.showinfo("Information", "Appliance updated.")
            appliances.lift()
            readData_Appliances()
                
            search_applianceID_Entry.delete(0, END)
            add_applianceName_Entry.delete(0, END)
            add_applianceRating_Entry.delete(0, END)

        else:
            messagebox.showinfo("Information", "Blank field/s detected. Please fill up all fields.")    
            appliances.lift()
    
    def deleteData_Appliances():
        appID = search_applianceID_Entry.get()
        delete_cmd = "DELETE FROM appliances_management WHERE roomID = '%s' AND applianceID = '%s'" % (selectedID, appID)

        if (appID != ""):
            db_cursor.execute(delete_cmd)
            db_connection.commit()
            messagebox.showinfo("Information", "Appliance deleted.")
            appliances.lift()
            search_applianceID_Entry.delete(0, END)
            readData_Appliances()
        
        else:
            messagebox.showinfo("Information", "Blank field/s detected. Please fill up all fields.")
            appliances.lift()

    def readData_Appliances():
        select_cmd = "SELECT * from appliances_management where roomID = " + selectedID
        db_cursor.execute(select_cmd)
        data = db_cursor.fetchall()

        appID = ""
        appName = ""
        appRating = ""

        for record in appliances_tree.get_children():
            appliances_tree.delete(record)

        count = 0

        for x in data:
            appID = x[0]
            appName = x[1]
            appRating = x[2]

            if count % 2 == 0:
                appliances_tree.insert(parent = '', index = 'end', values = (appID, appName, appRating), tags = ('evenrow'))
            
            else:
                appliances_tree.insert(parent = '', index = 'end', values = (appID, appName, appRating), tags = ('oddrow'))
            
            count += 1

            
        

    title = "List of Appliances in the " + selectedRoom
    toplevelTitle = Label(appliances, text = title, font = ("Arial", 25), fg = "#e43f5a", bg = "#162447")
    
    #create treeview
    appliances_tree = ttk.Treeview(appliances)
    appliances_tree['columns'] = ("Appliance ID", "Appliance Name", "Appliance Rating")

    #format columns
    appliances_tree.column("#0", width = 0, stretch = NO)
    appliances_tree.column("Appliance ID", width = 100, minwidth = 50, anchor = CENTER)
    appliances_tree.column("Appliance Name", width = 150, minwidth = 100, anchor = W)
    appliances_tree.column("Appliance Rating", width = 100, minwidth = 100, anchor = CENTER)

    #create headings
    appliances_tree.heading("#0", text = "")
    appliances_tree.heading("Appliance ID", text = "Appliance ID", anchor = CENTER)
    appliances_tree.heading("Appliance Name", text = "Appliance Name", anchor = W)
    appliances_tree.heading("Appliance Rating", text = "Rating", anchor = CENTER)

    # Create Striped Row Tags
    appliances_tree.tag_configure('oddrow', background="white")
    appliances_tree.tag_configure('evenrow', background="lightblue")

    add_applianceName_Lbl = Label(appliances, text = "Appliance Name: ", font = ("Arial", 12), fg = "white", bg = "#162447")
    add_applianceName_Entry = Entry(appliances, width = 55, bg = "#1f4068", fg = "white")
    add_applianceRating_Lbl = Label(appliances, text = "Appliance Rating In Watts: ", font = ("Arial", 12), fg = "white", bg = "#162447")
    add_applianceRating_Entry = Entry(appliances, width = 55, bg = "#1f4068", fg = "white")

    search_applianceID_Lbl = Label(appliances, text = "Appliance ID: ", font = ("Arial", 12), fg = "white", bg = "#162447") 
    search_applianceID_Entry = Entry(appliances, width = 20, bg = "#1f4068", fg = "white")

    addAppliancesBtn = Button(appliances, text = "Add Appliance", width = 20, command = addData_Appliances, fg = "white", bg = "#1b1b2f")
    searchAppliancesBtn = Button(appliances, text = "Search Appliance", width = 20, command = searchData_Appliances, fg = "white", bg = "#1b1b2f")
    updateAppBtn = Button(appliances, text = "Update Appliance", width = 20, command = updateData_Appliances, fg = "white", bg = "#1b1b2f")
    deleteAppBtn = Button(appliances, text = "Delete Appliance", width = 20, command = deleteData_Appliances, fg = "white", bg = "#1b1b2f")

    showAllAppBtn = Button(appliances, text = "Show All Data", width = 20, command = readData_Appliances, fg = "white", bg = "#1b1b2f")

    toplevelTitle.grid(row = 0, column = 0, columnspan = 3, sticky = EW, pady = 20, padx = 20)
    appliances_tree.grid(row = 1, column = 0, columnspan = 3, sticky = EW, padx = 20)

    add_applianceName_Lbl.grid(row = 2, column = 0, sticky = W, padx = 20)
    add_applianceName_Entry.grid(row = 2, column = 1, columnspan = 2, padx = 20, sticky = W)
    add_applianceRating_Lbl.grid(row = 3, column = 0, sticky = W, padx = 20)
    add_applianceRating_Entry.grid(row = 3, column = 1, columnspan = 2, sticky = W, padx = 20)

    search_applianceID_Lbl.grid(row = 4, column = 0, sticky = W, padx = 20)
    search_applianceID_Entry.grid(row = 4, column = 1, sticky = W, padx = 20)
    searchAppliancesBtn.grid(row = 4, column = 2, pady = 10, sticky = W, padx = 20)

    addAppliancesBtn.grid(row = 5, column = 0, pady = 10, sticky = W, padx = 20)
    updateAppBtn.grid(row = 5, column = 1, pady = 10, sticky = W, padx = 20)
    deleteAppBtn.grid(row = 5, column = 2, pady = 10, sticky = W, padx = 20)

    showAllAppBtn.grid(row = 6, column = 0, pady = 10, sticky = W, padx = 20)
    readData_Appliances()


def addData_Room():
    insert_cmd = "INSERT INTO room_management (roomNum, roomName) VALUES (%s, %s);"
    get_roomNumber = add_roomNumber_Entry.get()
    get_roomName = add_roomName_Entry.get()

    if (get_roomNumber != "" and get_roomName != ""):
        value = (get_roomNumber, get_roomName)
        db_cursor.execute(insert_cmd, value)
        db_connection.commit()
        messagebox.showinfo("Information","Room added into the database.")
        add_roomName_Entry.delete(0, END)
        add_roomNumber_Entry.delete(0, END)
        readData_Room()
        
    else:
        messagebox.showinfo("Information","Blank field/s detected. Please fill up all fields.")

def readData_Room():
    select_cmd = "SELECT * from room_management"
    db_cursor.execute(select_cmd)
    data = db_cursor.fetchall()

    roomID = ""
    roomNumber = ""
    roomName = ""

    for record in db_tree.get_children():
        db_tree.delete(record)

    count = 0

    for x in data:
        roomID = x[0]
        roomNumber = x[1]
        roomName = x[2]

        if count % 2 == 0:
            db_tree.insert(parent = '', index = 'end', values = (roomID, roomNumber, roomName), tags = ('evenrow'))
        
        else:
            db_tree.insert(parent = '', index = 'end', values = (roomID, roomNumber, roomName), tags = ('oddrow'))
        
        count += 1
    
def searchData_Room():
    searchID = search_ID_Entry.get()
    select_cmd = "SELECT * from room_management WHERE roomID = " + searchID
    db_cursor.execute(select_cmd)
    data = db_cursor.fetchall()
    
    roomID = ""
    roomNumber = ""
    roomName = ""

    for record in db_tree.get_children():
        db_tree.delete(record)

    for x in data:
        roomID = x[0]
        roomNumber = x[1]
        roomName = x[2]
        db_tree.insert(parent = '', index = 'end', values = (roomID, roomNumber, roomName), tags = ('evenrow'))
    
    search_ID_Entry.delete(0, END)

def updateData_Room():
    roomID = search_ID_Entry.get()
    roomNumber = add_roomNumber_Entry.get()
    roomName = add_roomName_Entry.get()

    update_cmd = "UPDATE room_management SET roomNum = '%s', roomName = '%s' WHERE roomID = '%s'" %(roomNumber, roomName, roomID)
        
    if (roomNumber != "" and roomName != "" and roomID != ""):
        db_cursor.execute(update_cmd)
        db_connection.commit()
        messagebox.showinfo("Information", "Room updated.")
        readData_Room()
            
        search_ID_Entry.delete(0, END)
        add_roomNumber_Entry.delete(0, END)
        add_roomName_Entry.delete(0, END)

    else:
        messagebox.showinfo("Information", "Blank field/s detected. Please fill up all fields.")    

def deleteData_Room():
    roomID = search_ID_Entry.get()
    delete_cmd = "DELETE FROM room_management WHERE roomID = " + roomID

    if (roomID != ""):
        db_cursor.execute(delete_cmd)
        db_connection.commit()
        messagebox.showinfo("Information", "Room deleted.")
        search_ID_Entry.delete(0, END)
        readData_Room()
    
    else:
        messagebox.showinfo("Information", "Blank field/s detected. Please fill up all fields.")

def recordSelection():
    global selectedID, selectedRoom

    selected = db_tree.focus()
    temp = db_tree.item(selected, 'values')
    selectedID = temp[0]
    selectedRoom = temp[2]

#Create widgets
mainFrame = LabelFrame(root, padx = 20, pady = 10, bg = "#1b1b2f")
mainTitle = Label(mainFrame, text = "ROOM MANAGEMENT", font = ("Arial", 25), fg = "#e43f5a", bg = "#1b1b2f")

contentFrame = LabelFrame(mainFrame, padx = 20, pady = 10, bg = "#162447") 

add_roomName_Lbl = Label(contentFrame, text = "Room Name: ", font = ("Arial", 12), fg = "white", bg = "#162447")
add_roomName_Entry = Entry(contentFrame, width = 50, bg = "#1f4068", fg = "white")
add_roomNumber_Lbl = Label(contentFrame, text = "Room Number: ", font = ("Arial", 12), fg = "white", bg = "#162447")
add_roomNumber_Entry = Entry(contentFrame, width = 50, bg = "#1f4068", fg = "white")

search_ID_Lbl = Label(contentFrame, text = "Room ID: ", font = ("Arial", 12), fg = "white", bg = "#162447")
search_ID_Entry = Entry(contentFrame, width = 20, bg = "#1f4068", fg = "white")
searchRoomBtn = Button(contentFrame, text = "Search Room", width = 20, command = searchData_Room, fg = "white", bg = "#1b1b2f")

addRoomBtn = Button(contentFrame, text = "Add Room", width = 20, command = addData_Room, fg = "white", bg = "#1b1b2f")
updateRoomBtn = Button(contentFrame, text = "Update Room", width = 20, command = updateData_Room, fg = "white", bg = "#1b1b2f")
deleteRoomBtn = Button(contentFrame, text = "Delete Room", width = 20, command = deleteData_Room, fg = "white", bg = "#1b1b2f")

showAllRoomsBtn = Button(contentFrame, text = "Show All Data", width = 20, command = readData_Room, fg = "white", bg = "#1b1b2f")
goToAppliancesBtn = Button(contentFrame, text = "Add Appliances", width = 20, command = addAppliances, fg = "white", bg = "#1b1b2f")

#Add style to treeview
style = ttk.Style()
style.theme_use('default')

style.configure( "Treeview",
    background = "#D3D3D3",
    forground = "black",
    rowheight = 25,
    fieldbackground = "#D3D3D3"
)

style.map('Treeview', 
    background = [('selected', "#347083")]
)
#Create table using treeview
db_tree = ttk.Treeview(contentFrame)

#define columns
db_tree['columns'] = ("ID", "Room Number", "Room Name")

#format columns
db_tree.column("#0", width = 0, stretch = NO)
db_tree.column("ID", width = 50, minwidth = 50, anchor = CENTER)
db_tree.column("Room Number", width = 100, minwidth = 100, anchor = CENTER)
db_tree.column("Room Name", width = 150, minwidth = 100, anchor = W)

#create headings
db_tree.heading("#0", text = "")
db_tree.heading("ID", text = "ID", anchor = CENTER)
db_tree.heading("Room Number", text = "Room Number", anchor = CENTER)
db_tree.heading("Room Name", text = "Room Name", anchor = W)

# Create Striped Row Tags
db_tree.tag_configure('oddrow', background="white")
db_tree.tag_configure('evenrow', background="lightblue")

#Pack / Display widgets
mainFrame.pack()
mainTitle.pack()

contentFrame.pack()

db_tree.grid(row = 0, column = 0, columnspan=3, sticky = EW)

add_roomName_Lbl.grid(row = 1, column = 0, sticky = W)
add_roomName_Entry.grid(row = 1, column = 1, sticky = W, columnspan=2)
add_roomNumber_Lbl.grid(row = 2, column = 0, sticky = W)
add_roomNumber_Entry.grid(row = 2, column = 1, sticky = W, columnspan=2)

search_ID_Lbl.grid(row = 3, column = 0, sticky = W)
search_ID_Entry.grid(row = 3, column = 1, sticky = W)
searchRoomBtn.grid(row = 3, column = 2, sticky = W)

addRoomBtn.grid(row = 4, column = 0, pady = 10, sticky = W)
updateRoomBtn.grid(row = 4, column = 1, pady = 10, sticky = W)
deleteRoomBtn.grid(row = 4, column = 2, pady = 10, stick = W)

showAllRoomsBtn.grid(row = 5, column = 0, sticky = W)
goToAppliancesBtn.grid(row = 5, column = 2, pady = 10, sticky = W)


readData_Room()

#end root widget
root.mainloop()