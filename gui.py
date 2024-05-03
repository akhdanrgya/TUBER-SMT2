import tkinter as tk
from tkinter import *

class GUI:
    
    def __init__(self):
        
        def click():
            self.screen = tk.Tk()
            self.screen.title("Anjay di click")

            self.label = tk.Label(self.screen, text=self.i.get())
            self.label.pack(padx=20, pady=20)
            
        self.screen = tk.Tk()
        self.screen.title("Rental Kendaraan")
        
        self.i = Entry(self.screen, width=50)
        self.i.pack()

        self.label = tk.Label(self.screen, text="RENTAL APP", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)
        
        self.btn1 = Button(self.screen, text="click aku dong kak", command=click, fg="black", bg="gray")
        self.btn1.pack()
        
        for x in range(5):
            self.btn2 = Button(self.screen, text=f"loop ke {x + 1}")
            self.btn2.pack()

        self.screen.mainloop()


GUI()
