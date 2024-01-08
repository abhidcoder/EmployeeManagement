from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Defining the Employee model
class Employee(db.Model):
    

    """
    Employee Model represents the structure of the 'employee' table in the database.

    Attributes:
        id (int): Primary key for the Employee table.
        name (str): Name of the employee.
        address (str): Address of the employee.
        email (str): Email address of the employee, unique and not nullable.
        designation (str): Designation or job title of the employee.
        department (str): Department in which the employee works and not nullable.
        date_of_joining (Date): Date when the employee joined the organization.
        attendance (relationship): One-to-Many relationship with the 'Attendance' table.

    Relationships:
        - One Employee can have multiple attendance records.

    Note:
        - 'attendance' attribute represents the attendance records associated with the employee.
    """

    # Fields for the Employee model
    #Note: nullabe considers '' empty string as not null
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    email = db.Column(db.String(255),nullable=False, unique=True)  #email should be unique and not Null
    designation = db.Column(db.String(255))
    department = db.Column(db.String(255),nullable=False)
    date_of_joining = db.Column(db.Date,nullable=False)
    # One-to-Many relationship with Attendance
    attendance = db.relationship('Attendance', backref='employee', lazy=True)

# Defining the Attendance model
class Attendance(db.Model):

    """
    Attendance Model represents the structure of the 'attendance' table in the database.

    Attributes:
        id (int): Primary key for the Attendance table.
        in_time (DateTime): Time when the employee checked in for attendance.
        out_time (DateTime): Time when the employee checked out for attendance.
        date (Date): Date of the attendance record.
        employee_id (int): Foreign key referencing the 'id' column in the 'employee' table, not nullable.

    Relationships:
        - Belongs to one Employee ('employee_id' references the 'id' column in the 'employee' table).

    Note:
        - The 'employee_id' attribute establishes a foreign key relationship with the 'id' column in the 'employee' table.
    """
    
    # Fields for the Attendance model
    id = db.Column(db.Integer, primary_key=True)
    in_time = db.Column(db.DateTime)
    out_time = db.Column(db.DateTime)
    date = db.Column(db.Date)
    # Foreign key referencing Employee
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    

# Exception handling for database operations
try:
    # Create all tables in the database
    db.create_all()
except Exception as e:
    # Logging Error
    print(f"Error creating tables: {e}")