import oop_res
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
import sys
import database as db
from database import my_cursor
import re


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        loadUi('UIs\welcome window.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(self.close_function)
        self.TeacherButton.clicked.connect(self.open_teacher_window)
        self.StudentButton.clicked.connect(self.open_student_window)
        self.CoursesButton.clicked.connect(self.open_course_window)

    def open_teacher_window(self):
        self.close()
        self.main = teacher_main_window()
        self.main.show()

    def open_student_window(self):
        self.close()
        self.main = student_main_window()
        self.main.show()

    def open_course_window(self):
        self.close()
        self.main = course_main_window()
        self.main.show()

    def close_function(self):
        self.close()


class student_main_window(QMainWindow):
    def __init__(self):
        super(student_main_window, self).__init__()
        self.setupUi()

    def setupUi(self):
        loadUi('UIs\students_1ui.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(self.close_function)
        self.BackButton.clicked.connect(self.back_function)
        self.add_studentButton.clicked.connect(self.open_add_window)
        self.edit_studentButton.clicked.connect(self.open_edit_window)
        self.fees_button.clicked.connect(self.open_fees_window)

    def close_function(self):
        self.close()

    def back_function(self):
        self.close()
        self.main = MainWindow()
        self.main.show()

    def open_add_window(self):
        self.close()
        self.main = student_add_window()
        self.main.show()

    def open_edit_window(self):
        self.close()
        self.main = student_edit_window()
        self.main.show()

    def open_fees_window(self):
        self.close()
        self.main = fees_window()
        self.main.show()


class teacher_main_window(QMainWindow):
    def __init__(self):
        super(teacher_main_window, self).__init__()
        self.setupUi()

    def setupUi(self):
        loadUi('UIs\Teachers_1.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(self.close_function)
        self.BackButton.clicked.connect(self.back_function)
        self.Add_teacherButton.clicked.connect(self.open_add_window)
        self.edit_TeacherButton.clicked.connect(self.open_edit_window)
        self.add_assistantButton.clicked.connect(self.open_assistant_window)
        self.stats_Button.clicked.connect(self.open_stats_window)

    def close_function(self):
        self.close()

    def back_function(self):
        self.close()
        self.main = MainWindow()
        self.main.show()

    def open_add_window(self):
        self.close()
        self.main = teacher_add_window()
        self.main.show()

    def open_edit_window(self):
        self.close()
        self.main = teacher_edit_window()
        self.main.show()

    def open_assistant_window(self):
        self.close()
        self.main = assistant_add_window()
        self.main.show()

    def open_stats_window(self):
        self.close()
        self.main = teacher_stats_window()
        self.main.show()


class course_main_window(QMainWindow):
    def __init__(self):
        super(course_main_window, self).__init__()
        self.setupUi()

    def setupUi(self):
        loadUi('UIs\courses_1ui.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(self.close_function)
        self.BackButton.clicked.connect(self.back_function)
        self.Add_Button.clicked.connect(self.open_add_window)
        self.edit_Button.clicked.connect(self.open_edit_window)
        self.detailsButton.clicked.connect(self.open_details_window)

    def close_function(self):
        self.close()

    def back_function(self):
        self.close()
        self.main = MainWindow()
        self.main.show()

    def open_add_window(self):
        self.close()
        self.main = course_add_window()
        self.main.show()

    def open_edit_window(self):
        self.close()
        self.main = course_edit_window()
        self.main.show()

    def open_details_window(self):
        self.close()
        self.main = course_details_window()
        self.main.show()


class teacher_add_window(QMainWindow):
    def __init__(self):
        super(teacher_add_window, self).__init__()
        self.setupUi()

    def setupUi(self):
        loadUi(r'UIs\\add_t.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(self.close_function)
        self.BackButton.clicked.connect(self.back_function)
        self.add_Button.clicked.connect(self.add)
        for id in db.get_courses_ids():
            for value in id:
                self.course_Id.addItem(value)
        self.note_msg.setText('')

    def add(self):
        f_name = self.first_Name.text()
        l_name = self.last_Name.text()
        t_id = self.id.text()
        c_id = self.course_Id.currentText()
        db.add_teacher(f_name, l_name, t_id, c_id)
        self.note_msg.setText('teacher added successfully')

    def back_function(self):
        self.close()
        self.main = teacher_main_window()
        self.main.show()

    def close_function(self):
        self.close()


class teacher_edit_window(QMainWindow):
    def __init__(self):
        super(teacher_edit_window, self).__init__()
        self.setupUi()

    def setupUi(self):
        loadUi(r'UIs\\edit_t.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(self.close_function)
        self.BackButton.clicked.connect(self.back_function)
        self.edit_Button.clicked.connect(self.get_teacher_data)
        self.update_Button.clicked.connect(self.update)
        for t_id in db.get_teacher_ids():
            for t_value in t_id:
                self.teacher_Id_Box.addItem(t_value)
        self.note_msg.setText('')
        self.first_Name.setText('')
        self.last_Name.setText('')
        self.course_Id_Box.setCurrentText('choose a course')
        for id in db.get_courses_ids():
            for value in id:
                self.course_Id_Box.addItem(value)

    def back_function(self):
        self.close()
        self.main = teacher_main_window()
        self.main.show()

    def close_function(self):
        self.close()

    def get_teacher_data(self):
        id = (self.teacher_Id_Box.currentText(),)
        f_name, l_name, course = db.get_teacher_data(id)
        self.first_Name.setText(f_name)
        self.last_Name.setText(l_name)
        c_name = (course,)
        c_id = db.get_course_id_by_name(c_name)
        self.course_Id_Box.setCurrentText(c_id[0])

    def update(self):
        t_id = self.teacher_Id_Box.currentText()
        f_name = self.first_Name.text()
        l_name = self.last_Name.text()
        c_id = self.course_Id_Box.currentText()
        print(f_name, l_name, t_id, c_id)
        db.add_teacher(t_id, f_name, l_name, c_id)
        self.note_msg.setText('teacher updated successfully')


class assistant_add_window(QMainWindow):
    def __init__(self):
        super(assistant_add_window, self).__init__()
        self.setupUi()

    def setupUi(self):
        loadUi(r'UIs\\assistant_add.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(self.close_function)
        self.BackButton.clicked.connect(self.back_function)
        self.add_Button.clicked.connect(self.add)
        for t_id in db.get_teacher_ids():
            for t_value in t_id:
                self.teacher_Id_Box.addItem(t_value)
        self.note_msg.setText('')

    def back_function(self):
        self.close()
        self.main = teacher_main_window()
        self.main.show()

    def close_function(self):
        self.close()

    def add(self):
        f_name = self.first_Name.text()
        l_name = self.last_Name.text()
        salary = self.salary.text()
        gender = self.gender.text()
        t_id = self.teacher_Id_Box.currentText()
        db.add_assistant(t_id, f_name, l_name, salary, gender)
        self.note_msg.setText('assistant added successfully')


class teacher_stats_window(QMainWindow):
    def __init__(self):
        super(teacher_stats_window, self).__init__()
        self.setupUi()

    def setupUi(self):
        loadUi(r'UIs\\teacher_stats.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(self.close_function)
        self.BackButton.clicked.connect(self.back_function)

    def back_function(self):
        self.close()
        self.main = teacher_main_window()
        self.main.show()

    def close_function(self):
        self.close()


class student_add_window(QMainWindow):
    def __init__(self):
        super(student_add_window, self).__init__()
        self.setupUi()

    def setupUi(self):
        loadUi(r'UIs\\add_s.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(self.close_function)
        self.BackButton.clicked.connect(self.back_function)
        self.add_Button.clicked.connect(self.add)
        self.note_msg.setText('')
        for c_id in db.get_courses_ids():
            for c_value in c_id:
                self.course_Id.addItem(c_value)

        for t_id in db.get_teacher_ids():
            for t_value in t_id:
                self.teacher_Id_Box.addItem(t_value)

    def back_function(self):
        self.close()
        self.main = student_main_window()
        self.main.show()

    def close_function(self):
        self.close()

    def add(self):
        f_name = self.first_Name.text()
        l_name = self.last_Name.text()
        phone = self.phone.text()
        c_id = self.course_Id.currentText()
        t_id = self.teacher_Id_Box.currentText()
        gender = self.gender.text()
        db.add_student(f_name, l_name, phone, gender, c_id, t_id)
        self.note_msg.setText('student added successfully')


class student_edit_window(QMainWindow):
    def __init__(self):
        super(student_edit_window, self).__init__()
        self.setupUi()

    def setupUi(self):
        loadUi(r'UIs\\edit_s.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(self.close_function)
        self.BackButton.clicked.connect(self.back_function)

    def back_function(self):
        self.close()
        self.main = student_main_window()
        self.main.show()

    def close_function(self):
        self.close()


class fees_window(QMainWindow):
    def __init__(self):
        super(fees_window, self).__init__()
        self.setupUi()

    def setupUi(self):
        loadUi(r'UIs\\fees_table.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(self.close_function)
        self.BackButton.clicked.connect(self.back_function)

    def back_function(self):
        self.close()
        self.main = student_main_window()
        self.main.show()

    def close_function(self):
        self.close()


class course_add_window(QMainWindow):
    def __init__(self):
        super(course_add_window, self).__init__()
        self.setupUi()

    def setupUi(self):
        loadUi(r'UIs\\add_c.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(self.close_function)
        self.BackButton.clicked.connect(self.back_function)
        self.add_Button.clicked.connect(self.add)
        self.note_msg.setText('')

    def back_function(self):
        self.close()
        self.main = course_main_window()
        self.main.show()

    def close_function(self):
        self.close()

    def add(self):
        name = self.name.text()
        id = self.id.text()
        price = self.price.text()
        db.add_course(name, id, price)
        self.note_msg.setText('course added successfully')


class course_edit_window(QMainWindow):
    def __init__(self):
        super(course_edit_window, self).__init__()
        self.setupUi()

    def setupUi(self):
        loadUi(r'UIs\\edit_c.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(self.close_function)
        self.BackButton.clicked.connect(self.back_function)

    def back_function(self):
        self.close()
        self.main = course_main_window()
        self.main.show()

    def close_function(self):
        self.close()


class course_details_window(QMainWindow):
    def __init__(self):
        super(course_details_window, self).__init__()
        self.setupUi()

    def setupUi(self):
        loadUi(r'UIs\\course_details.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(self.close_function)
        self.BackButton.clicked.connect(self.back_function)

    def back_function(self):
        self.close()
        self.main = course_main_window()
        self.main.show()

    def close_function(self):
        self.close()
