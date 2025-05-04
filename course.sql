USE course_registration_db;

-- Create table for departments
CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- Create table for instructors
CREATE TABLE instructors (
    instructor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Create table for courses
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    instructor_id INT,
    department_id INT,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Create table for students
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

-- Create table for registrations (Many-to-Many: students <-> courses)
CREATE TABLE registrations (
    registration_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
--     registration_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Insert departments
INSERT INTO departments (name) VALUES ('Computer Science'), ('Business');

-- Insert instructors
INSERT INTO instructors (name, email, department_id) VALUES 
('Alice Kim', 'alice@university.com', 1),
('Bob Mwangi', 'bob@university.com', 2);

-- Insert courses
INSERT INTO courses (title, description, instructor_id, department_id) VALUES 
('Web Development', 'HTML, CSS, JavaScript basics', 1, 1),
('Business Strategy', 'Introduction to business strategy', 2, 2);

-- Insert students
INSERT INTO students (name, email) VALUES 
('Grace Ndungu', 'grace@student.com'),
('John Otieno', 'john@student.com');

-- Insert registrations
INSERT INTO registrations (student_id, course_id) VALUES 
(1, 1),
(2, 1),
(2, 2);