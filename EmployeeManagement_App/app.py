from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.exceptions import BadRequest

######## File imports start here #########
from sqliteDB import *
from sections import *
from middlewares import *
######## File imports Ends here #########

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db.init_app(app)

middleware_instance = Middlewares()

#####################################################################################

#Home Section
""" Home Page (viewing all the employees here at home page) """

# Home Route
@app.route('/', methods=['GET'])
def home():
    try:
        # Fetching all the Employee Details from DB
        employees = Employees.get_all_employee()
        return render_template('home.html', employees=employees)
    except Exception as e:
        # Log the exception or handle it as needed
        error_message = f"Error fetching employee details: {str(e)}"
        return render_template('error.html', error_message=error_message)

#####################################################################################

#Employee Section

""" Adding and Rendering Employee Details """

# Endpoint for adding the Employees
@app.route('/add_employee', methods=['POST'])
@middleware_instance.email_validation_middleware
def add_employee():
    try:
        data = request.get_json()

        #check for empty string
        if data['email'] == '' or data['designation'] == '' or data['department'] == '' or data['date_of_joining'] == '' or data['name'] == '':
            return jsonify({'message': "department, date of joining, name and Email cannot be empty"}), 200

        Employees.add_an_employee(data)

        return jsonify({'message': 'Employee added successfully'}), 201 # success
    except BadRequest as e:
        # Handle BadRequest exception (Invalid email address) raised in middleware
        return jsonify({'message': "Invalid Email Format"}), 400  # Bad Request
    except Exception as e:
        # Log the exception or handle it as needed
        return jsonify({'message':f"Please check email, department and name cannot be null, Email should be Unique and try again : \n{e}" }), 500  # Internal Server Error

# Route to Render the Employee Page
@app.route('/render_add_employee', methods=['GET'])
def render_add_employee():
    try:
        return render_template('add_employee.html')
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('error.html', error_message=error_message)

#####################################################################################

#Attendance Section
""" Adding and Rendering Attendance """

# Route to render the details of the Attendance of an individual Employee
@app.route('/render_attendance/<int:employee_id>', methods=['GET'])
def render_attendance(employee_id):
    try:
        attendance_list = EmpAttendance.get_attendance_report(employee_id)
        return render_template('show_attendance.html', attendance={'attendance': attendance_list})
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('error.html', error_message=error_message)

    
# Route to mark the attendance of the employee
@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    try:
        data = request.get_json()
        EmpAttendance.attendance_marking(data)
        return jsonify({'message': 'Attendance marked successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'Please check that you have filled all the input fields and try again'}), 500

# Route to Render the Marks Form of the attendance
@app.route('/render_mark_attendance', methods=['GET'])
def render_mark_attendance():
    try:
        # Fetching all the Employee Details from DB
        employees = Employees.get_all_employee()
        return render_template('mark_attendance.html', employees=employees)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('error.html', error_message=error_message)


#####################################################################################

#Department section
""" Getting the Department Details """

# Route to render the Department wise report
@app.route('/department_report')
def department_report():
    try:
        report = Reports.get_department_report()
        return render_template('department.html', report=report)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('error.html', error_message=error_message)

#####################################################################################




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)




