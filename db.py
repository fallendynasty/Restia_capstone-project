import sqlite3
import sql

class Table:
    def init(self, database, table):
        self.database = database
        self.table = table

    def execute(self, sql, values = None):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            cur.execute(sql, values)

    def update(self, data_updated, data_checked):
        with sqlite3.connect(self.database) as conn:
            query = """UPDATE """ + self.table + """ SET student_name = ? WHERE id = ?"""
            param = (data_updated, data_checked)
            cur = conn.cursor()
            cur.execute(query, param)
            conn.commit()


    def delete(self, value):
        with sqlite3.connect(self.database) as conn:
            query = """DELETE FROM """ + self.table + """ WHERE id = ?;"""
            param = (value, )
            cur = conn.cursor()
            cur.execute(query, param)
            conn.commit()


    def find(self, value):
        with sqlite3.connect(self.database) as conn:
            query = """SELECT * FROM """ + self.table + """ WHERE id = ?;"""
            param = (value, )
            cur = conn.cursor()
            cur.execute(query, param)
            record = cur.fetchone()

        return record

class Student(Table):
    def init(self, database):
        super().init(database, "Student")
        self.execute(sql.CREATE_STUDENT)

    def insert(self, doc):
        if not self.find(doc['id']):
            self.execute(sql.INSERT_STUDENT, tuple(doc.values()))

class Class(Table):
    def init(self, database):
        super().init(database, "Class")
        self.execute(sql.CREATE_CLASS)

    def insert(self, doc):
        if not self.find(doc['id']):
            self.execute(sql.INSERT_CLASS, doc)


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

    def insert(self, doc):
        if not self.find(doc['id']):
            super().insert(sql.INSERT_ACTIVITY, doc)


class Subject(Table):
    def init(self, database):
        super().init(database, "Subject")
        self.execute(sql.CREATE_SUBJECT)

    def insert(self, doc):
        if not self.find(doc['id']):
            super().insert(sql.INSERT_SUBJECT, doc)











CREATE_STUDENT = """
CREATE TABLE IF NOT EXISTS Student (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    YearEnrolled INTEGER,
    StudentClass INTEGER,
    FOREIGN KEY(StudentClass) REFERENCES Class(ID)
);
"""

CREATE_CLASS = """
CREATE TABLE IF NOT EXISTS Class (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    ClassLevel TEXT CHECK (
        ClassLevel IN ('JC1', 'JC2')
        ),
    GraduatingYear INTEGER,
    ClassTutor INTEGER,
    FOREIGN KEY (ClassTutor) REFERENCES Tutor(ID)
);
"""

CREATE_SUBJECT = """
CREATE TABLE IF NOT EXISTS Subject (
    ID TEXT PRIMARY KEY,
    Name TEXT CHECK (
        Name IN (
            'GP', 'MATH', 'FM', 'COMP', 'PHY', 'CHEM', 'ECONS', 'BIO',
            'GEO', 'HIST', 'ELIT', 'ART', 'CLTRANS', 'CL', 'ML', 'TL', 'TRAN',
            'CLL', 'CLB', 'PW', 'PUNJABI', 'HINDI', 'BENGALESE', 'JAPANESE'
            )
        ),
    SubjectLevel TEXT CHECK (
        SubjectLevel IN ('H1','H2','H3')
        )
);
"""

CREATE_CLUB = """
CREATE TABLE IF NOT EXISTS Club (
    ID INTEGER PRIMARY KEY,
    Name TEXT
);
"""

# start date has a certain format
# end date is optional
CREATE_ACTIVITY = """
CREATE TABLE IF NOT EXISTS Activity (
    ID INTEGER PRIMARY KEY,
    Name TEXT
    StartDate TEXT
    EndDate TEXT
    Description TEXT
);
""" 