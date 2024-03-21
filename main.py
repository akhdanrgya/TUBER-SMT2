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
    try:
        values = (brand, plat, *args)
        placeholders = ",".join(["%s"] * len(values))
        sql = f"INSERT INTO {table} VALUES ({placeholders})"
        myCursor.execute(sql, values)
        myDb.commit()
        print(f"{'Mobil' if table == 'mobil' else 'Motor'} berhasil ditambahkan")
    except Exception as err:
        print(f"fungsi addVehicle error : {err}")


def deleteVehicle(table, vehicle_id):
    try:
        sql = f"DELETE FROM {table} WHERE {'id_mobil' if table == 'mobil' else 'id_motor'} = %s"
        myCursor.execute(sql, (vehicle_id,))
        myDb.commit()
        print(f"{'Mobil' if table == 'mobil' else 'Motor'} berhasil dihapus")
    except Exception as err:
        print(f"fungsi deleteVehicle error : {err}")


def admin():
    try:
        os.system("cls")
        while True:
            print("""
                <<< Menu Admin >>>
                
                1. Tambah
                2. Hapus
                3. Edit
                4. Back
                5. Exit
                
                """)
            pilih = int(input("Masukan Pilihan: "))

            if pilih == 1:
                print("""
                1. Mobil
                2. Motor
                3. Back
                      """)

                pilihSub1 = int(input("Masukan Pilihan: "))

                if pilihSub1 == 1:
                    brandMobil = input("Masukkan brand mobil: ")
                    platMobil = input("Masukkan plat mobil: ")
                    hargaMobil = input("Masukkan harga sewa mobil: ")
                    addVehicle("mobil", None, brandMobil,
                               platMobil, hargaMobil)
                elif pilihSub1 == 2:
                    brandMotor = input("Masukan brand motor: ")
                    platMotor = input("Masukan plat motor: ")
                    cc = input("Masukan CC motor: ")
                    hargaMotor = input("Masukan harga sewa motor: ")
                    addVehicle("motor", None, brandMotor,
                               platMotor, hargaMotor, cc)
                elif pilihSub1 == 3:
                    admin()

            elif pilih == 2:
                print("""
                1. Mobil
                2. Motor
                3. Back
                      """)

                pilihSub2 = int(input("Masukan Pilihan: "))

                if pilihSub2 == 1:
                    delete_id = int(
                        input("Masukkan ID Mobil yang akan dihapus: "))
                    deleteVehicle("mobil", delete_id)
                elif pilihSub2 == 2:
                    delete_id = int(
                        input("Masukkan ID Motor yang akan dihapus: "))
                    deleteVehicle("motor", delete_id)
                elif pilihSub2 == 3:
                    admin()

            elif pilih == 4:
                main()
    except Exception as err:
        print(f"fungsi admin error : {err}")


def show_vehicles(table_name):
    try:
        if table_name == 'mobil':
            myCursor.execute("SELECT id_mobil, brand, plat, harga FROM mobil")
        elif table_name == 'motor':
            myCursor.execute(
                "SELECT id_motor, brand, plat, cc, harga FROM motor")

        for row in myCursor:
            print(f"\nId      : {row[0]}")
            print(f"Brand   : {row[1]}")
            print(f"Plat    : {row[2]}")
            if table_name == 'motor':
                print(f"CC      : {row[3]}")
            print(f"Harga   : {row[-1]}")
    except Exception as err:
        print(f"fungsi show_vehicles error : {err}")


def main():
    try:
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
                else:
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
    except Exception as err:
        print(f"fungsi main error : {err}")


main()
