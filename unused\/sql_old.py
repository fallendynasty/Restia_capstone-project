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

CREATE_STUDENTCLUB = """
CREATE TABLE IF NOT EXISTS StudentClub (
    StudentID INTEGER,
    ClubID INTEGER,
    Role TEXT DEFAULT 'MEMBER',
    PRIMARY KEY (StudentID, ClubID)
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (ClubID) REFERENCES Club(ID)
);
"""

CREATE_STUDENTSUBJECT = """
CREATE TABLE IF NOT EXISTS StudentSubject (
    StudentID INTEGER,
    SubjectID TEXT,
    PRIMARY KEY (StudentID, SubjectID)
    FOREIGN KEY (StudentID) REFERENCES Student(ID),
    FOREIGN KEY (SubjectID) REFERENCES Subject(ID)
);
"""

CREATE_STUDENTACTIVITY = """
CREATE TABLE IF NOT EXISTS StudentActivity (
    StudentID INTEGER,
    ActivityID INTEGER,
    PRIMARY KEY (StudentID, ActivityID)
    FOREIGN KEY (StudentID) REFERENCES Student(ID),
    FOREIGN KEY (ActivityID) REFERENCES Activity(ID)
);
"""

CREATE_CLUBACTIVITY = """
CREATE TABLE IF NOT EXISTS ClubActivity (
    ClubID INTEGER,
    ActivityID INTEGER,
    PRIMARY KEY (ClubID, ActivityID)
    FOREIGN KEY (ClubID) REFERENCES Club(ID),
    FOREIGN KEY (ActivityID) REFERENCES Activity(ID)
);
"""

### SQL INSERT STATEMENTS ###
# Insert for Student, Class, Club, Subject, Activity
INSERT_STUDENT = """
INSERT INTO Student (
    Name,
    Age,
    YearEnrolled,
    StudentClass
) VALUES (
    :Name,
    :Age,
    :YearEnrolled,
    :StudentClass
);
"""

INSERT_CLASS = """
INSERT INTO Class (
    Name,
    ClassLevel,
    GraduatingYear,
    ClassTutor
) VALUES (
    :Name,
    :ClassLevel,
    :GraduatingYear,
    :ClassTutor
);
"""

INSERT_CLUB = """
INSERT INTO Club (
    Name
) VALUES (
    :Name
);
"""

INSERT_ACTIVITY = """
INSERT INTO Activity (
    Name,
    StartDate,
    EndDate,
    Description
) VALUES (
    :Name,
    :StartDate,
    :EndDate,
    :Description
);
"""

INSERT_SUBJECT = """
INSERT INTO Subject (
    ID
    Name,
    SubjectLevel
) VALUES (
    :ID
    :Name,
    :SubjectLevel
);
"""
