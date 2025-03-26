Library Management System - Odoo Module

Overview

This Odoo module implements a Library Management System with the following functionalities:

CRUD Operations: Create, Read, Update, and Delete for books and borrow records.

Pop-up Modal for Reminders: A reminder email is triggered when the return date is exceeded.

Overdue Fee Calculation: Automatic calculation of total fees if the return date is exceeded.

Permission Management: Access control using user groups, specifically a 'Librarian' group.

Features

1. CRUD Functionality

Manage books, members, and borrow records.

Users with the right permissions can add, edit, and delete records.

2. Return Date Reminder

A pop-up modal appears when a book return is overdue.

The system sends automated email reminders to the borrower.

3. Overdue Fee Calculation

If a book is returned past its due date, a fee is calculated automatically.

The fee is based on the number of overdue days.

4. Group-Based Permissions

Librarian Group: Has full control over book management and borrow records.

Regular Users: Can view books but have restricted permissions for borrow operations.

Installation

Clone the repository:

git clone [https://github.com/yourusername/library-management-odoo.git]

Move the module to your Odoo custom addons directory:

mv library_management odoo/addons/

Restart the Odoo server:

odoo-bin -c odoo.conf -u library_management

Configuration

Assign users to the Librarian group via Settings > Users & Companies > Users.

Configure email settings in Settings > Technical > Outgoing Mail Servers for reminders.

Usage

Navigate to Library Management in the Odoo menu.

Add books and borrowers.

Issue books with a due date.

The system will track due dates and send reminders for overdue books.

Late return fees will be automatically calculated and displayed.

Screenshots

(Add relevant screenshots of the module here)

Contributing

Feel free to contribute by submitting issues or pull requests. Follow Odoo best practices for module development.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Author Ahmed Nouri

Developed by anouri339@gmail.com. For inquiries, contact anouri339@gmail.com.
