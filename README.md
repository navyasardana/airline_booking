
````markdown
# Dream Airways – Airline Ticketing System

A Python and MySQL command-line project that simulates a basic airline ticketing system. It allows users to book tickets, calculate bills based on selected services, check ticket status, and cancel bookings, with data stored and managed using a MySQL database.

## Features

- Ticket Booking: Collects passenger details and generates a unique PNR  
- Billing: Calculates charges based on travel class, luggage selection, and optional in-flight menu items  
- Ticket Status Check: Allows users to check ticket status using PNR, email ID, or phone number  
- Cancellation: Updates ticket status to "Cancelled" upon user request  
- Database Initialization: Automatically sets up required tables (if not already created) on first run

## Tech Stack

- Programming Language: Python  
- Database: MySQL  
- Libraries Used: `pymysql`, `random`

## Setup Instructions

### Prerequisites

- Python 3.x installed  
- MySQL installed and running locally  
- `pymysql` library installed (`pip install pymysql`)

### Installation & Usage

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/airline-ticketing-system.git
   cd airline-ticketing-system
````

2. Edit MySQL Credentials

   Open the Python file and update the database connection details:

   ```python
   db = x.connect(host='localhost', user='root', password='your_password', db='flight')
   ```

3. Run the program

   Use the terminal or any Python IDE to run the script:

   ```bash
   python main.py
   ```

4. The program will:

   * Set up required tables if they don't exist
   * Offer a menu to book tickets, check status, or cancel bookings

## Project Structure

* `dab()`: Initializes the database and tables
* `booking()`: Handles passenger input and stores ticket data
* `bill()`: Adds cost of travel class, food, and luggage
* `status()`: Checks ticket status
* `cancel()`: Cancels bookings
* `main()`: Runs the application interface

## Notes

* The database and tables are created automatically on the first run
* This project is for educational purposes and demonstrates CRUD operations using Python and MySQL

```

