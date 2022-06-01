from cgitb import text
import oop_res
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QComboBox
import sys
import database as db
from database import my_cursor
import re
import pywhatkit as kit
import time
import pyautogui

# welcome window for the application


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
    # a button for each category  in the app

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
        self.fees_detailsButton.clicked.connect(self.open_fees_window)
        # self.fees_button.clicked.connect(self.open_fees_window)

    def close_function(self):
        self.close()
    # return to main window (welcome window)

    def back_function(self):
        self.close()
        self.main = MainWindow()
        self.main.show()
    # open the student add window

    def open_add_window(self):
        self.close()
        self.main = student_add_window()
        self.main.show()
    # open the student edit window

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
    # back to main window

    def back_function(self):
        self.close()
        self.main = MainWindow()
        self.main.show()
    # open teacher add window

    def open_add_window(self):
        self.close()
        self.main = teacher_add_window()
        self.main.show()
    # open the teacher edit window

    def open_edit_window(self):
        self.close()
        self.main = teacher_edit_window()
        self.main.show()
    # open the add assistant window

    def open_assistant_window(self):
        self.close()
        self.main = assistant_add_window()
        self.main.show()
    # open teacher stats window

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
    # back to main window

    def back_function(self):
        self.close()
        self.main = MainWindow()
        self.main.show()
    # open the course add window

    def open_add_window(self):
        self.close()
        self.main = course_add_window()
        self.main.show()
    # open the course edit window

    def open_edit_window(self):
        self.close()
        self.main = course_edit_window()
        self.main.show()
    # open course stats window

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
        # add all the IDs in the courses table to the combo box
        for id in db.get_courses_ids():
            for value in id:
                self.course_Id.addItem(value)
        self.note_msg.setText('')
        # call the load list function
        self.load_list()

    def load_list(self):
        # clear the list first so if called will have no duplicates
        self.teachers_List.clear()
        for result in db.teacher_info():
            self.teachers_List.addItem(result[0])

    def add(self):
        # add a new teacher (read data in text lines and validating it)
        f_name = self.first_Name.text()
        l_name = self.last_Name.text()
        t_id = self.id.text()
        c_id = self.course_Id.currentText()
        v_name = False
        v_course = False
        v_id = False
        v_duplication = False

        if db.get_teacher_data((t_id,)) is None:
            # check if ID already exsist
            v_duplication = True
        else:
            self.note_msg.setText('ID already exsist')
        if len(f_name) == 0 or len(l_name) == 0:
            self.note_msg.setText('input the name pleas')
        else:
            v_name = True
        if c_id == 'choose a course':
            self.note_msg.setText('select a course pleas')
        else:
            v_course = True
        if len(t_id) == 0:
            self.note_msg.setText('input an ID pleas')
        else:
            v_id = True
        if v_name and v_course and v_id and v_duplication:
            # call the add teacher stored procedure
            db.add_teacher(f_name, l_name, t_id, c_id)
            self.note_msg.setText('teacher added successfully')
            # update the list
            self.load_list()
            self.first_Name.setText('')
            self.last_Name.setText('')
            self.id.setText('')
            self.course_Id.setCurrentText('choose a course')

    def back_function(self):
        # back to teachers main window
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
        self.delete_Button.clicked.connect(self.delete)
        # add all teacher IDs to the combo box
        for t_id in db.get_teacher_ids():
            for t_value in t_id:
                self.teacher_Id_Box.addItem(t_value)
        # reset values
        self.note_msg.setText('')
        self.first_Name.setText('')
        self.last_Name.setText('')
        self.course_Id.setCurrentText('choose a course')
        # add all the course IDs to the combo box
        for id in db.get_courses_ids():
            for value in id:
                self.course_Id.addItem(value)
    # return to the teacher main window

    def back_function(self):
        self.close()
        self.main = teacher_main_window()
        self.main.show()

    def close_function(self):
        self.close()

    def get_teacher_data(self):
        id = (self.teacher_Id_Box.currentText(),)
        # call a queary that return the data we want to show about the teacher
        result = db.get_teacher_data(id)
        if result is not None:
            # if teacher exsist(for sure it will haha)
            # unpack the result
            f_name, l_name, course = result
            self.first_Name.setText(f_name)
            self.last_Name.setText(l_name)
            c_name = (course,)
            c_id = db.get_course_id_by_name(c_name)
            if c_id is not None:
                # extra security check (:p not needed as all values are selected from combo boxes but safty is better)
                self.course_Id.setCurrentText(c_id[0])
        else:
            self.note_msg.setText('choose a teacher ID')

    def update(self):
        # update teacher values by the new inserted ones
        t_id = self.teacher_Id_Box.currentText()
        f_name = self.first_Name.text()
        l_name = self.last_Name.text()
        c_id = self.course_Id.currentText()
        v_name = False
        if len(f_name) == 0 or len(l_name) == 0:
            self.note_msg.setText('input the name pleas')
        else:
            v_name = True
        if v_name:
            db.update_teacher(t_id, f_name, l_name, c_id)
            self.note_msg.setText('teacher updated successfully')
            # update the combo box values
            self.teacher_Id_Box.clear()
            self.teacher_Id_Box.addItem('choose a teacher')
            for id in db.get_teacher_ids():
                for value in id:
                    self.teacher_Id_Box.addItem(value)
            self.first_Name.setText('')
            self.last_Name.setText('')
            self.course_Id.setCurrentText('choose a course')

    def delete(self):
        # delete the selected ID from the combo box
        t_id = (self.teacher_Id_Box.currentText(),)
        if self.teacher_Id_Box.currentText() != 'choose a teacher':
            db.delete_teacher(t_id)
            self.note_msg.setText('teacher deleted successfully')
            # update the combo box values
            self.teacher_Id_Box.clear()
            self.teacher_Id_Box.addItem('choose a teacher')
            for id in db.get_teacher_ids():
                for value in id:
                    self.teacher_Id_Box.addItem(value)
            self.first_Name.setText('')
            self.last_Name.setText('')
            self.course_Id.setCurrentText('choose a course')
        else:
            self.note_msg.setText('choose a teacher')


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
        self.delete_Button.clicked.connect(self.delete)
        # add all the assistants name to the combo box
        for names in db.get_assistant_name():
            full_name = ''
            for value in names:
                full_name += value+' '
            self.assistant_box.addItem(full_name)
        # add all the teacher IDs to the combo box
        for t_id in db.get_teacher_ids():
            for t_value in t_id:
                self.teacher_Id_Box.addItem(t_value)
        self.note_msg.setText('')
    # return to the teachers main window

    def back_function(self):
        self.close()
        self.main = teacher_main_window()
        self.main.show()

    def close_function(self):
        self.close()

    def delete(self):
        if self.assistant_box.currentText() == 'choose an assistant':
            self.note_msg.setText('choose an assistant')

        else:
            name = (self.assistant_box.currentText()).split()
            f_name = name[0]
            l_name = name[1]
            db.delete_assistant(f_name, l_name)
            self.note_msg.setText('assistant deleted successfully')
            self.assistant_box.clear()
            self.assistant_box.addItem("choose an assistant")
            for names in db.get_assistant_name():
                full_name = ''
                for value in names:
                    full_name += value+' '
                self.assistant_box.addItem(full_name)

    def add(self):
        # adding a new assistant
        f_name = self.first_Name.text()
        l_name = self.last_Name.text()
        salary = self.salary.text()
        gender = self.gender.currentText()
        t_id = self.teacher_Id_Box.currentText()
        v_name = False
        v_salary = False
        v_gender = False
        v_t_id = False
        v_duplication = False
        if db.assistant_check(f_name, l_name) is None:
            v_duplication = True
        else:
            self.note_msg.setText('assistant already exsist')
        if len(f_name) == 0 or len(l_name) == 0:
            self.note_msg.setText('please input the name field')
        else:
            v_name = True

        if len(gender) == 0:
            self.note_msg.setText('please input the gender field')
        else:
            v_gender = True

        if len(salary) == 0:
            self.note_msg.setText('please input the salary field')
        else:
            if salary.strip().isdigit():
                v_salary = True
            else:
                self.note_msg.setText('wrong value type in salary field')

        if t_id == 'choose a teacher':
            self.note_msg.setText('please select a teacher')
        else:
            v_t_id = True

        if v_name and v_duplication and v_t_id and v_salary and v_gender:
            db.add_assistant(t_id, f_name, l_name, salary, gender)
            self.note_msg.setText('assistant added successfully')
        # update the combo box
        self.assistant_box.clear()
        self.assistant_box.addItem("choose an assistant")
        for names in db.get_assistant_name():
            full_name = ''
            for value in names:
                full_name += value+' '
            self.assistant_box.addItem(full_name)


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
        self.show_Button.clicked.connect(self.show_function)
        # add the Ids to the combo box
        for t_id in db.get_teacher_ids():
            for t_value in t_id:
                self.teacher_Id_Box.addItem(t_value)

    def show_function(self):
        # show teacher stats based by the ID using sql queries
        id = (self.teacher_Id_Box.currentText(),)
        assistant_number = db.get_assistant_count(id)
        self.assistants_Count.setText(str(assistant_number))
        student_number = db.number_of_students(id)
        self.students_Count.setText(str(student_number))
        total_salaries = db.total_Salaries(id)
        self.total_Salaries.setText(str(total_salaries))
        total_income = db.total_income(id)
        self.total_Income.setText(str(total_income))

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
       # making the dependant combo boxes
        self.combo1 = self.findChild(QComboBox, 'teacher_Id_Box')
        self.combo2 = self.findChild(QComboBox, 'course_Id')
        # adding all values with associated values to the course combo box "teachers can have one course but a course can have many teachers"
        for c_id in db.get_courses_ids():
            for c_value in c_id:
                items = []
                for item in self.get_t_ids(c_value):
                    items += item
                self.combo2.addItem(c_value, items)
        # adding all values with associated values to the teacher combo box
        for t_id in db.get_teacher_ids():
            for t_value in t_id:
                self.combo1.addItem(t_value, self.get_c_ids(t_value))

        self.combo1.activated.connect(self.t_clicker)
        self.combo2.activated.connect(self.c_clicker)
        # call the function to fill the students list
        self.fill_list()

    def fill_list(self):
        # same way as othe fill_list functions
        self.students_List.clear()
        for result in db.student_info():
            self.students_List.addItem(result[0])

    def t_clicker(self, index):
        # first base conditons: if the course value is none:
        if self.course_Id.currentText() == 'choose a course':
            # 1:if the value inputed in theacher is not none and course is none:
            if self.teacher_Id_Box.currentText() != 'choose a teacher':
                # we clear the courses and fill only the associated values of the teacher ID we inputed
                self.combo2.clear()
                self.combo2.addItem('choose a course', 'choose a teacher')
                self.combo2.addItem(self.combo1.itemData(index))
            # 2: if we click on none and course is none:
            elif self.teacher_Id_Box.currentText() == 'choose a teacher':
                # we clear both and add all items to both the combo boxes
                self.combo2.clear()
                self.combo2.addItem('choose a course', 'choose a teacher')
                for c_id in db.get_courses_ids():
                    for c_value in c_id:
                        items = []
                        for item in self.get_t_ids(c_value):
                            items += item
                    self.combo2.addItem(c_value, items)

        # base 2: if course is not none:
        else:
            # 1: if we click on none and course is not none:
            if self.teacher_Id_Box.currentText() == 'choose a teacher':
                # we clear the course box and add all items to it and make the current text the same as the one before the clear
                # beacuse i dont want to reset both u cant just make it a pass or it will input some empty items to the text box
                value = self.combo2.currentText()
                self.combo2.clear()
                self.combo2.addItem('choose a course', 'choose a teacher')
                # we add all the courses beacuse none is the input from teachers
                for c_id in db.get_courses_ids():
                    for c_value in c_id:
                        items = []
                        for item in self.get_t_ids(c_value):
                            items += item
                        self.combo2.addItem(c_value, items)
                # clear the teachers box
                self.combo1.clear()
                self.combo1.addItem('choose a teacher', 'choose a course')
                # add all the values of teachers
                for t_id in db.get_teacher_ids():
                    for t_value in t_id:
                        self.combo1.addItem(t_value, self.get_c_ids(t_value))
                self.combo2.setCurrentText(value)
                # call the course function so the original state will remain the same
                self.c_clicker(self.combo2.currentIndex())
                # all this equal that the none input do nothing if the course box is not none
            # 2:if we click on a value and cours is not none
            elif self.teacher_Id_Box.currentText() != 'choose a teacher':
                # the following code will cause the value in the course box will be only the course that the IDs in the teacher box is avilabe for
                #  so now both the teacher values and couse will math and no errors will happen
                box1_value = self.combo1.currentText()
                # getting all the IDs in the teacher box so we can add the agine after the clear
                values = [self.combo1.itemText(i)
                          for i in range(self.combo1.count())]
                box2_value = self.combo2.currentText()
                self.combo1.clear()
                self.combo1.addItem('choose a teacher', 'choose a course')
                # add the same values as before so the teachers box will remain the same
                for value in values:
                    if value != 'choose a teacher':
                        self.combo1.addItem(value, self.get_c_ids(value))
                self.combo1.setCurrentText(box1_value)
                # we clear the courses box
                self.combo2.clear()
                self.combo2.addItem('choose a course', 'choose a teacher')
                self.combo2.setCurrentText('choose a course')
                # add the course associated with the index of the item selected in the teachers box (all will have the same course ID but you must do this so the boxes will be dependant )
                self.t_clicker(self.combo1.currentIndex())
                self.combo2.setCurrentText(box2_value)

    def c_clicker(self, index):
        # same process as the t_clicker function
        if self.teacher_Id_Box.currentText() == 'choose a teacher':
            if self.course_Id.currentText() != 'choose a course':
                self.combo1.clear()
                self.combo1.addItem('choose a teacher', 'choose a course')
                self.combo1.addItems(self.combo2.itemData(index))
            elif self.course_Id.currentText() == 'choose a course':
                self.combo1.clear()
                self.combo1.addItem('choose a teacher', 'choose a course')
                for t_id in db.get_teacher_ids():
                    for t_value in t_id:
                        self.combo1.addItem(t_value, self.get_c_ids(t_value))
        else:
            if self.course_Id.currentText() == 'choose a course':
                value = self.combo1.currentText()
                self.combo1.clear()
                self.combo1.addItem('choose a teacher', 'choose a course')
                for t_id in db.get_teacher_ids():
                    for t_value in t_id:
                        self.combo1.addItem(t_value, self.get_c_ids(t_value))
                self.combo2.clear()
                self.combo2.addItem('choose a course', 'choose a teacher')
                for c_id in db.get_courses_ids():
                    for c_value in c_id:
                        items = []
                        for item in self.get_t_ids(c_value):
                            items += item
                        self.combo2.addItem(c_value, items)
                self.combo1.setCurrentText(value)
                self.t_clicker(self.combo1.currentIndex())

            elif self.course_Id.currentText() != 'choose a course':
                items = []
                box1_value = self.combo1.currentText()
                box2_value = self.combo2.currentText()
                self.combo2.clear()
                self.combo2.addItem('choose a course', 'choose a teacher')
                for item in self.get_t_ids(box2_value):
                    items += item
                self.combo2.addItem(box2_value, items)
                self.combo2.setCurrentText(box2_value)
                self.combo1.clear()
                self.combo1.addItem('choose a teacher', 'choose a course')
                self.combo1.setCurrentText('choose a teacher')
                self.c_clicker(self.combo2.currentIndex())
                self.combo1.setCurrentText(box1_value)

    def back_function(self):
        self.close()
        self.main = student_main_window()
        self.main.show()

    def close_function(self):
        self.close()

    def add(self):
        # adding a student "id is auto incremented "
        f_name = self.first_Name.text()
        l_name = self.last_Name.text()
        phone = self.phone.text()
        c_id = self.course_Id.currentText()
        t_id = self.teacher_Id_Box.currentText()
        gender = self.gender.currentText()
        v_name = False
        v_phone = False
        v_gender = False
        v_check_box = False
        v_duplication = False
        checker = db.student_check(f_name, l_name, phone, gender, c_id)
        if checker is None:
            v_duplication = True
        elif checker[0] == c_id and checker[1] == t_id:
            self.note_msg.setText('student already exsist')
        else:
            v_duplication = True

        if len(f_name) == 0 or len(l_name) == 0:
            self.note_msg.setText('please input the student field')
        else:
            v_name = True
        if len(phone) == 0:
            self.note_msg.setText('please input the phone field')
        elif len(phone) < 10 or len(phone) > 11:
            self.note_msg.setText('please input a valid phone number')
        else:
            if phone.isdigit():
                v_phone = True
            else:
                self.note_msg.setText('please input a valid phone number')

        if gender == 'choose a gender':
            self.note_msg.setText('please choose a gender')
        else:
            v_gender = True
        if t_id == 'choose a teacher' or c_id == 'choose a course':
            self.note_msg.setText('please choose the IDs')
        else:
            v_check_box = True
        if v_check_box and v_name and v_phone and v_gender and v_duplication:
            db.add_student(f_name, l_name, phone, gender, c_id, t_id)
            self.note_msg.setText('student added successfully')
            # update the student list
            self.fill_list()
            self.first_Name.setText('')
            self.last_Name.setText('')
            self.phone.setText('')
            self.gender.setCurrentText('choose a gender')
            self.teacher_Id_Box.setCurrentText('choose a teacher')
            self.course_Id.setCurrentText('choose a course')

    def get_c_ids(self, value):
        # getting the course associated with the teacher ID passed in the parameter
        result = db.get_c_ids((value,))
        if result is not None:
            return result[0]
        else:
            pass

    def get_t_ids(self, value):
        # getting the teachers associated with the course ID passed in the parameter
        result = db.get_t_ids((value,))
        if result is not None:
            return result
        else:
            pass


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
        self.edit_Button.clicked.connect(self.get_data)
        self.delete_Button.clicked.connect(self.delete)
        self.update_Button.clicked.connect(self.update)
        # process same as above
        self.combo1 = self.findChild(QComboBox, 'teacher_Id_Box')
        self.combo2 = self.findChild(QComboBox, 'course_Id')
        for c_id in db.get_courses_ids():
            for c_value in c_id:
                items = []
                for item in self.get_t_ids(c_value):
                    items += item
                self.combo2.addItem(c_value, items)

        for t_id in db.get_teacher_ids():
            for t_value in t_id:
                self.combo1.addItem(t_value, self.get_c_ids(t_value))

        self.combo1.activated.connect(self.t_clicker)
        self.combo2.activated.connect(self.c_clicker)

    def t_clicker(self, index):
        if self.course_Id.currentText() == 'choose a course':
            if self.teacher_Id_Box.currentText() != 'choose a teacher':
                self.combo2.clear()
                self.combo2.addItem('choose a course', 'choose a teacher')
                self.combo2.addItem(self.combo1.itemData(index))
            elif self.teacher_Id_Box.currentText() == 'choose a teacher':
                self.combo2.clear()
                self.combo2.addItem('choose a course', 'choose a teacher')
                for c_id in db.get_courses_ids():
                    for c_value in c_id:
                        items = []
                        for item in self.get_t_ids(c_value):
                            items += item
                    self.combo2.addItem(c_value, items)

        else:
            if self.teacher_Id_Box.currentText() == 'choose a teacher':
                value = self.combo2.currentText()
                self.combo2.clear()
                self.combo2.addItem('choose a course', 'choose a teacher')
                for c_id in db.get_courses_ids():
                    for c_value in c_id:
                        items = []
                        for item in self.get_t_ids(c_value):
                            items += item
                        self.combo2.addItem(c_value, items)
                self.combo1.clear()
                self.combo1.addItem('choose a teacher', 'choose a course')
                for t_id in db.get_teacher_ids():
                    for t_value in t_id:
                        self.combo1.addItem(t_value, self.get_c_ids(t_value))
                self.combo2.setCurrentText(value)
                self.c_clicker(self.combo2.currentIndex())
            elif self.teacher_Id_Box.currentText() != 'choose a teacher':
                box1_value = self.combo1.currentText()
                values = [self.combo1.itemText(i)
                          for i in range(self.combo1.count())]
                box2_value = self.combo2.currentText()
                self.combo1.clear()
                self.combo1.addItem('choose a teacher', 'choose a course')
                for value in values:
                    if value != 'choose a teacher':
                        self.combo1.addItem(value, self.get_c_ids(value))
                self.combo1.setCurrentText(box1_value)
                self.combo2.clear()
                self.combo2.addItem('choose a course', 'choose a teacher')
                self.combo2.setCurrentText('choose a course')
                self.t_clicker(self.combo1.currentIndex())
                self.combo2.setCurrentText(box2_value)

    def c_clicker(self, index):
        if self.teacher_Id_Box.currentText() == 'choose a teacher':
            if self.course_Id.currentText() != 'choose a course':
                self.combo1.clear()
                self.combo1.addItem('choose a teacher', 'choose a course')
                self.combo1.addItems(self.combo2.itemData(index))
            elif self.course_Id.currentText() == 'choose a course':
                self.combo1.clear()
                self.combo1.addItem('choose a teacher', 'choose a course')
                for t_id in db.get_teacher_ids():
                    for t_value in t_id:
                        self.combo1.addItem(t_value, self.get_c_ids(t_value))
        else:
            if self.course_Id.currentText() == 'choose a course':
                value = self.combo1.currentText()
                self.combo1.clear()
                self.combo1.addItem('choose a teacher', 'choose a course')
                for t_id in db.get_teacher_ids():
                    for t_value in t_id:
                        self.combo1.addItem(t_value, self.get_c_ids(t_value))
                self.combo2.clear()
                self.combo2.addItem('choose a course', 'choose a teacher')
                for c_id in db.get_courses_ids():
                    for c_value in c_id:
                        items = []
                        for item in self.get_t_ids(c_value):
                            items += item
                        self.combo2.addItem(c_value, items)
                self.combo1.setCurrentText(value)
                self.t_clicker(self.combo1.currentIndex())
            elif self.course_Id.currentText() != 'choose a course':
                items = []
                box1_value = self.combo1.currentText()
                box2_value = self.combo2.currentText()
                self.combo2.clear()
                self.combo2.addItem('choose a course', 'choose a teacher')
                for item in self.get_t_ids(box2_value):
                    items += item
                self.combo2.addItem(box2_value, items)
                self.combo2.setCurrentText(box2_value)
                self.combo1.clear()
                self.combo1.addItem('choose a teacher', 'choose a course')
                self.combo1.setCurrentText('choose a teacher')
                self.c_clicker(self.combo2.currentIndex())
                self.combo1.setCurrentText(box1_value)

    def get_c_ids(self, value):
        result = db.get_c_ids((value,))
        if result is not None:
            return result[0]
        else:
            pass

    def get_t_ids(self, value):
        result = db.get_t_ids((value,))
        if result is not None:
            return result
        else:
            pass

    def back_function(self):
        self.close()
        self.main = student_main_window()
        self.main.show()

    def close_function(self):
        self.close()

    def get_data(self):
        # get the student data by its ID
        id = (self.id.text(),)
        result = db.get_student_data(id)
        if result is not None:
            phone, gender, f_name, l_name, = result
            c_id, t_id = db.get_teacher_and_course_id(id)
            course_id = (c_id,)
            teacher_id = (t_id,)
            self.first_Name.setText(f_name)
            self.last_Name.setText(l_name)
            self.phone.setText(str(phone))
            self.gender.setCurrentText(gender)
            self.teacher_Id_Box.setCurrentText(teacher_id[0])
            self.course_Id.setCurrentText(course_id[0])
        else:
            self.note_msg.setText('please input a valid student ID')

    def update(self):
        # update the student with the new data
        id = self.id.text()
        f_name = self.first_Name.text()
        l_name = self.last_Name.text()
        phone = self.phone.text()
        gender = self.gender.currentText()
        t_id = self.teacher_Id_Box.currentText()
        c_id = self.course_Id.currentText()
        v_name = False
        v_phone = False
        v_gender = False
        v_check_box = False

        if len(f_name) == 0 or len(l_name) == 0:
            self.note_msg.setText('please input the name fields')
        else:
            v_name = True
        if len(phone) == 0:
            self.note_msg.setText('please input the phone field')
        elif len(phone) < 10 or len(phone) > 11:
            self.note_msg.setText('please input a valid phone number')
        else:
            if phone.isdigit():
                v_phone = True
            else:
                self.note_msg.setText('please input a valid phone number')
        if gender == 'choose a gender':
            self.note_msg.setText('please choose a gender')
        else:
            v_gender = True
        if t_id == 'choose a teacher' or c_id == 'choose a course':
            self.note_msg.setText('please choose the ID fields')
        else:
            v_check_box = True
        if v_check_box and v_name and v_phone and v_gender:
            db.update_student(id, f_name, l_name, t_id, phone, gender, c_id)
            self.note_msg.setText('student updated successfully')
            self.first_Name.setText('')
            self.last_Name.setText('')
            self.phone.setText('')
            self.gender.setCurrentText('choose a gender')
            self.teacher_Id_Box.setCurrentText('choose a teacher')
            self.course_Id.setCurrentText('choose a course')

    def delete(self):
        # delete student by ID
        if len(self.id.text()) == 0:
            self.note_msg.setText('please input a valid student ID')
        else:
            id = (self.id.text(),)
            db.delete_student(id)
            self.note_msg.setText('student deleted successfully')
            self.first_Name.setText('')
            self.last_Name.setText('')
            self.phone.setText('')
            self.gender.setCurrentText('choose a gender')
            self.teacher_Id_Box.setCurrentText('choose a teacher')
            self.course_Id.setCurrentText('choose a course')
            self.id.setText('')


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
        self.switch_Button.clicked.connect(self.switch_fees)
        self.unpaid_Button.clicked.connect(self.unpay_fees)
        self.alert_Button.clicked.connect(self.send_alert)
        self.send_Button.clicked.connect(self.send_text_massage)

        self.fill_list()

    def fill_list(self):
        # same way as othe fill_list functions
        self.students_List.clear()
        for result in db.fees_info():
            self.students_List.addItem(result[0])

    def unpay_fees(self):
        id = ((self.id.text()),)
        db.unpay_fees(id)
        self.fill_list()
        self.note_msg.setText('fees switched to unpaid')

    def switch_fees(self):
        id = ((self.id.text()),)
        db.pay_fees(id)
        self.fill_list()
        phone = db.get_phone(id)
        self.note_msg.setText('fees switched to paid')
        self.send_paid(str(phone[0]))

    def back_function(self):
        self.close()
        self.main = student_main_window()
        self.main.show()

    def close_function(self):
        self.close()

    def send_alert(self):
        for phone in db.get_all_unpaid_phone():
            kit.sendwhatmsg_instantly(
                f'+20'+str(phone[0]), " Hello \n we would like to remind you that the fees for your course is not paid 'center name here'", 2, False)
            pyautogui.click()  # Clicks the bar
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'w')
        self.note_msg.setText('alerts sent to all unpaid students')

    def send_text_massage(self):
        text = self.message_text.toPlainText()
        for phone in db.get_all_phone():
            kit.sendwhatmsg_instantly(
                f'+20'+str(phone[0]), text, 2, False)
            pyautogui.click()  # Clicks the bar
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'w')
        self.note_msg.setText('message sent to all students')

    def send_paid(self, phone):
        kit.sendwhatmsg_instantly(
            f'+20'+phone, "course fees are successfully paid /n thanks", 2, False)
        pyautogui.click()  # Clicks the bar
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'w')


class course_add_window(QMainWindow):
    # process is the same as any add class
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
        self.fill_list()

    def fill_list(self):
        self.courses_List.clear()
        for result in db.course_info():
            self.courses_List.addItem(result[0])

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
        v_name = False
        v_id = False
        v_price = False
        v_duplication = False

        if db.get_course_data((id,)) is None:
            v_duplication = True
        else:
            self.note_msg.setText('ID already exsist')
        if len(name) == 0:
            self.note_msg.setText('input the name field please')
        else:
            v_name = True
        if len(id) == 0:
            self.note_msg.setText('input the ID field please')
        else:
            v_id = True
        if len(price) == 0:
            self.note_msg.setText('input the price field please')
        else:
            if price.strip().isdigit():
                v_price = True
            else:
                self.note_msg.setText('wrong value type in price field')
        if v_name and v_id and v_price and v_duplication:
            db.add_course(name, id, price)
            self.note_msg.setText('course added successfully')
            self.name.setText('')
            self.price.setText('')
            self.id.setText('')
            self.fill_list()


class course_edit_window(QMainWindow):
    # process is the same as any edit window
    def __init__(self):
        super(course_edit_window, self).__init__()
        self.setupUi()

    def setupUi(self):
        loadUi(r'UIs\\edit_c.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(self.close_function)
        self.BackButton.clicked.connect(self.back_function)
        self.update_Button.clicked.connect(self.update)
        self.edit_Button.clicked.connect(self.edit_data)
        self.delete_Button.clicked.connect(self.delete)

        for id in db.get_courses_ids():
            for value in id:
                self.course_Id.addItem(value)
        self.note_msg.setText('')
        self.name.setText('')
        self.price.setText('')

    def back_function(self):
        self.close()
        self.main = course_main_window()
        self.main.show()

    def close_function(self):
        self.close()

    def edit_data(self):
        id = (self.course_Id.currentText(),)
        result = db.get_course_data(id)
        if result is not None:
            name, price = result
            self.name.setText(name)
            self.price.setText(str(price))

        else:
            self.note_msg.setText('choose a valid ID')

    def update(self):
        name = self.name.text()
        id = self.course_Id.currentText()
        price = self.price.text()
        new_id = self.new_id.text()
        v_name = False
        v_id = False
        v_price = False
        if len(name) == 0:
            self.note_msg.setText('please input the user field')
        else:
            v_name = True
        if len(new_id) == 0 or id == 'choose a course':
            self.note_msg.setText('please check the ID fields')
        else:
            v_id = True
        if len(price) == 0:
            self.note_msg.setText('please input the price field')
        else:
            if price.strip().isdigit():
                v_price = True
            else:
                self.note_msg.setText('wrong value type in price field')
                print(type(price))

        if v_name and v_price and v_id:
            db.update_course(id, new_id, name, price)
            self.note_msg.setText('course updated successfully')
            self.course_Id.clear()
            self.course_Id.addItem('choose a course')
            for id in db.get_courses_ids():
                for value in id:
                    self.course_Id.addItem(value)
            self.name.setText('')
            self.price.setText('')

    def delete(self):
        if self.course_Id.currentText() != 'choose a course':
            id = (self.course_Id.currentText(),)
            db.delete_course(id)
            self.note_msg.setText('course deleted successfully')
            self.course_Id.clear()
            self.course_Id.addItem('choose a course')
            for id in db.get_courses_ids():
                for value in id:
                    self.course_Id.addItem(value)
            self.name.setText('')
            self.price.setText('')

        else:
            self.note_msg.setText('choose a valid ID')


class course_details_window(QMainWindow):
    # process is the same as the teacher stats window
    def __init__(self):
        super(course_details_window, self).__init__()
        self.setupUi()

    def setupUi(self):
        loadUi(r'UIs\\course_details.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(self.close_function)
        self.BackButton.clicked.connect(self.back_function)
        self.show_Button.clicked.connect(self.show_function)
        for id in db.get_courses_ids():
            for value in id:
                self.course_Id.addItem(value)

    def show_function(self):
        id = (self.course_Id.currentText(),)
        enrolements = db.course_enrollment(id)
        self.enrol_Number.setText(str(enrolements))
        teachers_number = db.get_teacher_count(id)
        self.teachers_Count.setText(str(teachers_number))
        course_income = db.total_course_income(id)
        self.total_Income.setText(str(course_income))

    def back_function(self):
        self.close()
        self.main = course_main_window()
        self.main.show()

    def close_function(self):
        self.close()
