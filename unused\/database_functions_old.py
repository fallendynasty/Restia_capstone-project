import sqlite3
import csv
import sql

class Table:
    def init(self, database, table):
        self.database = database
        self.table = table

    def import_csv(self, filename):
        with open(filename, 'r') as f:
            for record in csv.DictReader(f):
                self.insert(record)

    def execute(self, sql, values="", type=""):
        with sqlite3.connect(self.__database) as conn:
            cur = conn.cursor()
            cur.execute(sql, values)

class Student(Table):
    def init(self, database):
        super().init(database, "Student")
        self.execute(sql.CREATE_STUDENT)

    def insert(self, document):
        super().insert(sql.INSERT_STUDENT, document)


class Class(Table):
    def init(self, database):
        super().init(database, "Class")
        self.execute(sql.CREATE_CLASS)

    def insert(self, document):
        super().insert(sql.INSERT_CLASS, document)


class Club(Table):
    def init(self, database):
        super().init(database, "Club")
        self.execute(sql.CREATE_CLUB)

    def insert(self, document):
        super().insert(sql.INSERT_CLUB, document)


class Activity(Table):
    def init(self, database):
        super().init(database, "Activity")
        self.execute(sql.CREATE_ACTIVITY)

    def insert(self, document):
        super().insert(sql.INSERT_ACTIVITY, document)


class Subject(Table):
    def init(self, database):
        super().init(database, "Subject")
        self.execute(sql.CREATE_SUBJECT)

    def insert(self, document):
        super().insert(sql.INSERT_SUBJECT, document)