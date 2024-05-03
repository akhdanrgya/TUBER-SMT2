import tkinter as tk
from tkinter import *

class AdminPanel:
    def __init__(self, root):
        self.root = root
        self.root_admin = tk.Toplevel(self.root)
        self.root_admin.title("Admin panel")

        self.label_admin = Label(self.root_admin, text="Enter PIN:", font="Arial")
        self.label_admin.pack(padx=50, pady=10)

        self.pin_admin = Entry(self.root_admin, show="*")
        self.pin_admin.pack(padx=50, pady=5)

        self.btn_admin = Button(self.root_admin, text="Enter", command=self.check_pin)
        self.btn_admin.pack(padx=50, pady=10)

    def check_pin(self):
        pin = self.pin_admin.get()

        if pin == "123":
            self.root_admin.destroy()
            AdminPanelWindow(self.root)
        else:
            self.label_admin.config(text="Incorrect PIN. Try again.", font="Arial", fg="red")
            self.pin_admin.delete(0, 'end')

class AdminPanelWindow:
    def __init__(self, root):
        self.root = root
        self.root_admin_panel = tk.Tk()
        self.root_admin_panel.title("Admin panel")
        
        self.admin_label = Label(self.root_admin_panel, text="ADMIN PANEL RENTAL KENDARAAN", font="Arial")
        self.admin_label.pack(padx=50, pady=20)

class SewaKendaraanWindow:
    def __init__(self, root):
        self.root = root
        self.root_sewaKendaraan_panel = tk.Tk()
        self.root_sewaKendaraan_panel.title("Sewa kendaraan")
        
        self.sewaKendaraan_label = Label(self.root_sewaKendaraan_panel, text="SEWA KENDARAAN", font="Arial")
        self.sewaKendaraan_label.pack(padx=50, pady=20)

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rental Kendaraan")
        
        self.label = Label(self.root, text="RENTAL KENDARAAN", font="Arial")
        self.label.pack(padx=50, pady=20)
        
        self.admin_btn = Button(self.root, text="Admin", command=self.open_admin_panel)
        self.admin_btn.pack(padx=10, pady=10)

        self.sewa_kendaraan = Button(self.root, text="Sewa Kendaraan", command=self.open_sewaKendaraan_panel)
        self.sewa_kendaraan.pack(padx=10, pady=10)
        
        self.root.mainloop()

    def open_admin_panel(self):
        AdminPanel(self.root)
    
    def open_sewaKendaraan_panel(self):
        SewaKendaraanWindow(self.root)

GUI()
