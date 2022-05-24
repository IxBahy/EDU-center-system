import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='2411',
    database='edu_db'
)


my_cursor = db.cursor()


def login_check(name):
    my_cursor.execute(
        'SELECT passwd FROM admins WHERE user_name=\''+name+"\'")
    result = my_cursor.fetchone()
    if result == None:
        return None
    else:
        return result[0]


def add_admin(name, email, passwd):
    my_cursor.execute('call add_admine(%s,%s,%s);', (
        name, email, passwd))
    db.commit()


def add_teacher(f_name, l_name, id, c_id):
    my_cursor.execute('call add_teacher(%s,%s,%s,%s);',
                      (f_name, l_name, id, c_id))
    db.commit()


def add_course(name, id, price):
    my_cursor.execute('call add_teacher(%s,%s,%s);',
                      (name, id, price))
    db.commit()


def add_student(f_name, l_name, phone, gender, c_id, t_id):
    my_cursor.execute('call add_teacher(%s,%s,%s,%s,%s,%s);',
                      (f_name, l_name, phone, gender, c_id, t_id))
    db.commit()


def edit_teacher(id):
    my_cursor.execute('call edit_teacher(%s);', (id))
    db.commit()


def get_std_count(id):
    my_cursor.execute('call get_std_count(%s);', (id))
    result = my_cursor.fetchone
    return


def get_courses_ids():
    my_cursor.execute('Select name from courses')
    result = my_cursor.fetchall()
    return result
