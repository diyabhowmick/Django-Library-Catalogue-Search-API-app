# Django-Library-Catalogue-Search-API-app

1. Introduction:

The Library Catalog Search project aims to provide users with a convenient and efficient way to search for books in a library catalog. The project includes a web application where users can enter book titles and search for relevant information about the books available in the library.

2. Features:

Search for Books: Users can search for books by entering the title of the book in the search form.
Display Book Details: After performing a search, users can view detailed information about the books, including the title, author, ISBN, genre, and publication date.
Responsive Design: The web application is designed to be responsive, ensuring optimal viewing experience across various devices and screen sizes.
3. Technologies Used:

Django: Django is a high-level Python web framework used for rapid development of web applications.
Bootstrap: Bootstrap is a front-end framework for developing responsive and mobile-first websites.
SQLite: SQLite is a lightweight, serverless relational database management system used for storing book information.
Python Requests: Python Requests library is used for making HTTP requests to the backend server to fetch book details based on user search queries.
4. Project Structure:

index.html: This file contains the HTML markup for the search form where users can enter book titles.
results.html: This file displays detailed information about the books based on user search queries.
views.py: This Python file contains the Django view functions responsible for handling user requests, fetching book details from the backend server, and rendering HTML templates.
5. Installation:

To run the Library Catalog Search project locally, follow these steps:

Clone the project repository from GitHub: [Project Repository URL]
Install Python and Django if not already installed on your system.
Install required Python packages using pip:
Copy code
pip install django requests
Run the Django development server:
Copy code
python manage.py runserver
Access the web application in your browser at http://localhost:8000.
6. Usage:

Open the web application in your browser.
Enter the title of the book you want to search for in the search form and click the "Search" button.
View detailed information about the books matching your search query on the results page.
7. Conclusion:

The Library Catalog Search project provides a simple yet effective solution for searching and accessing information about books in a library catalog. With its user-friendly interface and responsive design, users can easily find the books they are looking for and access relevant details with ease.

