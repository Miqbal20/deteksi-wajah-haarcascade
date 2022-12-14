import cv2


def main(dir_asset):
    # Sumber Gambar
    img = f"{dir_asset}/groubwajah.jpg"

    # Inisialisasi gambar
    foto = cv2.imread(img)

    # Metode yang bisa digunakan dalam deteksi wajah
    haarcascade_frontalface = f"{dir_asset}/haarcascade_frontalface_default.xml"
    haarcascade_eye = f"{dir_asset}/haarcascade_eye.xml"
    haarcascade_smile = f"{dir_asset}/haarcascade_smile.xml"

    while True:
        print("================================")
        print("Deteksi Melalui Gambar")
        print("1. Haarcascade Frontal Face")
        print("2. Haarcascade Eye")
        print("3. Haarcascade Smile")
        print("================================")
        pilihan = input("Masukan metode deteksi wajah : ")
        if pilihan == "1":
            faceDetektor = cv2.CascadeClassifier(haarcascade_frontalface)
            scale = 1.3
        elif pilihan == "2":
            faceDetektor = cv2.CascadeClassifier(haarcascade_eye)
            scale = 1.3
        elif pilihan == "3":
            faceDetektor = cv2.CascadeClassifier(haarcascade_smile)
            scale = 3
        elif pilihan == "q" or pilihan == "Q":
            print("Keluar")
            break
        else:
            print("Pilihan tidak ada")
            break

        rgbfoto = cv2.cvtColor(foto, cv2.COLOR_BGR2RGB)
        abufoto = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
        while True:
            muka = faceDetektor.detectMultiScale(abufoto, scale, 1)
            for (x, y, w, h) in muka:
                fotook = cv2.rectangle(rgbfoto, (x, y), (x + h, y + h), (0, 0, 255), 1)
                result = cv2.cvtColor(fotook, cv2.COLOR_BGR2RGB)
                cv2.imshow('Foto Cek', result)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
