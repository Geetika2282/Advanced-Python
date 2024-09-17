from flask import Flask, request, render_template, redirect, session
import csv

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form data
        session['name'] = request.form.get('name')
        session['email'] = request.form.get('email')

        # Save to CSV
        with open('data.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([session['name'], session['email']])

        return redirect('/confirm')
    return render_template('home.html')


@app.route('/confirm')
def confirm():
    # Retrieve name and email from session
    name = session.get('name')
    email = session.get('email')

    # Pass the values to confirm.html
    return render_template('confirm.html', name=name, email=email)


if __name__ == '__main__':
    app.run(debug=True)
