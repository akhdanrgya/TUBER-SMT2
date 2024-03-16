import mysql.connector
import os

myDb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rental"
)

myCursor = myDb.cursor()


def add_vehicle(table_name, brand, plat, *args):
    values = (brand, plat, *args)
    placeholders = ",".join(["%s"] * len(values))
    sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
    myCursor.execute(sql, values)
    myDb.commit()
    print(f"{'Mobil' if table_name == 'mobil' else 'Motor'} berhasil ditambahkan")


def show_vehicles(table_name):
    if table_name == 'mobil':
        myCursor.execute("SELECT id_mobil, brand, plat, harga FROM mobil")
    elif table_name == 'motor':
        myCursor.execute("SELECT id_motor, brand, plat, cc, harga FROM motor")

    for row in myCursor:
        print(f"\nId      : {row[0]}")
        print(f"Brand   : {row[1]}")
        print(f"Plat    : {row[2]}")
        if table_name == 'motor':
            print(f"CC      : {row[3]}")
        print(f"Harga   : {row[-1]}")


def check_id_exist(table_name, id_value):
    myCursor.execute(f"SELECT * FROM {table_name}")
    id_records = myCursor.fetchall()
    id_list = [record[0] for record in id_records]
    return id_value in id_list


def admin_menu():
    os.system("cls")
    while True:
        print("""
              <<< Menu Admin >>>
              
              1. Tambah Mobil
              2. Tambah Motor
              3. Back
              4. Exit
              
              """)
        pilih = int(input("Masukan Pilihan: "))

        if pilih == 1:
            brandMobil = input("Masukkan brand mobil: ")
            platMobil = input("Masukkan plat mobil: ")
            hargaMobil = input("Masukkan harga sewa mobil: ")
            add_vehicle('mobil', brandMobil, platMobil, hargaMobil)

        elif pilih == 2:
            brandMotor = input("Masukan brand motor: ")
            platMotor = input("Masukan plat motor: ")
            cc = input("Masukan CC motor: ")
            hargaMotor = input("Masukan harga sewa motor: ")
            add_vehicle('motor', brandMotor, platMotor, cc, hargaMotor)

        elif pilih == 3:
            break


def main():
    os.system("cls")
    while True:
        print("""
            <<< Menu Utama >>>
            
            1. Sewa Mobil
            2. Sewa Motor
            3. Daftar Kendaraan
            4. Admin
            5. Exit
            
            """)
        pilih = int(input("Masukan Pilihan: "))

        if pilih == 1:
            sewaMobil = int(input("Masukan ID Mobil: "))
            print("1" if check_id_exist('mobil', sewaMobil) else "error")

        elif pilih == 2:
            sewaMotor = int(input("Masukan ID Motor: "))
            print("Anjay" if check_id_exist('motor', sewaMotor) else "error")

        elif pilih == 3:
            os.system("cls")
            while True:
                print("""
            <<< Daftar Kendaraan >>>
            
            1. Mobil
            2. Motor
            3. Back
            
            """)

                pilihDaftar = int(input("Masukan Pilihan: "))

                if pilihDaftar == 1:
                    show_vehicles('mobil')
                elif pilihDaftar == 2:
                    show_vehicles('motor')
                elif pilihDaftar == 3:
                    os.system("cls")
                    break

        elif pilih == 4:
            admin_menu()

        elif pilih == 5:
            break


if __name__ == "__main__":
    main()
