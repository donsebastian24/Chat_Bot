from flask import Flask, render_template, request

app = Flask(__name__)

# Sample dictionary to store user data and tickets
users_data = {}


@app.route('/')
def greeting():
    return render_template('index.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        employee_number = request.form['employee_number']
        email = request.form['email']
        mobile_number = request.form['mobile_number']

        # Basic input validation
        if not (employee_number and email and mobile_number):
            return "Please provide all required information."

        # Store user data
        user_key = f"{employee_number}-{email}"
        users_data[user_key] = {'employee_number': employee_number,
                                'email': email,
                                'mobile_number': mobile_number,
                                'issue_type': None,
                                'sub_issue': None,
                                'problem_description': None,
                                'suggested_solutions': None}

        return render_template('issue_selection.html', user_key=user_key)

    return render_template('greeting.html')


@app.route('/process/<user_key>', methods=['POST'])
def process(user_key):
    user_data = users_data.get(user_key)

    if not user_data:
        return "Invalid user key."

    issue_type = request.form['issue_type']
    user_data['issue_type'] = issue_type

    return render_template('sub_issue_selection.html', user_key=user_key, issue_type=issue_type)


@app.route('/sub_process/<user_key>', methods=['POST'])
def sub_process(user_key):
    user_data = users_data.get(user_key)

    if not user_data:
        return "Invalid user key."

    sub_issue = request.form['sub_issue']
    user_data['sub_issue'] = sub_issue

    return render_template('problem_description.html', user_key=user_key)


@app.route('/solution/<user_key>', methods=['POST'])
def solution(user_key):
    user_data = users_data.get(user_key)

    if not user_data:
        return "Invalid user key."

    problem_description = request.form['problem_description']
    user_data['problem_description'] = problem_description

    # Sample logic to suggest solutions based on the issue
    suggested_solutions = ["Check if it's plugged in", "Restart the device", "Contact IT support"]
    user_data['suggested_solutions'] = suggested_solutions

    return render_template('suggested_solution.html', user_key=user_key, solutions=suggested_solutions)


@app.route('/follow_up/<user_key>', methods=['POST'])
def follow_up(user_key):
    user_data = users_data.get(user_key)

    if not user_data:
        return "Invalid user key."

    return render_template('follow_up.html', user_key=user_key)


@app.route('/escalate/<user_key>', methods=['POST'])
def escalate(user_key):
    user_data = users_data.get(user_key)

    if not user_data:
        return "Invalid user key."

    # Sample logic to create a ticket
    ticket_number = "T123"
    user_data['ticket_number'] = ticket_number

    return render_template('ticket_submission.html', user_key=user_key, ticket_number=ticket_number)




if __name__ == '__main__':
    app.run(debug=True)
