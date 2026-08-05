
# Contact Book

A simple **Contact Book application built using Python**.  
This project allows users to add, view, search, delete, and edit contacts, as well as check the total number of saved contacts.

The project uses a simple text file (`contact_file.txt`) to store contact information instead of a database.

---

##  Features

-  Add a new contact
-  View all contacts
-  Search for a contact by name
-  Delete a contact
-  Edit/update an existing contact
-  Count total number of contacts
-  Exit the application
-  Basic unit testing using Python's `unittest` module
-  Persistent data storage using a text file

---

## Technologies Used

- **Python 3**
- **File Handling**
- **Functions**
- **Loops and Conditional Statements**
- **Exception Handling**
- **Unit Testing**
- Python `unittest` module

---

##  Project Structure

```text
Contact-Book/
│
├── contact_book.py
├── test_contact_book.py
└── contact_file.txt
data.txt
practice_file_io.py
practice_oop.py
README.md
````

### File Description

| File                   | Description                                               |
| ---------------------- | --------------------------------------------------------- |
| `contact_book.py`      | Main Python program containing all Contact Book functions |
| `test_contact_book.py` | Unit tests for testing contact operations                 |
| `contact_file.txt`     | Text file used to store contact information               |
| `README.md`            | Documentation for the project                             |

---

## How It Works

The program stores each contact in the following format:

```text
Name: Aditya
Mobile number: 9876543210
Email: aditya@gmail.com

```

Each contact occupies **4 lines** in the text file:

1. Name
2. Mobile number
3. Email
4. Blank line

The program uses this structure to search, edit, delete, and count contacts.

---

## Getting Started

### 1. Clone the Repository

Clone this repository using:

```bash
git clone <your-repository-url>
```

### 2. Enter the Project Folder

```bash
cd Contact-Book
```

### 3. Run the Program

```bash
python3 contact_book.py
```

---

## Main Menu

When the program starts, the following menu is displayed:

```text
- - - - - - - - - - - Contact Book - - - - - - - - - -

1. Add Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Edit Contact
6. Total Number of Contacts
7. Exit

--------------------------------------------------------

Enter Your Choice :
```

---

## Available Operations

### 1. Add Contact

Allows the user to enter:

* Name
* Mobile number
* Email

Example:

```text
Enter your name : Aditya
Mobile number : 9876543210
Email : aditya@gmail.com

Details added!
```

The contact is then stored in `contact_file.txt`.

---

### 2. View All Contacts

Displays all contacts currently stored in the contact file.

Example:

```text
Name: Aditya
Mobile number: 9876543210
Email: aditya@gmail.com

Name: Rahul
Mobile number: 1235678904
Email: rahul@gmail.com
```

---

### 3. Search Contact

Searches for a contact using the name entered by the user.

Example:

```text
Enter name : Rahul

Contact found!

Name: Rahul
Mobile number: 1235678904
Email: rahul@gmail.com
```

The search is **case-insensitive**, so searching for:

```text
rahul
```

can also find:

```text
Rahul
```

---

### 4. Delete Contact

Deletes a contact based on the name entered by the user.

Example:

```text
Enter Contact Name to Delete : Rahul

Contact Found!
Name: Rahul
Mobile number: 1235678904
Email: rahul@gmail.com

Contact Deleted Successfully!
```

If the contact does not exist:

```text
Contact Not Found!
```

---

### 5. Edit Contact

Allows the user to update an existing contact.

The user can change:

* Name
* Mobile number
* Email

Example:

```text
Enter name to edit : Aditya

Enter New Name : Aditya Waghumbare
Enter New Mobile Number : 9999999999
Enter New Email : aditya@example.com

Contact Updated Successfully!
```

---

### 6. Total Number of Contacts

Counts the total number of contacts stored in `contact_file.txt`.

Example:

```text
Total number of Contacts : 4
```

The program counts the number of lines and divides it by `4`, because each contact occupies four lines.

---

### 7. Exit

Exits the Contact Book application.

---

## Testing

This project includes basic unit tests using Python's built-in `unittest` module.

The tests currently check:

* Adding a contact
* Deleting a contact

### Run Tests

Use:

```bash
python3 -m unittest test_contact_book.py
```

or:

```bash
python3 test_contact_book.py
```

### Expected Output

A successful test run should look similar to:

```text
..
----------------------------------------------------------------------
Ran 2 tests in 0.00s

OK
```

---

## Functions

The main program contains the following functions:

```python
add_contact()
view_contacts()
search_contact()
delete_contact()
edit_contacts()
total_contacts()
```

### `add_contact()`

Adds a new contact to `contact_file.txt`.

### `view_contacts()`

Reads and displays all stored contacts.

### `search_contact()`

Searches for a contact by name.

### `delete_contact()`

Finds and removes a contact from the file.

### `edit_contacts()`

Updates the information of an existing contact.

### `total_contacts()`

Calculates and displays the total number of contacts.

---

## Data Storage

This project does not use a database.

Instead, contact information is stored in:

```text
contact_file.txt
```

Example:

```text
Name : adi
Mobile number : 9876543210
Email : aditya@gmail.com

Name: Kapil
Mobile number: 1234567890
Email: kapil@gmail.com

Name: Rahul
Mobile number: 1235678904
Email: rahul@gmail.com
```

---

## Concepts Practiced

This project was created to practice fundamental Python programming concepts such as:

* Variables
* Functions
* User input
* `if-elif-else`
* `while` loops
* `for` loops
* String manipulation
* File handling
* Reading and writing files
* Exception handling
* `try-except`
* Boolean variables
* Lists
* Python modules
* Unit testing
* `unittest`
* Basic CRUD operations

---

## CRUD Operations

The Contact Book implements the basic **CRUD** operations:

| CRUD       | Operation           | Function                               |
| ---------- | ------------------- | -------------------------------------- |
| **Create** | Add contact         | `add_contact()`                        |
| **Read**   | View/Search contact | `view_contacts()` / `search_contact()` |
| **Update** | Edit contact        | `edit_contacts()`                      |
| **Delete** | Delete contact      | `delete_contact()`                     |

---

## Current Limitations

This is a beginner-level project and currently has some limitations:

* Contacts are stored in a plain text file.
* There is no database.
* Mobile numbers and email addresses are not validated.
* Duplicate contacts can be added.
* Search is based on the contact name.
* The application runs in the terminal.
* The data format depends on each contact occupying exactly four lines.

---

## Future Improvements

Possible improvements for future versions include:

* [ ] Add mobile number validation
* [ ] Add email validation
* [ ] Prevent duplicate contacts
* [ ] Improve search functionality
* [ ] Add partial-name search
* [ ] Add contact IDs
* [ ] Store data using JSON
* [ ] Use SQLite database
* [ ] Add a graphical user interface (GUI)
* [ ] Add sorting contacts alphabetically
* [ ] Add multiple search filters
* [ ] Improve error handling
* [ ] Add more unit tests

---

## 👨‍💻 Author

**Aditya Waghumbare**

Python beginner project developed to practice:

```text
Python
File Handling
Functions
CRUD Operations
Unit Testing
```

---

## License

This project is created for **learning and educational purposes**.

```
```
