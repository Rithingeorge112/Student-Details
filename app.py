from flask import Flask, request, url_for, render_template, redirect
import csv
from pathlib import Path

app = Flask(__name__)
path = Path(__file__).parent/'csv\\students.csv'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detail-submit', methods=['POST'])
def detailSubmit():
    if request.method == 'POST':
        storeInCSV()
        return redirect(url_for('home'))

@app.route('/add-student')
def addStudent():
    return render_template('add-student.html')

@app.route('/search-student')
def searchStudent():
    return render_template('search-student.html')

@app.route('/single-student', methods=['POST'])
def singleStudent():
    student_id = request.form['student-id']
    count = -1
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            count = count + 1
    if(int(student_id) > count):
        return render_template('search-student.html', Max=count)
    else:
        with open(path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if(row[0] == student_id):
                    name = row[1]
                    gender = row[2]
                    dob = row[3]
                    city = row[4]
                    state = row[5]
                    email = row[6]
                    degree = row[7]
                    stream = row[8]
        return render_template('singleStudent.html', 
                                id=student_id, name=name, 
                                gender=gender, dob=dob,
                                city=city, state=state,
                                email=email, degree=degree, stream=stream)

@app.route('/all student details')
def displayAllStudent():
    allstudents = []
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for i in reader:
            allstudents.append(i)

    return render_template('allstudents.html', allStudents=allstudents)

def storeInCSV():
    student_id = request.form['student-id']
    student_name = request.form['student-name']
    gender = request.form['gender']
    dob = request.form['dob']
    city = request.form['city']
    state = request.form['state']
    emailId = request.form['email-id']
    qualification = request.form['qualification']
    stream = request.form['stream']
    studentDetail = [student_id, student_name, gender, dob, city, state, emailId, qualification, stream]

    with open(path, 'a+', newline='\n') as file:
        write = csv.writer(file, studentDetail)
        write.writerow(studentDetail)


if __name__ == '__main__':
    app.run(debug=True)