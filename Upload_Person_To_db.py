from imutils import paths
import face_recognition
import pickle
import cv2
import os
import psqlpt

db = psqlpt.create_connection('hackatosjasai', 'postgres', '', 'localhost', '5432')
cursor = db.cursor()


def add_person_to_db(name, path):
    image = cv2.imread(path)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model='hog')
    encodings = face_recognition.face_encodings(rgb, boxes)

    data = {"encodings": encodings, "names": name}

    try:
        book = ''
        for res in data['encodings'][0]:
            book += str(res)
            book += ' '

        postgres_insert_photo = """INSERT INTO photo(encoding_vector, person_id) VALUES(%s, %s)"""
        cursor.execute("select id, title from person")
        lst_persons = []

        while True:
            mobile = cursor.fetchone()
            if mobile:
                lst_persons.append(mobile)
            else:
                break

        for dt in lst_persons:
            if name == dt[1]:
                cursor.execute(postgres_insert_photo, (book, dt[0]))
                db.commit()
                break
        else:
            postgres_insert_person = """INSERT INTO person(title) values(%s)"""
            cursor.execute(postgres_insert_person, (name,))
            db.commit()

            cursor.execute("select max(id) from person")
            cursor.execute(postgres_insert_photo, (book, cursor.fetchone()[0]))
            db.commit()

        count = cursor.rowcount
    except Exception as e:
        print(e)
    finally:
        if db:
            cursor.close()
            db.close()
            print('Соединение с DB закрыто петушок')

