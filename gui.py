import tkinter as tk
from tkinter import *

class GUI:
    
    def __init__(self):
        
        def adminPin():
            self.root_admin = tk.Toplevel()
            self.root_admin.title("Admin panel")

            self.label_admin = Label(self.root_admin, text="Enter PIN:", font="Arial")
            self.label_admin.pack(padx=50, pady=10)

            self.pin_admin = Entry(self.root_admin, show="*")
            self.pin_admin.pack(padx=50, pady=5)

            self.btn_admin = Button(self.root_admin, text="Enter", command=checkPin)
            self.btn_admin.pack(padx=50, pady=10)
        
        def checkPin():
            pin = self.pin_admin.get()

            if pin == "123":
                # self.label_admin.config(text="ADMIN PANEL RENTAL KENDARAAN", font="Arial")
                self.root_admin.destroy()
                adminPanel()
            else:
                self.label_admin.config(text="Incorrect PIN. Try again.", font="Arial", fg="red")
                self.pin_admin.delete(0, 'end')
        
        def adminPanel():
            self.rootAdminPanel = tk.Tk()
            self.rootAdminPanel.title("ADMIN PANEL RENTAL KENDARAAN")
            
            self.adminLabel = Label(self.rootAdminPanel, text="ADMIN PANEL RENTAL KENDARAAN", font="Arial")
            self.adminLabel.pack(padx=50, pady=20)

        self.root = tk.Tk()
        self.root.title("Rental Kendaraan")
        
        self.label = Label(self.root, text="RENTAL KENDARAAN", font="Arial")
        self.label.pack(padx=50, pady=20)
        
        self.adminBTN = Button(self.root, text="Admin", command=adminPin)
        self.adminBTN.pack(padx=10, pady=10, side="left")
        
        self.root.mainloop()

GUI()
