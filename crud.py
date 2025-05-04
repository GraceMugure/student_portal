from database import get_connection
from schemas import StudentCreate

def create_student(student: StudentCreate):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO students (name, email, age) VALUES (%s, %s, %s)"
    cursor.execute(sql, (student.name, student.email, student.age))
    conn.commit()
    student_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return {**student.dict(), "id": student_id}

def get_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_student(student_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_student(student_id: int, student: StudentCreate):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE students SET name=%s, email=%s, age=%s WHERE id=%s"
    cursor.execute(sql, (student.name, student.email, student.age, student_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Student updated"}

def delete_student(student_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Student deleted"}
