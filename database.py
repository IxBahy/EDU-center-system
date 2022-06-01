import mysql.connector
# all the quearies used in the application are defined here
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


def delete_student(id):
    my_cursor.execute(
        'call delete_student(%s);', (id))
    my_cursor.execute('select count(s_id) from student_course_teacher')
    result_1 = my_cursor.fetchone()
    if result_1[0] is not None and result_1[0] > 0:
        my_cursor.execute(
            'alter table student_course_teacher auto_increment=%s;', ((result_1[0]+1,)))
        my_cursor.execute(
            'alter table students auto_increment=%s;', ((result_1[0]+1,)))
    elif result_1[0] == 0:
        my_cursor.execute(
            'alter table student_course_teacher auto_increment= 1 ;')
        my_cursor.execute(
            'alter table students auto_increment= 1 ;')
    db.commit()


def assistant_check(f_name, l_name):
    my_cursor.execute(
        'select * from assistants where first_name=%s and last_name=%s ;', (f_name, l_name))
    result = my_cursor.fetchone()
    return result


def get_c_ids(t_id):
    my_cursor.execute(
        'select id from courses where name=(select course from teachers where id = %s)', (t_id))
    result = my_cursor.fetchone()
    return result


def get_t_ids(c_id):
    my_cursor.execute(
        'select id from teachers where course=(select name from courses where id = %s)', (c_id))
    result = my_cursor.fetchall()
    return result


def get_assistant_count(id):
    my_cursor.execute(
        'select count(*) from assistants  where teacher_id =%s', (id))
    result = my_cursor.fetchone()
    if result is None:
        result = 0
        return result
    else:
        return result[0]


def get_teacher_count(c_id):
    my_cursor.execute(
        'select count(id) from teachers where course = (select name from courses where id= %s)', (c_id))
    result = my_cursor.fetchone()
    if result is None:
        result = 0
        return result
    else:
        return result[0]


def course_enrollment(c_id):
    my_cursor.execute(
        'select count(s_id) from student_course_teacher where c_id = %s ;', (c_id))
    result = my_cursor.fetchone()
    if result is None:
        result = 0
        return result
    else:
        return result[0]


def number_of_students(t_id):

    my_cursor.execute(
        'select count(s_id)  from student_course_teacher where t_id = %s;', (t_id))
    result = my_cursor.fetchone()
    if result is None:
        result = 0
        return result
    else:
        return result[0]


def total_Salaries(t_id):
    my_cursor.execute(
        'SELECT SUM(salary) from assistants where teacher_id = %s;', (t_id))
    result = my_cursor.fetchone()
    if result is None:
        result = 0
        return result
    else:
        return result[0]


def total_income(t_id):
    var = 0
    args = (t_id[0], var)
    result = my_cursor.callproc('TotalIncome', args)
    return result[1]


def total_course_income(c_id):
    var = 0
    args = (c_id[0], var)
    result = my_cursor.callproc('total_course_income', args)
    return result[1]


def teacher_info():
    sql = ('select concat("Name: ",teachers.first_name," ",teachers.last_name, ". ID: " ,teachers. id,". Course ID: ",(select courses.id where name=teachers.course)," ")\
         as TeacherInfo from teachers left join courses\
        on teachers.course=courses.name where courses.id is not null;')
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    return result


def course_info():
    sql = ('select concat("Name: ",name,". Price: ",price," . ID: ", id)  from courses;')
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    return result


def student_info():
    sql = ('select concat(students.id,"- Name: ",students.first_name," ",students.last_name,". Phone number: ",students.phone,", teacher ID: ",\
        (select student_course_teacher.t_id where s_id=students.id)," Course ID: ",(select student_course_teacher.c_id where s_id=students.id ))\
             from students inner join student_course_teacher on students.id=student_course_teacher.s_id ORDER BY students.id ;')
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    return result


def student_check(f_name, l_name, phone, gender, c_id):
    sql = ('select c_id,t_id from student_course_teacher where s_id= \
        (select id from students where phone=%s and gender=%s and first_name=%s and last_name=%s and course= (select name from courses where id=%s) );')
    my_cursor.execute(
        sql, (phone, gender, f_name, l_name, c_id))
    result = my_cursor.fetchone()
    return result


def fees_info():
    sql = ('select concat(id,"-Name:",first_name," ",last_name,", fees: ",paid) from students ORDER BY id')
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    return result


def pay_fees(id):
    sql = ('update students set paid=1 where id=(%s);')
    my_cursor.execute(sql, (id))
    db.commit()


def unpay_fees(id):
    sql = ('update students set paid=0 where id=(%s);')
    my_cursor.execute(sql, (id))
    db.commit()


def get_phone(id):
    my_cursor.execute('select phone from students where id=%s', (id))
    result = my_cursor.fetchone()
    return result


def get_all_unpaid_phone():
    my_cursor.execute('select phone from students where paid=0')
    result = my_cursor.fetchall()
    return result


def get_all_phone():
    my_cursor.execute('select phone from students')
    result = my_cursor.fetchall()
    return result
