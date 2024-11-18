from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    # Print for debugging
    print(f"Redirecting to success with name: {name}")
    return f"Welcome {name}"

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('user')  # Get the 'user' value from the form data
        if user:
            # Print for debugging
            print(f"Received user: {user}")
            return redirect(url_for('success', name=user))
        else:
            print("No user name provided.")
            return "Error: No user name provided."

    # Render the login form for GET request
    return render_template('app.html')

if __name__ == '__main__':
    app.run(debug=True)

