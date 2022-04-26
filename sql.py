### SQL CREATE STATEMENTS ###
CREATE_STUDENT = """
CREATE TABLE IF NOT EXISTS Student (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Age INTEGER NOT NULL,
    YearEnrolled INTEGER NOT NULL,
    GraduatingYear INTEGER NOT NULL,
    StudentClass INTEGER,
    FOREIGN KEY(StudentClass) REFERENCES Class(ID)
);
"""

CREATE_CLASS = """
CREATE TABLE IF NOT EXISTS Class (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    ClassLevel TEXT NOT NULL CHECK (
        ClassLevel IN ('JC1', 'JC2')
        )
);
"""

CREATE_SUBJECT = """
CREATE TABLE IF NOT EXISTS Subject (
    ID TEXT PRIMARY KEY,
    Name TEXT NOT NULL CHECK (
        Name IN (
            'GP', 'MATH', 'FM', 'COMP', 'PHY', 'CHEM', 'ECONS', 'BIO',
            'GEO', 'HIST', 'ELIT', 'ART', 'CLTRANS', 'CL', 'ML', 'TL',
            'CLL', 'CLB', 'PW', 'PUNJABI', 'HINDI', 'BENGALESE', 'JAPANESE'
            )
        ),
    SubjectLevel TEXT NOT NULL CHECK (
        SubjectLevel IN ('H1','H2','H3')
        )
);
"""

CREATE_CLUB = """
CREATE TABLE IF NOT EXISTS Club (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
);
"""

# start date has a certain format
# end date is optional
CREATE_ACTIVITY = """
CREATE TABLE IF NOT EXISTS Activity (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    StartDate TEXT NOT NULL,
    EndDate TEXT,
    Description TEXT
);
"""

### RELATIONAL TABLES ###
CREATE_STUDENTCLUB = """
CREATE TABLE IF NOT EXISTS StudentClub (
    StudentID INTEGER,
    ClubID INTEGER,
    Role TEXT DEFAULT 'MEMBER',
    PRIMARY KEY (StudentID, ClubID)
    FOREIGN KEY (StudentID) REFERENCES Student(ID),
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



### SQL INSERT STATEMENTS ###
# Insert for Student, Class, Club, Subject, Activity
INSERT_STUDENT = """
INSERT INTO Student (
    Name,
    Age,
    YearEnrolled,
    GraduatingYear,
    StudentClass
) VALUES (
    :Name,
    :Age,
    :YearEnrolled,
    :GraduatingYear,
    :StudentClass
);
"""

INSERT_CLASS = """
INSERT INTO Class (
    Name,
    ClassLevel
) VALUES (
    :Name,
    :ClassLevel
);
"""

INSERT_CLUB = """
INSERT INTO Club (
    Name
) VALUES (
    :Name
)
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
    ID,
    Name,
    SubjectLevel
) VALUES (
    :ID,
    :Name,
    :SubjectLevel
);
"""

INSERT_MEMBER = """
INSERT INTO StudentClub (
    StudentID,
    ClubID
) VALUES (
    :StudentID,
    :ClubID
)
"""

STUDENT_NOT_IN_CLUB = """
SELECT Student.ID, Student.Name, Club.Name
FROM Student
LEFT JOIN StudentClub
ON Student.ID = StudentClub.StudentID
LEFT JOIN Club
ON Club.ID = StudentClub.ClubID
WHERE Student.ID IN (
    SELECT ID
    FROM Student
    WHERE ID NOT IN (
        SELECT StudentID
        FROM StudentClub
        WHERE ClubID = ?
    )
);
"""

STUDENTROLE_IN_CLUB = """
SELECT Student.Name, StudentClub.Role
FROM Student
JOIN StudentClub
ON Student.ID = StudentClub.StudentID
JOIN Club
ON Club.ID = StudentClub.ClubID
WHERE ClubID = ?;
"""
