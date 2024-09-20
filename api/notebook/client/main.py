import requests
import sys

API_URL = "http://127.0.0.1:8000/notes/"

def print_menu():
    print("\nNotebook CLI")
    print("1. List all notes")
    print("2. Create a new note")
    print("3. View a note")
    print("4. Update a note")
    print("5. Delete a note")
    print("6. Exit")

def list_notes():
    response = requests.get(API_URL)
    if response.status_code == 200:
        notes = response.json()
        if not notes:
            print("No notes found.")
        else:
            print("\nNotes List:")
            for note in notes:
                print(f"ID: {note['id']} | Title: {note['title']}")
    else:
        print(f"Failed to retrieve notes. Status code: {response.status_code}")

def create_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    response = requests.post(API_URL, params={"title": title, "content": content})
    if response.status_code == 200:
        print("Note created successfully.")
    else:
        print(f"Failed to create note. Status code: {response.status_code}")

def view_note():
    note_id = input("Enter note ID to view: ")
    response = requests.get(f"{API_URL}{note_id}")
    if response.status_code == 200:
        note = response.json()
        print(f"\nID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Content: {note['content']}")
    else:
        print(f"Note not found. Status code: {response.status_code}")

def update_note():
    note_id = input("Enter note ID to update: ")
    title = input("Enter new title (leave blank to keep unchanged): ")
    content = input("Enter new content (leave blank to keep unchanged): ")
    response = requests.put(f"{API_URL}{note_id}", params={"title": title, "content": content})
    if response.status_code == 200:
        print("Note updated successfully.")
    else:
        print(f"Failed to update note. Status code: {response.status_code}")

def delete_note():
    note_id = input("Enter note ID to delete: ")
    response = requests.delete(f"{API_URL}{note_id}")
    if response.status_code == 200:
        print("Note deleted successfully.")
    else:
        print(f"Failed to delete note. Status code: {response.status_code}")

def main():
    while True:
        print_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            list_notes()
        elif choice == "2":
            create_note()
        elif choice == "3":
            view_note()
        elif choice == "4":
            update_note()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            print("Exiting the application...")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
