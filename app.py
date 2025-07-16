from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)  # Initialize Flask app

# Route for Home page
@app.route('/')
def index():
    # Render the 'index.html' template for the homepage
    return render_template('index.html')

# Route for Courses page
@app.route('/courses')
def courses_page():
    # Render the 'courses.html' template for courses information
    return render_template('courses.html')

# Route for About page
@app.route('/about')
def about_page():
    # Render the 'about.html' template for about page
    return render_template('about.html')

# Route for Contact page
@app.route('/contact')
def contact_page():
    # Check if 'success' query parameter is 'true' to show a success message
    success = request.args.get('success') == 'true'
    # Render the 'contact.html' template, passing success flag for UI feedback
    return render_template('contact.html', success=success)

# Route to handle contact form submission via POST
@app.route('/submit', methods=['POST'])
def submit_form():
    # Retrieve form data submitted by the user
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Get current timestamp formatted as a string
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Prepare a formatted entry string to save
    entry = f"{timestamp} | {name} | {email} | {message}\n"

    # Define file path for storing submissions (in the same directory as this script)
    submissions_file = os.path.join(os.path.dirname(__file__), 'submissions.txt')

    # Open the submissions file in append mode and write the entry
    with open(submissions_file, 'a') as f:
        f.write(entry)

    # Redirect back to the contact page with a success flag and anchor to thank you section
    return redirect(url_for('contact_page', success='true') + '#thankyou')

# Run the Flask app on port 5000 in debug mode if this script is run directly
if __name__ == '__main__':
    app.run(debug=True, port=5000)
