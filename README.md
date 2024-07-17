## Introduction
This project is a Django web application designed to manage an online library system where administrators can manage books, authors, and their borrow records. The application allows admins to add books, authors, and assign books to authors. Additionally, admins can export the library data to an Excel sheet.

## Features
- **Models**: Three main models - Author, Book, and BorrowRecord.
- **Forms**: Custom forms for adding authors, books, and borrow records with validation.
- **Views**: Views for adding and listing authors, books, and borrow records. Includes pagination.
- **Export to Excel**: Export author, book, and borrow record data to separate sheets in an Excel file.
- **Error Handling**: User notifications and error handling for form submissions and actions.
- **Best Practices**: Follows Django best practices and conventions, using class-based views (CBVs) wherever possible.

## Requirements
- Python 3.x
- Django 3.x or later
- django-excel or Django's built-in support for Excel file generation

## Setup Instructions
1. **Clone the Repository**
    ```bash
    git clone (https://github.com/azhannnnn/hackerkernal-task2.git)
    cd project
    ```

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations**
    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

7. **Access the Application**
    Open your web browser and navigate to `http://127.0.0.1:8000`.

## Project Structure
- **models.py**: Defines the Author, Book, and BorrowRecord models.
- **forms.py**: Contains forms for adding authors, books, and borrow records.
- **views.py**: Implements views to handle adding and listing authors, books, and borrow records, as well as exporting data to Excel.
- **templates/**: HTML templates for rendering views.
- **urls.py**: URL routing for the application.
- **static/**: Static files (CSS, JavaScript, images).

## Models
### Author
- `name` (CharField)
- `email` (EmailField)
- `bio` (TextField)
- Auto-generated ID

### Book
- `title` (CharField)
- `genre` (CharField)
- `published_date` (DateField)
- `author` (ForeignKey to Author)
- Auto-generated ID

### BorrowRecord
- `user_name` (CharField)
- `book` (ForeignKey to Book)
- `borrow_date` (DateField)
- `return_date` (DateField)
- Auto-generated ID

## Forms
- **Add Author Form**: Fields for name, email, and bio. Includes email validation.
- **Add Book Form**: Fields for title, genre, published_date, and a dropdown to select an author.
- **Add BorrowRecord Form**: Fields for user_name, book, borrow_date, and return_date.

## Views
- **Add Author**: Form to add an author.
- **Add Book**: Form to add a book.
- **Add BorrowRecord**: Form to add a borrow record.
- **List Authors**: Paginated list of authors.
- **List Books**: Paginated list of books.
- **List BorrowRecords**: Paginated list of borrow records.
- **Export to Excel**: Export data to separate sheets in an Excel file.

## Pagination
Utilizes Django's built-in pagination feature to paginate the lists of authors, books, and borrow records.

## Export to Excel
Implements functionality to export author, book, and borrow record data to separate sheets in an Excel file using `django-excel` or Django's built-in support for Excel file generation.

## Best Practices
- Utilizes Django's ORM and framework features.
- Implements class-based views (CBVs) wherever possible.
- Includes appropriate error handling and user notifications.

## Submission
Ensure your project is thoroughly tested and follows best practices before submission. Provide a link to your GitHub repository containing the project code. 

---
