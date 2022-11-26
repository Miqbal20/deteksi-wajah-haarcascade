import cv2


def main(dir_asset):
    # Metode yang bisa digunakan dalam deteksi wajah
    haarcascade_frontalface = f"{dir_asset}/haarcascade_frontalface_default.xml"
    haarcascade_eye = f"{dir_asset}/haarcascade_eye.xml"
    haarcascade_smile = f"{dir_asset}/haarcascade_smile.xml"

    while True:
        print("================================")
        print("Deteksi Menggunakan Webcam")
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

        cam = cv2.VideoCapture(0)
        cam.set(3, 640)
        cam.set(4, 480)

        while True:
            retV, frame = cam.read()
            abu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            muka = faceDetektor.detectMultiScale(abu, scale, 3)
            for (x, y, w, h) in muka:
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.imshow('Kamera', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
