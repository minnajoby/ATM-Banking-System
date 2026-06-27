# ATM Banking System

## Project Overview

A Python-based ATM Banking System that uses MySQL as the backend database. The project demonstrates database connectivity, account management, authentication, and banking operations.

## Technologies Used

* Python
* MySQL
* PyMySQL
* Git & GitHub
* PyCharm

## Features Implemented

### ✅ Account Creation

* Create new account
* Store account details in MySQL
* Duplicate account number validation

### ✅ Login Authentication

* Login using Account Number and PIN
* Account existence verification
* PIN validation
* Personalized welcome message after successful login

### ✅ Database Module

* Separate database connection module (`db_connection.py`)
* Reusable connection function

## Database Schema

| Column  | Type    |
| ------- | ------- |
| acc_no  | Integer |
| name    | Varchar |
| pin     | Integer |
| balance | Float   |

## Project Structure

ATM-Banking-System/

* main.py
* db_connection.py
* create_account.py
* login.py
* README.md

## Current Progress

✅ Database Setup

✅ MySQL Connection

✅ Create Account Module

✅ Duplicate Account Validation

✅ Login Module

✅ GitHub Version Control

## Upcoming Features

* Deposit Money
* Withdraw Money
* Balance Enquiry
* Mini Statement
* Main Menu System

## Future Enhancements

* Transaction History
* PIN Change Facility
* Account Deletion
* User-Friendly Menu Interface
