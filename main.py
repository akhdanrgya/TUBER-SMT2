import mysql.connector
import os


myDb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rental"
)

myCursor = myDb.cursor()

def addVehicle(table, brand, plat, *args):
    values = (brand, plat, *args)
    placeholders = ",".join(["%s"] * len(values))
    sql = f"INSERT INTO {table} VALUES ({placeholders})"
    myCursor.execute(sql, values)
    myDb.commit()
    print(f"{'Mobil' if table == 'mobil' else 'Motor'} berhasil ditambahkan") 


def admin():
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
            
            addVehicle("mobil", None, brandMobil, platMobil, hargaMobil)

        elif pilih == 2:
            brandMotor = input("Masukan brand motor: ")
            platMotor = input("Masukan plat motor: ")
            cc = input("Masukan CC motor: ")
            hargaMotor = input("Masukan harga sewa motor: ")
            
            addVehicle("motor", None, brandMotor, platMotor, hargaMotor, cc)

        elif pilih == 3:
            main()


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

            myCursor.execute("SELECT id_mobil FROM mobil")
            idMobil_records = myCursor.fetchall()

            idMobil_list = [record[0] for record in idMobil_records]

            if sewaMobil in idMobil_list:
                print("1")
            else:
                print("error")

        elif pilih == 2:
            sewaMotor = int(input("Masukan ID Motor: "))

            myCursor.execute("SELECT id_motor FROM motor")
            idMotor_records = myCursor.fetchall()

            idMotor_list = [record[0] for record in idMotor_records]

            if sewaMotor in idMotor_list:
                print("Anjay")
            else :
                print("error")

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
                    show_vehicles("mobil")
                elif pilihDaftar == 2:
                    show_vehicles("motor")
                elif pilihDaftar == 3:
                    main()

        elif pilih == 4:
            admin()
        
        elif pilih == 5:
            print("Terimakasih sudah menggunakan aplikasi ini :)")
            break


main()
