import tkinter as tk
from tkinter import ttk
import os
import datetime

"""
Author: Brandon Donkersloot
Assignment 4
This program models a windows file explorer using the ttk module. 

 
"""

def on_item_selected_left(event):
    selectedItem = leftTree.focus()  # Get the selected item's ID
    fullPath = items[selectedItem]
    # if there is already something in the top pane, wipe it
    if topTree.get_children():
        topTree.delete(topTree.get_children()[0])
    # if there is already something in the right pane, wipe it
    if rightTree.get_children():
        for i in rightTree.get_children():
            rightTree.delete(i)

    if not any(os.path.isdir(os.path.join(fullPath, item)) for item in os.listdir(fullPath)):
        entries = os.listdir(fullPath)
        for i in entries:
            fullEntryPath = os.path.join(fullPath, i)
            if os.path.isfile(fullEntryPath):
                size = os.path.getsize(fullEntryPath)
                timeNum = os.path.getmtime(fullEntryPath)
                dateModified = datetime.datetime.fromtimestamp(timeNum)
                name = os.path.basename(i)
                entry = rightTree.insert("", "end", values=(fullEntryPath, name, size, dateModified))
                itemsRight[entry] = fullEntryPath

    else:
        try:
            subDirsCount = 0
            filesCount = 0
            totalSize = 0
            # Count immediate subdirectories and files
            entries = os.listdir(fullPath)
            if fullPath not in selectedItemsLeft:
                for i in entries:
                    fullEntryPath = os.path.join(fullPath, i)
                    if os.path.isdir(fullEntryPath):
                        entry = leftTree.insert(selectedItem, "end", text=(i))
                        items[entry] = fullEntryPath
                        subDirsCount += 1
                    else:
                        totalSize += os.path.getsize(fullEntryPath)
                        filesCount += 1
                selectedItemsLeft.append(fullPath) # add to a dictionary of alreaddy selected item to avoid duplicates
            topTree.insert("", "end", values=(fullPath, subDirsCount, filesCount, totalSize))
        except Exception as e:
            print(e)
def on_item_selected_right(event):

    selectedItem = rightTree.focus() # Get the selected item's ID
    rightTree.item(selectedItem, tags=("redText",))
    fullPath = itemsRight[selectedItem] # get path located in the dictionary based on key - item id
    size = os.path.getsize(fullPath)
    timeNum = os.path.getmtime(fullPath)
    dateModified = datetime.datetime.fromtimestamp(timeNum)
    name = os.path.basename(fullPath)
    message = f'Full path = {fullPath}\n' \
              f'File name = {name}\n' \
              f'File size = {size}\n ' \
              f'Date last modified = {dateModified}'

    popup = tk.Toplevel(rightFrame)
    popup.title("File Summary")
    popup.geometry("300x150")

    # Use a Label to display the text
    ttk.Label(popup, text=message).pack(pady=20)

    ttk.Button(popup, text="Close", command=popup.destroy).pack(pady=10)


items = {}
itemsRight = {}
selectedItemsLeft = []

root = tk.Tk()
root.title("File Explorer")

# Get screen size
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# Calculate size
windowWidth = int(screenWidth * 0.7)
windowHeight = int(screenHeight * 0.6)

#set program size
root.geometry(f"{windowWidth}x{windowHeight}")

#create top frame
topFrame = tk.Frame(root, height=windowHeight * .1)
topFrame.pack(fill="x", side="top", padx=10, pady=15)
topFrame.pack_propagate(False)
ttk.Label(topFrame, text="Summary").pack()

# Create a Treeview for top pane
topTree = ttk.Treeview(topFrame, columns=("Full Path", "# of Subdirectories", "# of Files", "Size of Immediate Files"), show='headings')
topTree.heading("Full Path", text="Full Path")
topTree.heading("# of Subdirectories", text="# of Subdirectories")
topTree.heading("# of Files", text="# of Files")
topTree.heading("Size of Immediate Files", text="Size of Immediate Files")

topTree.pack()

#create left frame
leftFrame = tk.Frame(root)
leftFrame.pack(fill="both", expand=True, side="left", padx=10, pady=15)
ttk.Label(leftFrame, text="Directories").pack()
leftFrame.pack_propagate(False)

# Create a Treeview for left pane
leftTree = ttk.Treeview(leftFrame)

#create right frame
rightFrame = tk.Frame(root)
rightFrame.pack(fill="both", expand=True, side="right", padx=10, pady=15)
ttk.Label(rightFrame, text="Files").pack()
rightFrame.pack_propagate(False)


# bind function to event
leftTree.bind("<<TreeviewSelect>>", on_item_selected_left)



root_path = "C:\\"

# add data to left tree
for item in os.listdir(root_path):
    full_path = os.path.join(root_path, item)
    # if folder
    if os.path.isdir(full_path):
        entryID = leftTree.insert("", "end", text=(item))
        items[entryID] = full_path



# Add vertical scrollbar
verticleScrollBar = ttk.Scrollbar(leftFrame, orient="vertical", command=leftTree.yview)
leftTree.configure(yscrollcommand=verticleScrollBar.set)

leftTree.pack(side="left", fill="both", expand=True)
verticleScrollBar.pack(side="right", fill="y")

# Create a Treeview for right pane
rightTree = ttk.Treeview(rightFrame, columns=("Full Path", "Name", "Size", "Date last Modified"), show='headings')
rightTree.heading("Full Path", text="Full Path")
rightTree.heading("Name", text="Name")
rightTree.heading("Size", text="Size")
rightTree.heading("Date last Modified", text="Date last Modified")

rightTree.bind("<<TreeviewSelect>>", on_item_selected_right) # bind function to event
rightTree.tag_configure("redText", foreground="red") # tag for red text
# Add scrollbar
horizontalScrollBar = ttk.Scrollbar(rightFrame, orient="horizontal", command=rightTree.xview)
rightTree.configure(xscrollcommand=horizontalScrollBar.set)

rightTree.pack(side="top", fill="both", expand=True)
horizontalScrollBar.pack(side="bottom", fill="x")

root.mainloop()
