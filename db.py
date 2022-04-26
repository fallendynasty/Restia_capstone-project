### INITIATING DATABASE ###
import sqlite3
import sql
import csv



class Table:
    def __init__(self, database, table):
        self.__database = database
        self.__table = table

    def import_csv(self, filename):
        with open (filename, 'r') as f:
            for record in csv.DictReader(f):
                self.insert(record)

    def execute(self, sql, values=""):
        with sqlite3.connect(self.__database) as conn:
            cur = conn.cursor()
            cur.execute(sql, values)
            result = []

            # RETRIEVING RESULTS
            # IF TYPE IS EMPTY, RETURN []
            loop = cur.fetchall()
            for rec in loop:
                result.append(rec)

            conn.commit()
            return result
            # conn.close() automatically

    def get_all(self):
        sql = f'SELECT * FROM {self.__table};'
        return self.execute(sql)

    def find(self, **kwargs):
        # kwargs is a dictionary of key = column name, value = value pairs
        kwargs.setdefault('column', '*')
        sql_condition = " WHERE "
        sql_values = []

        # CREATING CONDITIONAL STATEMENT
        if 'dic' in kwargs.keys(): # dict passed in
            for key, value in kwargs['dic'].items():
                if key != 'column':
                    sql_condition += f"{key} = ? AND "
                    if type(value) == str:
                        sql_values.append(value.upper()) # values in database are stored in uppercase
                    else:
                        sql_values.append(value)

        else: # not a dict passed in
            for key, value in kwargs.items():
                if key != 'column':
                    sql_condition += f"{key} = ? AND "
                    if type(value) == str:
                        sql_values.append(value.upper()) # values in database are stored in uppercase
                    else:
                        sql_values.append(value)

        # CREATING EXECUTABLE SQL
        sql = "SELECT " + kwargs["column"] + f" FROM {self.__table}" + sql_condition
        sql = sql.strip("AND ") + ";"

        return self.execute(sql, tuple(sql_values))

    def insert(self, sql, document):
        # GENERALISE DATA
        for key, value in document.items():
            if type(value) == str:
                document[key] = value.upper()
            elif type(value) == int:
                document[key] = int(value)
        # NAME OF DOCUMENT NOT IN DATABASE THEN ADD
        if self.find(Name=document['Name']) == []:
            self.execute(sql, document)

    def drop(self):
        self.execute(f'DROP TABLE IF EXISTS {self.__table}')

class Student(Table):
    def __init__(self, database):
        super().__init__(database, "Student")
        self.execute(sql.CREATE_STUDENT)
        self.execute(sql.CREATE_STUDENTCLUB)
        self.execute(sql.CREATE_STUDENTSUBJECT)
        self.execute(sql.CREATE_STUDENTACTIVITY)

    def insert(self, document):
        super().insert(sql.INSERT_STUDENT, document)

class Class(Table):
    def __init__(self, database):
        super().__init__(database, "Class")
        self.execute(sql.CREATE_CLASS)

    def insert(self, document):
        super().insert(sql.INSERT_CLASS, document)

class Club(Table):
    def __init__(self, database):
        super().__init__(database, "Club")
        self.execute(sql.CREATE_CLUB)

    def insert(self, document):
        super().insert(sql.INSERT_CLUB, document)

    def find_students_not_in_club(self, club_id):
        return self.execute(sql.STUDENT_NOT_IN_CLUB, club_id)

    def find_students_in_club(self, club_id):
        return self.execute(sql.STUDENTROLE_IN_CLUB, club_id)

    def insert_member(self, club_id, student_id):
        data = []
        for id in student_id:
            data.append({'StudentID': id, 'ClubID': club_id})
        for record in data:
            self.execute(sql.INSERT_MEMBER, record)

class Activity(Table):
    def __init__(self, database):
        super().__init__(database, "Activity")
        self.execute(sql.CREATE_ACTIVITY)

    def insert(self, document):
        super().insert(sql.INSERT_ACTIVITY, document)

class Subject(Table):
    def __init__(self, database):
        super().__init__(database, "Subject")
        self.execute(sql.CREATE_SUBJECT)

    def insert(self, document):
        super().insert(sql.INSERT_SUBJECT, document)

coll = {
    'student': Student("database.db"),
    'class': Class("database.db"),
    'subject': Subject("database.db"),
    'activity': Activity("database.db"),
    'club': Club("database.db"),
}
coll['student'].import_csv('student.csv')
coll['class'].import_csv('class.csv')
coll['subject'].import_csv('subject.csv')
