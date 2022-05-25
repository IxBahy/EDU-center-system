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
    my_cursor.execute('call add_course(%s,%s,%s);',
                      (name, id, price))
    db.commit()


def add_student(f_name, l_name, phone, gender, c_id, t_id):
    my_cursor.execute('call add_student(%s,%s,%s,%s,%s,%s);',
                      (f_name, l_name, phone, gender, c_id, t_id))
    db.commit()


def add_assistant(t_id, f_name, l_name, salary, gender):
    my_cursor.execute('call add_assistant(%s,%s,%s,%s,%s);',
                      (t_id, f_name, l_name, salary, gender))
    db.commit()


def get_std_count(id):
    my_cursor.execute('call get_std_count(%s);', (id))
    result = my_cursor.fetchone
    return


def get_courses_ids():
    my_cursor.execute('Select id from courses;')
    result = my_cursor.fetchall()
    return result


def get_teacher_ids():
    my_cursor.execute('Select id from teachers;')
    result = my_cursor.fetchall()
    return result


def get_teacher_data(id):
    my_cursor.execute(
        'Select first_name,last_name,course from teachers where id=%s;', (id))
    result = my_cursor.fetchone()
    return result


def get_course_id_by_name(name):
    my_cursor.execute('Select id from courses where name = %s ;', (name))
    result = my_cursor.fetchone()
    return result


def update_teacher(t_id, f_name, l_name, c_id):
    my_cursor.execute('call update_teacher(%s,%s,%s,%s);',
                      (t_id, f_name, l_name, c_id))
    db.commit()


def delete_teacher(t_id):
    my_cursor.execute('delete from teachers where id = %s ;', (t_id))
    db.commit()


def update_course(id, new_id, name, price):
    my_cursor.execute('call update_course(%s,%s,%s,%s);',
                      (id, new_id, name, price))
    db.commit()


def get_course_data(id):
    my_cursor.execute(
        'Select name,price from courses where id=%s;', (id))
    result = my_cursor.fetchone()
    return result


def delete_course(id):
    my_cursor.execute('delete from courses where id = %s ;', (id))
    db.commit()


def delete_assistant(f_name, l_name):
    my_cursor.execute(
        'delete from assistants where first_name = %s and last_name=%s;', (f_name, l_name))
    db.commit()


def get_assistant_name():
    my_cursor.execute('select first_name, last_name from assistants;')
    result = my_cursor.fetchall()
    return result


def get_student_data(id):
    my_cursor.execute(
        'select phone,gender,first_name,last_name from students where id = %s;', (id))
    result = my_cursor.fetchone()
    return result


def get_teacher_and_course_id(id):
    my_cursor.execute(
        'select c_id,t_id from student_course_teacher where s_id = %s;', (id))
    result = my_cursor.fetchone()
    return result


def update_student(id, f_name, l_name, t_id, phone, gender, c_id):
    my_cursor.execute('call update_student(%s,%s,%s,%s,%s,%s,%s);',
                      (id, f_name, l_name, t_id, phone, gender, c_id))
    db.commit()
