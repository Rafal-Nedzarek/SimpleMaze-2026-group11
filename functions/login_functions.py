# -----------------------------------------------------------------------------
# File: login_functions.py
# ACS School Project - Simple Maze Example
# Organization: THUAS (The Hague University of Applied Sciences)
# Location: Delft
# Date: October 2026
# -----------------------------------------------------------------------------

import sqlite3
import sys
from functions import shared_functions as sf

db_path = "database/Accounts.db"

def enterChoice():
    keep_asking = True
    while keep_asking:
        try:
            choice = input("\nDo you want to login or register (type ? for help): ").strip().lower()
            if choice == "login":
                keep_asking = False
            elif choice == "register":
                keep_asking = False
            elif choice == "?":
                sf.show_help_text_start()
            elif choice == "quit":
                print("\nYou leave the school and the adventure comes to an end. Goodbye!")
                sys.exit()
            else:
                raise ValueError("\nInvalid option, type ? to see the available commands.")
        except ValueError as error:
            print(error)
    return choice

def usernameExists(username):
    with sqlite3.connect(db_path) as connection:
        row = connection.execute(
            "SELECT player_id FROM accounts WHERE player_username = ?",
            (username,)
        ).fetchone()
    return row is not None

def checkUsername(username):
    if len(username) < 3:
        raise ValueError("\nUsername needs at least 3 characters.")
    for char in username:
        if char == " ":
            raise ValueError("\nUsername can't contain spaces.")
        if not char.isalnum() and char not in "@!#$%&-_+":
            raise ValueError(
                f"\nInvalid symbol '{char}' in username. Use only letters, numbers and @ ! # $ % & - _ +")

def checkPassword(password):
    has_capital = False
    has_number = False
    has_symbol = False
    for char in password:
        if char.isupper():
            has_capital = True
        if char.isdigit():
            has_number = True
        if not char.isalnum():
            has_symbol = True

    errors = []
    if len(password) < 8:
        errors.append("- at least 8 characters")
    if not has_capital:
        errors.append("- at least one capital letter")
    if not has_number:
        errors.append("- at least one number")
    if not has_symbol:
        errors.append("- at least one special symbol: @!#$%&-_+")

    if errors:
        raise ValueError("\nYour password needs:\n" + "\n".join(errors))

def login():
    username = input("Username: ").strip()
    password = input("Password: ")

    with sqlite3.connect(db_path) as connection:
        row = connection.execute(
            "SELECT password FROM accounts WHERE player_username = ?",
            (username,)
        ).fetchone()
    if row is None:
        print(f"\nThe username '{username}' doesn't exist.")
        return None
    elif row[0] != password:
        print("\nWrong password.")
        forgot = input("Have you forgotten your password? yes/no: ").strip().lower()
        if forgot in ["yes", "y"]:
            print("\nPlease contact one of the game admins to get your password.")
            sys.exit()
        return None
    else:
        print(f"\nWelcome back, {username}!")
        return username

def register():
    try:
        username = input("Create username: ").strip()
        checkUsername(username)
        if usernameExists(username):
            raise ValueError(f"\nThe username '{username}' is already taken.")
        password = input("Create password: ")
        checkPassword(password)
        with sqlite3.connect(db_path) as connection:
            connection.execute(
                "INSERT INTO accounts (player_username, password) VALUES (?, ?)",
                (username, password))
        print(f"\nAccount '{username}' created! Welcome, {username}!")
        return username # success
    except ValueError as error:
        print(error)
        return None # error

def getUser():
    sf.schoolMaze()
    while True:
        choice = enterChoice()
        if choice == "login":
            player = login()
        elif choice == "register":
            player = register()

        if player is not None:
            return player