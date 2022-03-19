import pymysql

import conf_db

db = pymysql.connect(host="localhost", user="root", password="1234", database="humanz")
# db = conf_db.db

cursor = db.cursor()

def db_write(id,name,ip,phone):
    my_query = f"INSERT INTO `humanz`.`new_table` (`id`, `ip`, `name`, `phone`) VALUES ({id}, '{name}', '{ip}', '{phone}');"
    cursor.execute(my_query)
    db.commit()

def db_delete(id):
    my_query = f"DELETE FROM `humanz`.`new_table` WHERE `id`={id};"
    cursor.execute(my_query)
    db.commit()

def db_update(id,name,ip,phone):
    my_query = f"UPDATE `humanz`.`new_table` SET `name`='{name}', `ip`='{ip}', `phone`='{phone}' WHERE `id`={id};"
    cursor.execute(my_query)
    db.commit()



def db_read():
    cursor.execute("SELECT * FROM `humanz`.`new_table`")
    data = cursor.fetchall()
    return data
# print(db_read())

def db_filter_by_name(name):
    cursor.execute(f"SELECT * FROM `humanz`.`new_table` WHERE `name` = '{name}';")
    data = cursor.fetchall()
    return data




def db_filter_by_name(name):
    cursor.execute(f"SELECT * FROM `humanz`.`new_table` WHERE `name` = '{name}';")
    data = cursor.fetchall()
    return data


def db_filter_by_id(id):
    cursor.execute(f"SELECT * FROM `humanz`.`new_table` WHERE `id` = '{id}';")
    data = cursor.fetchall()
    return data


def db_filter_by_id2(id,name):
    cursor.execute(f"SELECT * FROM `humanz`.`new_table` WHERE `id` = '{id}' and `id` = '{name}';")
    data = cursor.fetchall()
    return data

print(db_filter_by_id2("55","Pass"))
# ('Pass', 911, 'Pass', '55')

def db_filter_by_ip(ip):
    cursor.execute(f"SELECT * FROM `humanz`.`new_table` WHERE `ip` = '{ip}';")
    data = cursor.fetchall()
    return data


def db_filter_by_phone(phone):
    cursor.execute(f"SELECT * FROM `humanz`.`new_table` WHERE `phone` = '{phone}';")
    data = cursor.fetchall()
    return data



