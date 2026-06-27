# ATM Banking System

## Project Overview

A Python-based ATM Banking System that uses MySQL as the backend database. The project demonstrates database connectivity, account management, authentication, and core banking operations through a menu-driven interface.

## Technologies Used

* Python
* MySQL
* PyMySQL
* Git & GitHub
* PyCharm

---

## Features Implemented

### ✅ Account Creation

* Create new bank accounts
* Store account details in MySQL
* Duplicate account number validation

### ✅ Login Authentication

* Login using Account Number and PIN
* Account existence verification
* PIN validation
* Personalized welcome message

### ✅ Deposit Module

* Deposit money into an account
* Automatic balance update
* Database synchronization using SQL UPDATE

### ✅ Withdraw Module

* Withdraw money from an account
* Insufficient balance validation
* Automatic balance update

### ✅ Balance Enquiry

* View account holder details
* Display current account balance

### ✅ Menu-Driven Interface

* Interactive ATM menu
* Access all banking operations from a single application

### ✅ Modular Programming

* Separate Python modules for each feature
* Reusable database connection module

---

## Database Schema

### accounts

| Column  | Type    |
| ------- | ------- |
| acc_no  | Integer |
| name    | Varchar |
| pin     | Integer |
| balance | Float   |

---

## Project Structure

```text
ATM-Banking-System/

├── main.py
├── db_connection.py
├── create_account.py
├── login.py
├── deposit.py
├── withdraw.py
├── balance.py
└── README.md
```

---

## Current Progress

* ✅ Database Setup
* ✅ MySQL Connection
* ✅ Create Account Module
* ✅ Duplicate Account Validation
* ✅ Login Authentication
* ✅ Deposit Module
* ✅ Withdraw Module
* ✅ Balance Enquiry Module
* ✅ Menu-Driven ATM Application
* ✅ Modular Programming Structure
* ✅ Git & GitHub Version Control

---

## Upcoming Features

* Transaction History
* Mini Statement
* Date & Time Tracking
* Exception Handling
* Account PIN Change
* Object-Oriented Programming (OOP) Refactoring

---

## Concepts Practiced

### Python

* Variables
* Data Types
* Input / Output
* Conditional Statements
* Loops
* Functions
* Modules
* Modular Programming

### Database

* MySQL
* SELECT Queries
* INSERT Queries
* UPDATE Queries
* Database Connectivity using PyMySQL

### Tools

* Git
* GitHub
* PyCharm

---

## Learning Outcomes

This project helped in understanding:

* Python and MySQL integration
* Database-driven application development
* Modular programming
* Menu-driven application design
* Version control using Git and GitHub

