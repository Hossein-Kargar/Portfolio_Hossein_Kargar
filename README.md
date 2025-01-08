# Flask Web Application with Form Submission

This project is a simple **Flask web application** that serves HTML pages and processes user-submitted form data. The
application saves the submitted form data into both a text file (`database.txt`) and a CSV file (`database.csv`) for
record-keeping.

## Features

- Serve static and dynamic HTML pages.
- Process and store form submissions (email, subject, and message).
- Save form data to a text file (`database.txt`) and a CSV file (`database.csv`).
- Handle routes dynamically for different HTML pages.
- Includes error handling for file operations and form submissions.

---

## Prerequisites

Before running the project, ensure you have the following installed:

1. **Python** (Version 3.6 or higher recommended)
2. **pip** (Python package manager)

---

## Installation

Follow these steps to set up and run the application locally:

1. **Clone the Repository**  
   Clone the repository onto your local machine using the following command:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a Virtual Environment** (optional but recommended)  
   Run the following commands:
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Linux or macOS
   venv\Scripts\activate           # On Windows
   ```

3. **Install Dependencies**  
   Install the required Python packages by running:
   ```bash
   pip install flask
   ```

4. **Run the Flask Application**  
   Start the application locally:
   ```bash
   python server.py
   ```
   By default, the application runs on `http://127.0.0.1:5000/`.

5. **Access the Application**  
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## File Structure

Below is an overview of the important files in this project:
