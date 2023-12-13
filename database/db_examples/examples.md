1. Problem: Store and retrieve contact information (name, phone number).
Python Code:


```sql
# Create table: CREATE TABLE Contacts (ID INTEGER PRIMARY KEY, Name TEXT, Phone TEXT)
# Insert: INSERT INTO Contacts (Name, Phone) VALUES (?, ?)
# Query: SELECT * FROM Contacts
```

```python
import sqlite3

class ContactBook:
    def __init__(self):
        self.conn = sqlite3.connect('contact_book.db')
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Contacts (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Phone TEXT NOT NULL
            );
        ''')

    def add_contact(self, name, phone):
        self.conn.execute('INSERT INTO Contacts (Name, Phone) VALUES (?, ?)', (name, phone))
        self.conn.commit()

    def view_contacts(self):
        cursor = self.conn.execute('SELECT * FROM Contacts')
        return cursor.fetchall()

    def update_contact(self, contact_id, name, phone):
        self.conn.execute('UPDATE Contacts SET Name = ?, Phone = ? WHERE ID = ?', (name, phone, contact_id))
        self.conn.commit()

    def delete_contact(self, contact_id):
        self.conn.execute('DELETE FROM Contacts WHERE ID = ?', (contact_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

# Usage
contact_book = ContactBook()
contact_book.add_contact('John Doe', '1234567890')
print(contact_book.view_contacts())
contact_book.update_contact(1, 'Jane Doe', '0987654321')
contact_book.delete_contact(1)

```

2. Personal Library Catalog
Problem: Catalog books owned by a user with title, author, and genre.
Python Code:


```sql
# Create table: CREATE TABLE Books (ID INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Genre TEXT)
# Insert, Query operations similar to Contacts
3. Basic Inventory System
```

```python
import sqlite3

class LibraryCatalog:
    def __init__(self):
        self.conn = sqlite3.connect('library.db')
        self.create_table()

    def create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Books (
                BookID INTEGER PRIMARY KEY AUTOINCREMENT,
                Title TEXT NOT NULL,
                Author TEXT NOT NULL,
                Genre TEXT NOT NULL
            );
        ''')
        self.conn.commit()

    def add_book(self, title, author, genre):
        self.conn.execute('INSERT INTO Books (Title, Author, Genre) VALUES (?, ?, ?)', (title, author, genre))
        self.conn.commit()

    def view_books(self):
        cursor = self.conn.execute('SELECT * FROM Books')
        return cursor.fetchall()

    def update_book(self, book_id, title, author, genre):
        self.conn.execute('UPDATE Books SET Title = ?, Author = ?, Genre = ? WHERE BookID = ?', (title, author, genre, book_id))
        self.conn.commit()

    def delete_book(self, book_id):
        self.conn.execute('DELETE FROM Books WHERE BookID = ?', (book_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

# Usage
library = LibraryCatalog()
library.add_book('1984', 'George Orwell', 'Dystopian')
library.add_book('To Kill a Mockingbird', 'Harper Lee', 'Classic')
print(library.view_books())
library.update_book(1, '1984', 'George Orwell', 'Political Fiction')
library.delete_book(2)

```
Problem: Track inventory items with name, quantity, and category.
Python Code:


```sql
# Create table: CREATE TABLE Inventory (ItemID INTEGER PRIMARY KEY, Name TEXT, Quantity INTEGER, Category TEXT)
# CRUD operations
4. Employee Management System
```


Problem: Manage employee data including name, position, and department.
Python Code:


```sql
# Create table: CREATE TABLE Employees (EmployeeID INTEGER PRIMARY KEY, Name TEXT, Position TEXT, Department TEXT)
# CRUD operations
```

5. Event Registration System
Problem: Record event attendees, event names, and dates.
Python Code:


```sql
# Create table: CREATE TABLE Events (EventID INTEGER PRIMARY KEY, Name TEXT, Date TEXT)
# Create table: CREATE TABLE Attendees (AttendeeID INTEGER PRIMARY KEY, EventID INTEGER, AttendeeName TEXT, FOREIGN KEY (EventID) REFERENCES Events(EventID))
# CRUD operations
```

6. Student Grading System
Problem: Store and manage student grades for courses.
Python Code:


```sql
# Create tables: Students, Courses, Grades with relevant fields and relationships
# CRUD operations
```

7. Blogging Platform
Problem: Handle blog posts, authors, and comments.
Python Code:


```sql
# Create tables: Authors, Posts, Comments with relationships
# CRUD operations, especially complex READ queries for comments per post
```
```python
class BloggingPlatform:
    def __init__(self):
        self.conn = sqlite3.connect('blogging.db')
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Posts (
                PostID INTEGER PRIMARY KEY AUTOINCREMENT,
                Title TEXT NOT NULL,
                Content TEXT NOT NULL
            );
        ''')
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Comments (
                CommentID INTEGER PRIMARY KEY AUTOINCREMENT,
                PostID INTEGER NOT NULL,
                Comment TEXT NOT NULL,
                FOREIGN KEY (PostID) REFERENCES Posts(PostID)
            );
        ''')

    def add_post(self, title, content):
        self.conn.execute('INSERT INTO Posts (Title, Content) VALUES (?, ?)', (title, content))
        self.conn.commit()

    def add_comment(self, post_id, comment):
        self.conn.execute('INSERT INTO Comments (PostID, Comment) VALUES (?, ?)', (post_id, comment))
        self.conn.commit()

    def view_posts(self):
        cursor = self.conn.execute('SELECT * FROM Posts')
        return cursor.fetchall()

    def view_comments(self, post_id):
        cursor = self.conn.execute('SELECT * FROM Comments WHERE PostID = ?', (post_id,))
        return cursor.fetchall()

    def __del__(self):
        self.conn.close()

# Usage
blog = BloggingPlatform()
blog.add_post('My First Post', 'Content of the first post')
blog.add_comment(1, 'Great post!')
print(blog.view_posts())
print(blog.view_comments(1))

```
8. E-commerce Product Catalog
Problem: Catalog products with categories, descriptions, and prices.
Python Code:


```sql
# Create tables: Products, Categories, ProductCategories
# CRUD operations, including JOIN queries
```

9. Flight Booking System
Problem: Manage flights, passengers, and bookings.
Python Code:


```sql
# Create tables: Flights, Passengers, Bookings with relationships
# Complex CRUD, especially with booking transactions
```
```python
class FlightBookingSystem:
    def __init__(self):
        self.conn = sqlite3.connect('flights.db')
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Flights (
                FlightID INTEGER PRIMARY KEY AUTOINCREMENT,
                FlightNumber TEXT NOT NULL,
                Departure TEXT NOT NULL,
                Arrival TEXT NOT NULL
            );
        ''')
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Bookings (
                BookingID INTEGER PRIMARY KEY AUTOINCREMENT,
                FlightID INTEGER NOT NULL,
                PassengerName TEXT NOT NULL,
                FOREIGN KEY (FlightID) REFERENCES Flights(FlightID)
            );
        ''')

    def add_flight(self, flight_number, departure, arrival):
        self.conn.execute('INSERT INTO Flights (FlightNumber, Departure, Arrival) VALUES (?, ?, ?)', (flight_number, departure, arrival))
        self.conn.commit()

    def book_flight(self, flight_id, passenger_name):
        self.conn.execute('INSERT INTO Bookings (FlightID, PassengerName) VALUES (?, ?)', (flight_id, passenger_name))
        self.conn.commit()

    def view_flights(self):
        cursor = self.conn.execute('SELECT * FROM Flights')
        return cursor.fetchall()

    def view_bookings(self, flight_id):
        cursor = self.conn.execute('SELECT * FROM Bookings WHERE FlightID = ?', (flight_id,))
        return cursor.fetchall()

    def __del__(self):
        self.conn.close()

# Usage
flight_system = FlightBookingSystem()
flight_system.add_flight('AA123', 'New York', 'London')
flight_system.book_flight(1, 'John Doe')
print(flight_system.view_flights())
print(flight_system.view_bookings(1))

```
10. Hospital Management System
Problem: Track patients, doctors, and appointments.
Python Code:


```sql
# Create tables: Patients, Doctors, Appointments
# CRUD operations, focus on appointment scheduling logic
```

11. Online Learning Platform
Problem: Manage courses, students, and enrollments.
Python Code:


```sql
# Create tables: Courses, Students, Enrollments
# CRUD operations, handle many-to-many relationships
```

12. Real Estate Property Listings
Problem: Catalog properties, agents, and viewings.
Python Code:


```sql
# Create tables: Properties, Agents, Viewings
# Complex queries for matching properties with agent availability
```

13. Restaurant Reservation System
Problem: Handle table reservations, customer details, and dining times.
Python Code:


```sql
# Create tables: Customers, Tables, Reservations
# CRUD operations, focus on reservation time logic
```

14. Car Rental Service
Problem: Manage car rentals, customers, and rental agreements.
Python Code:


```sql
# Create tables: Cars, Customers, Rentals
# CRUD operations, handle rental period logic and availability
```

15. Movie Theater Seating
Problem: Track movie showings, seats, and bookings.
Python Code:


```sql
# Create tables: Movies, Showings, Seats, Bookings
# Complex CRUD for seat availability and booking
```

16. Fitness Club Membership Management
Problem: Manage club members, subscription plans, and facility access.
Python Code:


```sql
# Create tables: Members, Plans, AccessLogs
# CRUD operations, focus on membership status and access control
```

17. Museum Artwork Catalog
Problem: Catalog artworks, artists, and exhibition history.
Python Code:


```sql
# Create tables: Artworks, Artists, Exhibitions
# Complex queries for exhibition history
```

18. Project Management Tool
Problem: Track projects, tasks, and team assignments.
Python Code:


```sql  
# Create tables: Projects, Tasks, Teams, TeamMembers
# CRUD operations, focus on task dependencies and team assignments
```

19. Social Media Analytics
Problem: Analyze social media posts, user engagement, and trends.
Python Code:


```sql
# Create tables: Users, Posts, Reactions
# Complex queries for analytics, trend detection
```

20. Stock Market Trading Platform
Problem: Handle stock market trades, portfolios, and historical prices.
Python Code:


```sql
# Create tables: Stocks, Trades, Portfolios, Prices
# Complex CRUD, handle real-time data and portfolio valuation