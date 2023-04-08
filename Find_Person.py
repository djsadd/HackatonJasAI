import face_recognition
import cv2
import numpy as np
import os


def get_person(photo, db):
    cursor = db.cursor()
    cascPathface = os.path.dirname(
        cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
    faceCascade = cv2.CascadeClassifier(cascPathface)
    lst_encoding = []
    cursor.execute("select encoding_vector, title from person inner join photo ON person.id=photo.person_id")
    while True:
        mobile = cursor.fetchone()
        if mobile:
            lst_encoding.append(mobile)
        else:
            break

    lst_name = []
    lst_data = []

    for row in lst_encoding:
        lst_data.append(np.array(row[0].split(), dtype='float64'))
        lst_name.append(row[1])

    data = {'encodings': lst_data, 'names': lst_name}
    image = cv2.imread(photo)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(60, 60),
                                         flags=cv2.CASCADE_SCALE_IMAGE)

    encodings = face_recognition.face_encodings(rgb)
    names = []
    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"],
                                                 encoding)
        name = "Unknown"
        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
                name = max(counts, key=counts.get)
                print(name)

            names.append(name)
            for ((x, y, w, h), name) in zip(faces, names):
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(image, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (0, 255, 0), 2)
        # cv2.imshow("Frame", image)
        # cv2.waitKey(0)
        return image