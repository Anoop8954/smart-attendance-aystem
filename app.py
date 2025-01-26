from flask import Flask, request, jsonify
import pymysql
import numpy as np
from face_recognition import capture_face_data, recognize_face

app = Flask(__name__)

# Database connection
db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="attendance_system"
)
cursor = db.cursor()

# Route to register a user
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data['name']
    roll_no = data['roll_no']
    face_data = capture_face_data(name, roll_no)
    sql = "INSERT INTO users (name, roll_no, face_data) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, roll_no, face_data.tobytes()))
    db.commit()
    return jsonify({"message": "User registered successfully!"})

# Route to mark attendance
@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    sql = "SELECT id, face_data FROM users"
    cursor.execute(sql)
    users = cursor.fetchall()
    known_faces = {user[0]: np.frombuffer(user[1], dtype=np.uint8) for user in users}
    recognize_face(known_faces)
    return jsonify({"message": "Attendance process completed!"})

if __name__ == '__main__':
    app.run(debug=True)
