# Employee Management and Attendance Tracking App

## Project Structure

- **app.py**: Main Flask application file containing routes.
- **sqliteDB.py**: Main Database file containing database models.
- **sections.py**: File containing logic for Employees, Attendance and Departments.
- **middleware.py**: File containing Middleware logic for validation purposes.

- **templates**: Folder containing HTML templates for rendering pages.
    - **home.html**: Template for the home page displaying the list of employees and navigation.
    - **department.html**: Template for the department-wise employee count report.
    - **mark_attendance.html**: Template for adding the attendance in and out time durations of employee.
    - **show_attendance.html**: Template for displaying the attendance details of a employee.
    - **add_employee.html**:  Template for adding the employee details.
    - **error.html**: Template for error handling if any templating rendering fails.

- **static**: Folder containing HTML templates for rendering pages.
    - **home.css**: Styling for home.html.
    - **department.css**: Styling for department.html.
    - **mark_attendance.css**: Styling for mark_attendance.html.
    - **show_attendance.css**: Styling for show_attendance.html.
    - **add_employee.css**:  Styling for add_employee.html.
    - **error.css**: Styling for error.html.

- **instance**: Folder contains the 'sqlite.db' database that will be created automatically as application starts.

- **README.md**: Project documentation file.



## How to Run Locally
1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask app using `python app.py` or `python3 app.py`.
4. Access the app in your web browser at `http://127.0.0.1:5000/`.


## Additional Information
- This app uses SQLite as the database.
- Make sure to have Python and Flask installed on your system.


## Note: If still facing the issue in runing due to the version conflicts then try

- pip install flask_sqlalchemy
- pip install watchdog

Feel free to reach out for any questions or improvements! 





