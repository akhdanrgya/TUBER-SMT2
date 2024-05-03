import tkinter as tk
from tkinter import *

class SideBar:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root, bg="gray", width=150)
        self.frame.pack(side="left", fill="y")
        
        self.tittle = Label(self.frame, text="RENTALKU", font="Arial", bg="gray", fg="white")
        self.tittle.pack(fill="x", padx=10, pady=10)
        
        self.admin_btn = Button(self.frame, text="Admin", command=self.show_admin_panel)
        self.admin_btn.pack(fill="x", padx=5, pady=5)
        
        self.sewa_kendaraan_btn = Button(self.frame, text="Sewa Kendaraan", command=self.show_sewa_kendaraan_panel)
        self.sewa_kendaraan_btn.pack(fill="x", padx=5, pady=5)

        self.content_frame = tk.Frame(self.root)
        self.content_frame.pack(side="left", fill="both", expand=True)

        # Default content
        self.default_content()

    def default_content(self):
        # Konten default di samping sidebar
        self.default_label = Label(self.content_frame, text="Selamat datang di aplikasi RENTALKU", font="Arial")
        self.default_label.pack(fill="both", expand=True)

    def show_admin_panel(self):
        # Hapus konten yang ada di frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Tampilkan konten Admin
        self.admin_label = Label(self.content_frame, text="ADMIN PANEL RENTAL KENDARAAN", font="Arial")
        self.admin_label.pack(fill="both", expand=True)

    def show_sewa_kendaraan_panel(self):
        # Hapus konten yang ada di frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Tampilkan konten Sewa Kendaraan
        self.sewa_kendaraan_label = Label(self.content_frame, text="SEWA KENDARAAN", font="Arial")
        self.sewa_kendaraan_label.pack(fill="both", expand=True)

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rental Kendaraan")
        
        self.sidebar = SideBar(self.root)

        self.root.mainloop()

if __name__ == "__main__":
    GUI()
