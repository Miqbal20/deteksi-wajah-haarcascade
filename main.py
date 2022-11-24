import deteksi_gambar
import deteksi_webcam

dir_asset = "C:/Users/miqba/PycharmProjects/DeteksiWajah/assets"


def main():
    while True:
        print("================================")
        print("Pilih Program Deteksi Wajah")
        print("1. Menggunakan Gambar")
        print("2. Menggunakan Webcam")
        print("================================")
        pilihan = input("Masukan metode deteksi wajah : ")
        if pilihan == "1":
            deteksi_gambar.main(dir_asset)
        elif pilihan == "2":
            deteksi_webcam.main(dir_asset)
        elif pilihan == "q" or pilihan == "Q":
            print("Keluar")
            exit()
        else:
            print("Pilihan tidak ada")
            break


if __name__ == '__main__':
    main()
