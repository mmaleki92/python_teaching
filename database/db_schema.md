## School Management System
- Students: Holds student information.
- Teachers: Contains teacher details.
- Courses: Lists available courses.
- Enrollments: Tracks which students are enrolled in which courses.
- Grades: Records grades for students in courses.

```sql
CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    Class TEXT
);

CREATE TABLE Teachers (
    TeacherID INTEGER PRIMARY KEY,
    Name TEXT,
    Subject TEXT
);

CREATE TABLE Subjects (
    SubjectID INTEGER PRIMARY KEY,
    Name TEXT,
    Subject TEXT
);

CREATE TABLE Courses (
    CourseID INTEGER PRIMARY KEY,
    Name TEXT,
    TeacherID INTEGER,
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID)
);

CREATE TABLE Enrollments (
    StudentID INTEGER,
    CourseID INTEGER,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

CREATE TABLE Grades (
    StudentID INTEGER,
    CourseID INTEGER,
    Grade TEXT,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);
```