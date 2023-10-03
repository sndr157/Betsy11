
```markdown
## Betsy - Product Management System

Betsy is a Python-based product management system that allows you to manage users, products, tags, and transactions. It provides a simple command-line interface for performing various operations on your product database.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Populating Test Data](#populating-test-data)
- [Running the Application](#running-the-application)
- [Available Operations](#available-operations)
- [Project Structure](#project-structure)
- [Issues and Solutions](#issues-and-solutions)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.x
- Pip (Python package manager)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/betsy.git
   cd betsy
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## **Usage**

### **Populating Test Data**

Before running the application, you can populate the database with sample data:

```bash
python populate_test_data.py
```

### **Running the Application**

You can run the Betsy application using the following command:

```bash
python main.py
```

### **Available Operations**

- **Show Data**: Display current data in the database, including users, tags, products, and transactions.

- **Search Product by Term**: Search for products by name or description.

- **Search Product by User**: List products sold by users with a given name.

- **Search Product by Tag**: List products with a specific tag.

- **Add Product User**: Attach a seller to a product.

- **Remove Product User**: Remove a seller from a product.

- **Update Quantity**: Update the quantity of a product.

- **Purchase**: Record a purchase transaction.

## **Project Structure**

The project is organized into the following modules:

- **models.py**: Defines the database schema using the Peewee ORM.

- **main.py**: Entry point for running the application and interacting with the database.

- **functions.py**: Contains utility classes and methods for querying the database.

- **populate_test_data.py**: Populates the database with sample data for testing.

## Issues and Solutions

For a detailed list of issues and their corresponding solutions, refer to the [Issues and Solutions](#issues-and-solutions) section in this README.

## **Contributing**

Contributions are welcome! If you'd like to contribute to the project, please contact me directly, check my bio for contact information.

## **Img speak louder than words**

![image](https://github.com/sndr157/Betsy11/assets/127830026/b26d14ae-8312-4a9a-92df-0b2087b430a9)


![image](https://github.com/sndr157/Betsy11/assets/127830026/86e81376-8549-4ad6-8bfc-2eeb19834b2b)


![image](https://github.com/sndr157/Betsy11/assets/127830026/69b2b377-ba61-467c-88c6-dc77a3909014)


![image](https://github.com/sndr157/Betsy11/assets/127830026/e866c155-eb15-4d7e-891d-f559c20691f9)


![image](https://github.com/sndr157/Betsy11/assets/127830026/204dcf7b-8927-4df8-bc20-f9272d138f82)




