# Restaurant Menu Flask CRUD

A simple web application for managing a restaurant menu using Flask and MySQL. This project provides CRUD (Create, Read, Update, Delete) operations for menu items.

## Features

- View all menu items
- Add new menu items
- Update existing menu items
- Delete menu items
- Simple web interface

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript

## Installation

1. **Clone the repository** (if applicable) or download the project files.

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Set up the database**:
   - Ensure MySQL is installed and running on your system.
   - Create the database by running the SQL script in `database.sql`:
     ```
     mysql -u root -p < database.sql
     ```
   - Update the database connection details in `app.py` if necessary (host, user, password).

4. **Run the application**:
   ```
   python app.py
   ```

5. **Access the application**:
   Open your web browser and go to `http://localhost:5000/p1`.

## Usage

- The main page displays the current menu items.
- Use the input fields to add new items.
- Click on items to edit or delete them (functionality implemented in the frontend).

## Project Structure

- `app.py`: Main Flask application with API endpoints.
- `database.sql`: SQL script to create the database and table.
- `requirements.txt`: Python dependencies.
- `public/`: Static files for the frontend.
  - `index.html`: Main HTML page.
  - `style.css`: Stylesheet.
  - `script.js`: JavaScript for frontend interactions.

## License

This project is open-source. Feel free to use and modify it.