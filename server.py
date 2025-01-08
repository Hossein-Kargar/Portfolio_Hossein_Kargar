from flask import Flask, request, render_template, redirect
import csv



app = Flask(__name__)

@app.route("/")
def my_home():
    """
    Represents the route for the home page of a Flask application.

    This function acts as the endpoint for the root URL of the application, serving
    the index HTML page when accessed.

    :return: HTML content rendered from the "index.html" template.
    :rtype: str
    """
    return render_template("index.html")

@app.route("/<string:page_name>")
def about(page_name):
    """
    Renders a template for a given page.

    This function takes a `page_name` parameter that corresponds to
    the name of a specific page template and returns a rendered
    template as a response.

    :param page_name: The name of the page template to be rendered
    :type page_name: str
    :return: A rendered page template
    :rtype: Response
    """
    return render_template(page_name)

def write_to_file(data):
    """
    Appends the provided data to a text file named 'database.txt'. The data should
    contain specific keys ('email', 'subject', and 'message') to format and store
    relevant information properly.

    The function opens the file in append mode, ensuring that new entries are added
    without overwriting existing content. Each piece of information is extracted
    from the input dictionary, formatted, and written as a new line in the file.

    :param data: The dictionary containing data to write, must include keys
                 'email', 'subject', and 'message'.
                 - email: str, the email address to store
                 - subject: str, the subject of the message
                 - message: str, the message content

    :return: None
    """
    with open('database.txt', mode='a', newline = '') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    """
    Writes the provided data to a CSV file named 'database.csv'. The function appends
    data to the file if it already exists or creates a new file. The data is expected
    to contain keys "email", "subject", and "message", which are written as a row in
    the CSV file.

    :param data: A dictionary containing keys "email", "subject", and "message".
    :type data: dict
    """
    with (open('database.csv', mode='a') as database2):
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """
    Handles form submission by accepting POST and GET requests, extracting form data,
    writing the data to a CSV file in case of a POST request, and redirecting the user
    to a thank you page. For a GET request, it returns an error message.

    :param request: Represents the incoming HTTP request object, used to handle form
        data and request methods.
    :return: For a POST request, redirects the user to a thank you HTML page if data
        is successfully processed and stored. If an exception occurs during storage,
        it returns an error message. For a non-POST request, it returns a generic error
        message.
    """
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'
