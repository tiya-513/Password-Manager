import json
import os
import random

def load_entries():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_entries(entries):
    with open("data.json", "w") as f:
        json.dump(entries, f)

def check_choice(choice):
    if choice == "about":
        print("Created by Rudrapriya Dutta")

    elif choice == "master password":
        print("Change master password: \n")
        user = input("Enter current master password: ")
        if mstr_pass["master_password"] == user:
            mstr_pass["master_password"] = input("Enter new master password: ")
            with open(file, "w") as f:
                json.dump(mstr_pass, f)
        else:
            print("Invalid master password. Not permitted to change.")

    elif choice == "help":
        help_data = {
            "about": "an about me page",
            "help": "displays this list",
            "list": "lists all users",
            "master password": "change master password",
            "entry": "New entry, takes in website name, username, and password",
            "show <ID_xxxx>": "displays an entry of the corresponding ID",
            "update <ID_xxxx>": "updates the entry of the corresponding ID",
            "delete <ID_xxxx>": "deletes a specific entry"
        }
        for d in help_data:
            print(d)
            print("\t", help_data[d], "\n")

    elif choice == "entry":
        data = {
            "Website": input("Enter website: "),
            "Username": input("Enter username: "),
            "Password": input("Enter password: "),
            "ID": random.randint(1000, 9999)
        }

        entries = load_entries()
        entries.append(data)
        save_entries(entries)

        print("New entry created")

    elif choice == "list":
        print("Existing users: ")
        entries = load_entries()

        for i, entry in enumerate(entries, start=1):
            print(f"Entry {i}:")
            print(f"Website  : {entry['Website']}")
            print(f"Username : {entry['Username']}")
            print(f"ID       : {entry['ID']}")

    elif choice.startswith("show "):
        entry_id = choice.split(" ", 1)[1]
        entries = load_entries()

        found = False
        for entry in entries:
            if str(entry["ID"]) == entry_id:
                print(f"Website : {entry['Website']}")
                print(f"Username: {entry['Username']}")
                print(f"Password: {entry['Password']}")
                found = True
                break

        if not found:
            print("Entry not found")

    elif choice.startswith("update "):
        entry_id = choice.split(" ", 1)[1]
        entries = load_entries()

        found = False
        for entry in entries:
            if str(entry["ID"]) == entry_id:
                print("Leave empty for no change")

                website = input(f"Website ({entry['Website']}): ")
                username = input(f"Username ({entry['Username']}): ")
                password = input("Password (********): ")

                if website != "":
                    entry["Website"] = website
                if username != "":
                    entry["Username"] = username
                if password != "":
                    entry["Password"] = password

                save_entries(entries)
                print(f"Updated entry {entry_id}!")
                found = True
                break

        if not found:
            print("Entry not found")

    elif choice.startswith("delete "):
        entry_id = choice.split(" ", 1)[1]
        entries = load_entries()

        found = False
        for entry in entries:
            if str(entry["ID"]) == entry_id:
                print("Deleting the following entry")
                print(f"Website : {entry['Website']}")
                print(f"Username: {entry['Username']}")

                confirm = input("type the word DELETE for confirmation: ")

                if confirm == "DELETE":
                    entries.remove(entry)
                    save_entries(entries)
                    print(f"Deleted {entry_id} successfully!")
                else:
                    print("Delete cancelled")

                found = True
                break

        if not found:
            print("Entry not found")

    else:
        if choice.strip() != "":
            print("Invalid input")


file = "x.json"

if os.path.exists(file):
    with open(file, "r") as f:
        mstr_pass = json.load(f)
else:
    mstr_pass = {"master_password": ""}

if not mstr_pass.get("master_password"):
    mstr_pass["master_password"] = input("New usage detected, create a master password: ")
    with open(file, "w") as f:
        json.dump(mstr_pass, f)

approved = False

for i in range(3):
    user = input("Enter current master password: ")

    if mstr_pass["master_password"] == user:
        print("Welcome to password manager!")

        while True:
            try:
                choice = input("~$ ")
                check_choice(choice)
            except KeyboardInterrupt:
                print("\nExiting your password manager")
                break

        approved = True
        break

if approved == False:
    print("Wrong master password. Failed to login.")