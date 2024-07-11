# Personal Journaling Django Backend App

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)

## Overview

This is a backend application built using Django that allows users to manage their personal journal entries. Users perform all the CRUD operations on journal entries, as well as fetch summary of their journal entries over a selected period but first they have to be authenticated.

## Features

- User registration and authentication
- Update user details i.e Usernames & Password
- Create, read, update, and delete journal entries
- Fetch summary of journal entries over a selected period (daily, weekly, monthly)

## Prerequisites

- Python 3.10 or higher installed on your machine
- Postgresql database version 16 preferably
- pgAdmin4 (optional)
- Postman (optional)

## Installation

0. Create project folder:
   ```bash
   cd <project directory>
   mkdir KGGeorge
   cd KGGeorge
   ```
1. Clone the repository:
   ```bash
   git clone https://github.com/GjoeKariuki/backend-journaling-shamiri.git
   cd backend-journaling-shamiri.git
   ```
2. Create virtual environment
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Create a `.env` file in the root directory of the project and add the following environment variables

   ```
   SECRET_KEY='django-insecure-^$#ol$l29@6vkw)!r%m%v^%er!511b410quq%v6g9kehr$a_&6'
   DEBUG=True

   DB_NAME=MyJournals
   DB_USER=postgres
   DB_PASSWORD=@2024#ND
   DB_HOST=localhost
   DB_PORT=5432

   ```

4. Install libraries
   ```
   pip install -r requirements.txt
   ```
5. Make migrations
   ```
   python manage.py makemigrations users
   python manage.py makemigrations journals
   ```
6. Run migrations
   ```
   python manage.py migrate users
   python manage.py migrate journals
   ```
7. Start the server
   ```
   python manage.py runserver
   ```
