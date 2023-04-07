import psqlpt
import numpy as np
db = psqlpt.create_connection('hackatonjasai', 'postgres', '', 'localhost', '5432')
cursor = db.cursor()

lst_encoding = []
cursor.execute("select encoding_vector, title from person inner join photo ON person.id=photo.person_id")
while True:
    mobile = cursor.fetchone()
    print(mobile)
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
print(data)