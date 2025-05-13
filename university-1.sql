ATTACH DATABASE 'university.db' as university;

-- Create table `students` (Primary key: student_id)
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date TEXT,
    enrollment_date TEXT
);

-- Insert sample data into `students`
INSERT INTO students (first_name, last_name, birth_date, enrollment_date) VALUES
('Emily', 'Brown', '2000-01-15', '2020-08-20'),
('Jane', 'Smith', '1999-07-30', '2019-09-10'),
('Mark', 'Johnson', '2001-05-25', '2021-01-15'),
('John', 'Doe', '2000-11-05', '2020-08-10'),
('Michael', 'Williams', '1998-04-18', '2018-05-23'),
('Sarah', 'Davis', '2002-10-10', '2022-01-01'),
('David', 'Miller', '2000-08-12', '2020-03-15'),
('Sophia', 'Garcia', '1999-12-30', '2019-08-12'),
('Daniel', 'Martinez', '2001-02-22', '2021-03-10'),
('Olivia', 'Rodriguez', '2000-09-05', '2020-07-17');

-- Create the courses table with an additional `professor_id` column
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    course_description TEXT,
    professor_id INTEGER,
    FOREIGN KEY (professor_id) REFERENCES faculty(faculty_id)
);

-- Insert sample data into the courses table with professor references
-- Dr. Alan Turing teaches Algorithms and Programming Languages
INSERT INTO courses (course_name, course_description, professor_id) VALUES
('Algorithms', 'Introduction to algorithms and data structures', 1),
('Programming Languages', 'Study of different programming paradigms', 1),
('Database Systems', 'Fundamentals of databases and SQL', 2),
('Operating Systems', 'Concepts and principles of operating systems', 3),
('Artificial Intelligence', 'Basics of AI and machine learning', 4),
('Computer Networks', 'Introduction to networking and protocols', 5),
('Software Engineering', 'Software development lifecycle and methodologies', 6),
('Discrete Mathematics', 'Mathematical foundations for computer science', 7),
('Data Science', 'Introduction to data analysis and statistics', 9),
('Web Development', 'Building websites and web applications', 10);

CREATE TABLE student_courses (
    student_id INTEGER,
    course_id INTEGER,
    grade INTEGER CHECK(grade BETWEEN 0 AND 100),  -- Grades range from 0 to 100
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    PRIMARY KEY (student_id, course_id)
);

-- Insert sample data into the updated student_courses table with grades ranging from 0 to 100
INSERT INTO student_courses (student_id, course_id, grade) VALUES
(1, 1, 85),
(1, 3, 78),
(2, 2, 62),
(2, 4, 80),
(3, 1, 75),
(3, 5, 88),
(4, 3, 65),
(4, 2, 60),
(5, 6, 90),
(5, 7, 60),
(6, 5, 83),
(6, 8, 77),
(7, 4, 68),
(7, 9, 82),
(8, 6, 91),
(8, 10, 80),
(9, 7, 85),
(9, 1, 76),
(10, 8, 69),
(10, 2, 93);

-- Create table `departments` (Primary key: department_id)
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL
);

-- Insert sample data into `departments`
INSERT INTO departments (department_name) VALUES
('Computer Science'),
('Mathematics'),
('Electrical Engineering'),
('Mechanical Engineering'),
('Civil Engineering'),
('Chemical Engineering'),
('Physics'),
('Biology'),
('Chemistry'),
('Economics');

-- Create table `faculty` (One-to-many relation: departments and faculty)
CREATE TABLE faculty (
    faculty_id INTEGER PRIMARY KEY,
    faculty_name TEXT NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Insert sample data into `faculty`
INSERT INTO faculty (faculty_name, department_id) VALUES
('Dr. Alan Turing', 1),
('Dr. Grace Hopper', 1),
('Dr. John von Neumann', 2),
('Dr. Carl Sagan', 7),
('Dr. Marie Curie', 8),
('Dr. Richard Feynman', 7),
('Dr. Nikola Tesla', 3),
('Dr. Ada Lovelace', 1),
('Dr. Albert Einstein', 7),
('Dr. Rosalind Franklin', 8);