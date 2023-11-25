from flask import Flask, request, render_template

app = Flask(__name__)

tickets = []


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/create_ticket', methods=['POST'])
def create_ticket():
    issue = request.form.get('issue')
    if issue is None:
        return 'No issue provided', 400

    ticket_id = len(tickets) + 1
    ticket = {'id': ticket_id, 'issue': issue}
    tickets.append(ticket)

    return 'Ticket created with ID: ' + str(ticket_id), 201


if __name__ == '__main__':
    app.run(debug=True)
