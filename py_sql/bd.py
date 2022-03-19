import pymysql

db = pymysql.connect(host="localhost", user="root", password="1234", database="humanz")

cursor = db.cursor()

# cursor.execute("SELECT VERSION()")
#
# data = cursor.fetchone()
#
# print(f"Database version : {data} ")
#
# insert_dolzhnost_query = "INSERT INTO `humanz`.`new_table` (`id`, `ip`, `name`, `phone`) VALUES (8, '10.10.109.143', 'Nikitya2', '7(800)3334455');"
# # insert_sotrudnik_query = "DELETE FROM `humanz`.`new_table` WHERE `id`=8;"
#
# insert_sotrudnik_query = "UPDATE `humanz`.`new_table` SET `name`='Pasha' WHERE `id`=2;"
# cursor.execute(insert_dolzhnost_query)
# cursor.execute(insert_sotrudnik_query)
# db.commit()

# query = "SELECT `dolzhnost`.`name_dolzhnost`, `sotrudnik`.`fio` FROM `lesson`.`dolzhnost` INNER JOIN `lesson`.`sotrudnik` ON `sotrudnik`.`dolzhnost_id_dolzhnost` = `dolzhnost`.`id_dolzhnost`;"
# cursor.execute(query)
# data = cursor.fetchall()
#
# print(data)
#

# cursor.execute("SELECT * FROM `humanz`.`new_table` WHERE `name` = 'Nikita;")
cursor.execute("SELECT * FROM `humanz`.`new_table`")
data = cursor.fetchall()
for i in data:
    print(i)
# print(data)

# cursor.execute("SELECT * FROM `lesson`.`dolzhnost`")
# data = cursor.fetchall()
# print(data)

# insert_dolzhnost_query = "INSERT INTO `humanz`.`new_table` (`name`, `id`, `ip`) VALUES (2, 'Menager', 10000);"
# cursor.execute(insert_dolzhnost_query)
# db.commit()


db.close()
