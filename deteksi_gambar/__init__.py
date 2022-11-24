import cv2


def main():
    # Sumber Gambar
    img = "C:/Users/miqba/PycharmProjects/DeteksiWajah/assets/groubwajah.jpg"

    # Metode yang bisa digunakan dalam deteksi wajah
    haarcascade_frontalface = "C:/Users/miqba/PycharmProjects/DeteksiWajah/assets/haarcascade_frontalface_default.xml"
    haarcascade_eye = "C:/Users/miqba/PycharmProjects/DeteksiWajah/assets/haarcascade_eye.xml"
    haarcascade_smile = "C:/Users/miqba/PycharmProjects/DeteksiWajah/assets/haarcascade_smile.xml"

    # Inisialisasi gambar
    foto = cv2.imread(img)
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
            scale = 5
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
                result = cv2.cvtColor(rgbfoto, cv2.COLOR_BGR2RGB)
                cv2.imshow('Foto Cek', result)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
