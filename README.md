# python-test-rajat
Python Developer Technical Test Statement 
This test is designed to assess a candidate’s abilities in:
•	Backend development using Python (with Flask or Django),
•	CRUD operations with database integration,
•	Validations,
•	Use of master-detail (cross-table) relationships (e.g., dropdowns populated from a master table).
________________________________________
🧪 Python Developer Technical Test Statement
Objective:
Develop a simple web-based Python application that performs CRUD operations on a transaction table, and master table, referencing a master table for dropdown selections. This test will evaluate your understanding of front-end validations, backend logic, validations, data relationships, and overall application structure.
________________________________________
🔧 Test Scenario: Inventory Entry System
You are required to create a small application to manage product purchase entries. The application will use two tables:
1. Master Table – Suppliers
Column	Type	Description
id	Integer (PK)	Auto-increment primary key
name	String	Name of the supplier
email	String	Unique, Valid email format
GSTIN	String	Unique, Valid GSTIN Format
is_active	Boolean	Active status
2. Transaction Table – PurchaseEntries
Column	Type	Description
id	Integer (PK)	Auto-increment primary key
invoice_no	String	Invoice number, required
supplier_id	Integer (FK)	Foreign Key linked to Suppliers.id
date	Date	Required, not in the future
amount	Float	Required, must be positive
________________________________________
✅ Functional Requirements
1.	Add Supplier
o	Validate for unique email and proper format.
o	Must be able to activate/deactivate a supplier.
2.	Add Purchase Entry
o	Dropdown for selecting Supplier (only active ones).
o	Validate invoice_no, date, and amount.
o	Prevent duplicate invoice_no.
3.	CRUD Operations
o	Implement Create, Read, Update, and Delete for both Suppliers and PurchaseEntries.
4.	Validations
o	All fields are mandatory unless marked otherwise.
o	Use both frontend (if applicable) and backend validations.
5.	Optional (Bonus):
o	Display supplier name in listing instead of just ID.
o	Add a search/filter on supplier name in transaction list.
________________________________________
📦 Technology Requirements
•	Python with Flask or Django (your choice)
•	SQLite/PostgreSQL/MySQL
•	Use SQLAlchemy or Django ORM
•	RESTful APIs (if applicable)
•	HTML forms or Postman collection for testing endpoints

