import cv2
from deepface import DeepFace
import numpy as np

kamera = cv2.VideoCapture(0)
if not kamera.isOpened():
    print("Kamerani ochib bo'lmadi!")
    exit()

print("AI ishga tushdi... 'q' bosilsa, chiqadi.\n")

while True:
    ret, frame = kamera.read()
    if not ret:
        break

    # Teskari kamerani to‘g‘rilaymiz (agar o‘ng-chap almashtirilgan bo‘lsa)
    frame = cv2.flip(frame, 1)

    cv2.imshow("Muslihiddin AI - Real Time Analysis 🧠", frame)

    try:
        natijalar = DeepFace.analyze(
            frame,
            actions=['age', 'gender', 'emotion'],
            enforce_detection=False
        )

        info = natijalar[0]
        yosh = int(info['age'])
        jins_dict = info['gender']

        # Jinsni aniq belgilaymiz
        jins = "Erkak" if jins_dict['Man'] > jins_dict['Woman'] else "Ayol"
        kayfiyat = info['dominant_emotion']

        # Yoshni yumshatish (ko‘p hollarda 5-10 yosh qo‘shib yuboradi)
        if yosh > 30:
            yosh -= np.random.randint(5, 10)

        print(f"👤 Jins: {jins} | 🎂 Yosh taxminan: {yosh} yosh | 😊 Kayfiyat: {kayfiyat}")

    except Exception:
        pass

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
