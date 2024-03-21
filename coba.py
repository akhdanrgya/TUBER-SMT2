import mysql.connector
import os
import tkinter as tk
from tkinter import messagebox

myDb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rental"
)

myCursor = myDb.cursor()


def addVehicle(table, brand, plat, *args):
    try:
        values = (brand, plat, *args)
        placeholders = ",".join(["%s"] * len(values))
        sql = f"INSERT INTO {table} VALUES ({placeholders})"
        myCursor.execute(sql, values)
        myDb.commit()
        messagebox.showinfo("Success", f"{'Mobil' if table == 'mobil' else 'Motor'} berhasil ditambahkan")
    except Exception as err:
        messagebox.showerror("Error", f"fungsi addVehicle error : {err}")


def deleteVehicle(table, vehicle_id):
    try:
        sql = f"DELETE FROM {table} WHERE {'id_mobil' if table == 'mobil' else 'id_motor'} = %s"
        myCursor.execute(sql, (vehicle_id,))
        myDb.commit()
        messagebox.showinfo("Success", f"{'Mobil' if table == 'mobil' else 'Motor'} berhasil dihapus")
    except Exception as err:
        messagebox.showerror("Error", f"fungsi deleteVehicle error : {err}")


def admin_window():
    admin_window = tk.Tk()
    admin_window.title("Admin Menu")

    def add_menu():
        add_window = tk.Toplevel(admin_window)
        add_window.title("Tambah Kendaraan")

        tk.Label(add_window, text="Pilih jenis kendaraan:").pack()
        add_choice = tk.StringVar(add_window)

        add_menu_option = tk.OptionMenu(add_window, add_choice, "Mobil", "Motor")
        add_menu_option.pack()

        def add_vehicle():
            add_choice_value = add_choice.get()

            if add_choice_value == "Mobil":
                brandMobil = brand_entry.get()
                platMobil = plat_entry.get()
                hargaMobil = harga_entry.get()
                addVehicle("mobil", None, brandMobil, platMobil, hargaMobil)
            elif add_choice_value == "Motor":
                brandMotor = brand_entry.get()
                platMotor = plat_entry.get()
                cc = cc_entry.get()
                hargaMotor = harga_entry.get()
                addVehicle("motor", None, brandMotor, platMotor, hargaMotor, cc)
            add_window.destroy()

        tk.Label(add_window, text="Brand:").pack()
        brand_entry = tk.Entry(add_window)
        brand_entry.pack()

        tk.Label(add_window, text="Plat:").pack()
        plat_entry = tk.Entry(add_window)
        plat_entry.pack()

        tk.Label(add_window, text="Harga:").pack()
        harga_entry = tk.Entry(add_window)
        harga_entry.pack()

        tk.Label(add_window, text="CC (Hanya untuk Motor):").pack()
        cc_entry = tk.Entry(add_window)
        cc_entry.pack()

        tk.Button(add_window, text="Tambah", command=add_vehicle).pack()

    def delete_menu():
        delete_window = tk.Toplevel(admin_window)
        delete_window.title("Hapus Kendaraan")

        tk.Label(delete_window, text="Pilih jenis kendaraan:").pack()
        delete_choice = tk.StringVar(delete_window)

        delete_menu_option = tk.OptionMenu(delete_window, delete_choice, "Mobil", "Motor")
        delete_menu_option.pack()

        def delete_vehicle():
            delete_choice_value = delete_choice.get()
            delete_id = id_entry.get()

            if delete_choice_value == "Mobil":
                deleteVehicle("mobil", delete_id)
            elif delete_choice_value == "Motor":
                deleteVehicle("motor", delete_id)
            delete_window.destroy()

        tk.Label(delete_window, text="ID Kendaraan:").pack()
        id_entry = tk.Entry(delete_window)
        id_entry.pack()

        tk.Button(delete_window, text="Hapus", command=delete_vehicle).pack()

    tk.Button(admin_window, text="Tambah Kendaraan", command=add_menu).pack()
    tk.Button(admin_window, text="Hapus Kendaraan", command=delete_menu).pack()

    admin_window.mainloop()


def main_window():
    main_window = tk.Tk()
    main_window.title("Menu Utama")

    def show_vehicles_menu():
        show_vehicles_window = tk.Toplevel(main_window)
        show_vehicles_window.title("Daftar Kendaraan")

        def show_vehicles(table_name):
            try:
                vehicles_text = ""
                if table_name == 'mobil':
                    myCursor.execute("SELECT id_mobil, brand, plat, harga FROM mobil")
                    vehicles_text += "Daftar Mobil:\n"
                elif table_name == 'motor':
                    myCursor.execute("SELECT id_motor, brand, plat, cc, harga FROM motor")
                    vehicles_text += "Daftar Motor:\n"

                for row in myCursor:
                    vehicles_text += f"\nId: {row[0]}\n"
                    vehicles_text += f"Brand: {row[1]}\n"
                    vehicles_text += f"Plat: {row[2]}\n"
                    if table_name == 'motor':
                        vehicles_text += f"CC: {row[3]}\n"
                    vehicles_text += f"Harga: {row[-1]}\n"
                    vehicles_text += "\n"

                vehicles_label.config(text=vehicles_text)
            except Exception as err:
                messagebox.showerror("Error", f"fungsi show_vehicles error : {err}")

        tk.Button(show_vehicles_window, text="Daftar Mobil",
                  command=lambda: show_vehicles("mobil")).pack()
        tk.Button(show_vehicles_window, text="Daftar Motor",
                  command=lambda: show_vehicles("motor")).pack()

        vehicles_label = tk.Label(show_vehicles_window, text="")
        vehicles_label.pack()

    tk.Button(main_window, text="Daftar Kendaraan", command=show_vehicles_menu).pack()
    tk.Button(main_window, text="Admin", command=admin_window).pack()
    tk.Button(main_window, text="Exit", command=main_window.destroy).pack()

    main_window.mainloop()


if __name__ == "__main__":
    main_window()
