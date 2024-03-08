import os
import subprocess
from gitpy import push, write, user, create

def main_menu():
    print("Welcome to the main menu:")
    print("1. Create repository")
    print("2. Write repository")
    print("3. Push repository")
    print("4. Set user information")
    print("0. Exit")

def create_repository():
    create.create_repository()

def write_repository():
    repo_name = input("Enter the repository name: ")
    write.write_repository(repo_name)

def push_repository():
    local_repo_name = input("Enter the local repository name: ")
    push.push_repository(local_repo_name)

def set_user_info():
    user.set_user_info()

if __name__ == "__main__":
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            create_repository()
        elif choice == "2":
            write_repository()
        elif choice == "3":
            push_repository()
        elif choice == "4":
            set_user_info()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")