from sqliteDB import *


class Employees:

    """
    Employees class provides methods to interact with the 'employee' table in the database.

    Methods:
        - get_all_employee(): Retrieve all employees from the 'employee' table.
        - get_employees_list_json(): Get a list of employees in JSON format.
        - add_an_employee(data): Add a new employee to the 'employee' table.

    Note:
        - This class assumes the existence of a 'db' object connected to a Flask SQLAlchemy instance.
        - 'Employee' model is expected to be defined and imported from the database setup.
    """

    @staticmethod
    def get_all_employee():
        """
        Retrieve all employees from the 'employee' table.

        Returns:
            List[Employee]: List of all employees.
        """

        employees = Employee.query.all()
        return employees

    @staticmethod
    def get_employees_list_json():
        """
        Get a list of employees in JSON format.

        Returns:
            List[Dict]: List of employee information in JSON format.
        """

        employees = get_all_employee()
        employee_list = []
        for emp in employees:
            employee_list.append({
                'name': emp.name,
                'address': emp.address,
                'email': emp.email,
                'designation': emp.designation,
                'department': emp.department,
                'date_of_joining': emp.date_of_joining.strftime('%Y-%m-%d') if emp.date_of_joining else None
            })
        return employee_list

    @staticmethod
    def add_an_employee(data):

        """
        Add a new employee to the 'employee' table.

        Args:
            data (dict): Data containing employee information.

        Returns:
            None
        """

        # Converting the 'date_of_joining' string to a Python date object
        date_of_joining_str = data.get('date_of_joining')
        date_of_joining = datetime.strptime(date_of_joining_str, '%Y-%m-%d').date() if date_of_joining_str else None

        new_employee = Employee(
            name=data.get('name'),
            address=data.get('address'),
            email=data.get('email'),
            designation=data.get('designation'),
            department=data.get('department'),
            date_of_joining=date_of_joining
        )

        db.session.add(new_employee)
        db.session.commit()

        return



class EmpAttendance:
    """
    EmpAttendance class provides methods related to attendance tracking for employees.

    Methods:
        - get_attendance_report(employee_id): Retrieve the attendance report for a specific employee.
        - attendance_marking(data): Mark attendance for an employee.

    Note:
        - This class assumes the existence of a 'db' object connected to a Flask SQLAlchemy instance.
        - 'Attendance' model is expected to be defined and imported from the database setup.
    """

    @staticmethod
    def get_attendance_report(employee_id):
        """
        Retrieve the attendance report for a specific employee.

        Args:
            employee_id (int): ID of the employee.

        Returns:
            List[Dict]: List of attendance records for the employee in JSON format.
        """

        attendance_records = Attendance.query.filter_by(employee_id=employee_id).all()
        attendance_list = []
        for record in attendance_records:
            attendance_list.append({
                'in_time': record.in_time.strftime('%Y-%m-%d %H:%M:%S') if record.in_time else None,
                'out_time': record.out_time.strftime('%Y-%m-%d %H:%M:%S') if record.out_time else None,
                'date': record.date.strftime('%Y-%m-%d')
            })
        return attendance_list

    @staticmethod
    def attendance_marking(data):

        """
        Mark attendance for an employee.

        Args:
            data (dict): Data containing attendance information.

        Returns:
            None
        """

        employee_id = data.get('employee_id')
        in_time_str = data.get('in_time')
        out_time_str = data.get('out_time')
        date_str = data.get('date')

        # Convert time strings to datetime objects with a default date
        default_date = datetime.now().date()
        in_time = datetime.combine(default_date, datetime.strptime(in_time_str, '%H:%M').time())
        out_time = datetime.combine(default_date, datetime.strptime(out_time_str, '%H:%M').time())

        # Convert date string to datetime object
        date = datetime.strptime(date_str, '%Y-%m-%d').date()

        attendance = Attendance(in_time=in_time, out_time=out_time, date=date, employee_id=employee_id)
        db.session.add(attendance)
        db.session.commit()

        return 


class Reports:

    """
    Reports class provides methods for generating various reports related to employee data.

    Methods:
        - get_department_report(): Retrieve a report on the number of employees in each department.

    Note:
        - This class assumes the existence of a 'db' object connected to a Flask SQLAlchemy instance.
        - 'Employee' model is expected to be defined and imported from the database setup.
    """
    @staticmethod
    def get_department_report():

        """
        Retrieve a report on the number of employees in each department.

        Returns:
            List[Dict]: List of department-wise reports in JSON format.
        """

        departments = db.session.query(Employee.department, db.func.count(Employee.id)).group_by(Employee.department).all()
        report = [{'department': dept, 'employee_count': count} for dept, count in departments]
        return report






