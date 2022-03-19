import pymysql

db = pymysql.connect(host="localhost", user="root", password="1234", database="humanz")

cursor = db.cursor()

with open('info.txt', 'rt') as f:
    for line in f:
        items = line[:-1].split(',')
        items[3] = items[3][1:]
        items[3] = items[3][:-1]

        name = items[0]
        id = int(items[1])
        ip = items[2]
        phone = items[3]

        query = f"INSERT INTO `humanz`.`new_table` (`id`, `ip`, `name`, `phone`) VALUES ({id}, '{name}', '{ip}', '{phone}');"
        cursor.execute(query)
        db.commit()
