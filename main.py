from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as py
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
        print(f"Gagal menambahkan kendaraan : {err}")


def deleteVehicle(table, vehicle_id):
    try:
        sql = f"DELETE FROM {table} WHERE {'id_mobil' if table == 'mobil' else 'id_motor'} = %s"
        myCursor.execute(sql, (vehicle_id))
        myDb.commit()
        print(f"{'Mobil' if table == 'mobil' else 'Motor'} berhasil dihapus")
    except Exception as err:
        print(f"Gagal menghapus kendaraan : {err}")


def updateVehicle(table, vehicle_id, value, edit):
    try:
        sql = f"UPDATE {table} SET {edit} = {value} WHERE {'id_mobil' if table == 'mobil' else 'id_motor'} = {vehicle_id}"
        myCursor.execute(sql)
        myDb.commit()
        print(f"{'Mobil' if table == 'mobil' else 'Motor'} berhasil diedit")
    except Exception as err:
        print(f"Gagal update kendaraan : {err}")


def insertToTransaction(nama, jenis, idKendaraan, waktuAwal, waktu):

    waktuAkhir = waktuAwal + timedelta(hours=waktu)
    myCursor.execute(
        f"SELECT harga FROM {jenis} WHERE id_{jenis} = {idKendaraan}")
    harga = myCursor.fetchone()[0]
    jumlahHarga = harga * waktu

    try:
        sql = f"INSERT INTO transaction (nama, jenisKendaraan, idKendaraan, waktuAwal, waktuAkhir, harga) VALUES ('{nama}', '{jenis}', {idKendaraan}, '{waktuAwal}', '{waktuAkhir}', {jumlahHarga})"
        myCursor.execute(sql)
        myDb.commit()
        print(
            f"{jenis} di sewa oleh {nama} dengan total waktu {waktu} dengan total harga {jumlahHarga}")
    except Exception as err:
        print(f"Gagal menambahkan transaction : {err}")


def transaction(jenis, idKendaraan):
    nama = input("Masukan nama anda: ")
    waktuAwal = datetime.now()
    waktu = int(input("Masukan total waktu perjam (1/2/3/4.....): "))

    insertToTransaction(nama, jenis, idKendaraan, waktuAwal, waktu)


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
        print(f"gagal untuk show vehicle : {err}")


def showTransaction():
    try:
        myCursor.execute("SELECT * FROM transaction")

        for row in myCursor:
            print(f"\nId              : {row[0]}")
            print(f"Nama            : {row[1]}")
            print(f"Jenis           : {row[2]}")
            print(f"Id Kendaraan    : {row[3]}")
            print(f"Waktu Awal      : {row[4]}")
            print(f"Waktu Akhir     : {row[5]}")
            print(f"Harga           : {row[6]}")

    except Exception as err:
        print(f"Gagal untuk show transaction : {err}")
        
def statTransaction():
    try:
        fig, ax = plt.subplots()
        totalBulan = {"March" : 0, "April" : 0}
        myCursor.execute("SELECT harga, DATE_FORMAT(waktuAwal, '%M') FROM transaction")
        for row in myCursor:
            harga = row[0]
            bulan = row[1]
            
            if bulan in totalBulan:
                totalBulan[bulan] += harga
        
        bar_label = ["red", "blue"]
        bar_color = ['tab:red', 'tab:blue']
        
        ax.bar(totalBulan.keys(), totalBulan.values(), label = bar_label, color = bar_color)
        ax.set_ylabel("Keuntungan")
        ax.set_xlabel("Bulan")
        ax.set_title("Statistik keuntungan perbulan di tahun 2024")
        ax.legend(title = "warna")
        
        plt.show()
        
    except Exception as err:
        print(f"gagal untuk fetch transaction : {err}")


def admin():
    try:
        os.system("cls")
        while True:
            print("""
                <<< Menu Admin >>>
                
                1. Tambah
                2. Hapus
                3. Edit
                4. Data Transaksi
                5. Stat
                6. Back
                7. Exit
                
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

            elif pilih == 3:
                jenis = input(
                    "Masukan jenis kendaraan yang ingin di edit (mobil/motor): ")
                idKendaraan = int(
                    input("Masukan id kendaraan yang ingin diedit: "))
                edit = input(
                    "Masukan apa yang ingin di edit (brand, plat, cc, harga): ")
                value = input("Masukan value: ")

                updateVehicle(jenis, idKendaraan, value, edit)

            elif pilih == 4:
                showTransaction()

            elif pilih == 6:
                main()
            
            elif pilih == 5:
                statTransaction()

    except Exception as err:
        print(f"fungsi admin error : {err}")


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
                    jenis = 'mobil'
                    transaction(jenis, sewaMobil)
                else:
                    print(f"Mobil dengan id {sewaMobil} tidak ada")

            elif pilih == 2:
                sewaMotor = int(input("Masukan ID Motor: "))

                myCursor.execute("SELECT id_motor FROM motor")
                idMotor_records = myCursor.fetchall()

                idMotor_list = [record[0] for record in idMotor_records]

                if sewaMotor in idMotor_list:
                    jenis = 'motor'
                    transaction(jenis, sewaMotor)
                else:
                    print(f"Motor dengan id {sewaMotor} tidak ada")

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
