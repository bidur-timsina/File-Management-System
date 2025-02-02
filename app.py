import os

def create_file(filename):
    try:
        with open(filename, 'x') as file:
            print(f"File {filename} created successfully")
    except FileExistsError:
        print(f"File {filename} already exists")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_all_file():
    files = os.listdir()
    if not files:
        print("No files found")
    else:
        print("Files found:")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"f{filename} deleted successfully")
    except FileNotFoundError:
        print(f"File {filename} not found")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(filename):
    try:
        with open('sample.txt', 'r') as file:
            content = file.read()
            print("content of file:" + content)
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def edit_file(filename):
    try:
        with open('sample.txt','a') as file:
            content = input("Enter the content you want to add:")
            file.write(content + "\n")
            print("Content added successfully")
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("File Management System")
        print("1. Create file")
        print("2. View all files")
        print("3. Delete file")
        print("4. Read file")
        print("5. Edit file")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            filename = input("Enter the name of the file: ")
            create_file(filename)
        elif choice == '2':
            view_all_file()
        elif choice == '3':
            filename = input("Enter the name of the file: ")
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter the name of the file: ")
            read_file(filename)
        elif choice == '5':
            filename = input("Enter the name of the file: ")
            edit_file(filename)
        elif choice == '6':
            print("closing the program ................ ")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()