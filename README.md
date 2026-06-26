# ATM Banking System

## Project Overview

A Python-based ATM Banking System that uses MySQL as the backend database. The project demonstrates database connectivity, account management, and banking operations.

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
* README.md

## Upcoming Features

* Login Module
* Deposit Money
* Withdraw Money
* Balance Enquiry
* Mini Statement
