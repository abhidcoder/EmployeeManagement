from flask import request,abort,jsonify
import re

class Middlewares:
    """
        Validate the email address extracted from the request data.

        Args:
            func (callable): The original function to be decorated.

        Returns:
            callable: The decorated function.

        Raises:
            HTTPException: If the email address is invalid (HTTP 400 Bad Request).

        Notes:
            This static method is intended to be used as a decorator for Flask routes.
            It validates the email address using a regular expression and raises an
            HTTPException with a 400 status code if the email is invalid. If the email
            is valid, it calls the original function.

        Example:
            ```python
            @app.route('/add_employee', methods=['POST'])
            @middleware_instance.email_validation_middleware
            def add_employee():
                # route logic here
            ```
        """

    @staticmethod
    def email_validation_middleware(func):
        def wrapper(*args, **kwargs):
            data = request.get_json() or {}
            email = data.get('email', '')

            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if re.match(email_regex, email) is None:
                abort(400, description='Invalid email address. Please provide a valid email.')

            try:
                return func(*args, **kwargs)
            except Exception as e:
                return jsonify({'message': f"An error occurred: {str(e)}"}), 500

        return wrapper
