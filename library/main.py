from library import Library

def main():
    library = Library("Marand")

    while True:
        print("\n ___Library Management___")
        print("1. add a book")
        print("2. remove a book")
        print("3. search a book")
        print("4. show a book")
        print("5. exit")

        choice = input("Your choice: ")

        if choice == '1':
            title= input("Enter book name : ")
            author = input("Enter author name : ")
            print(library.add_book(title, author))
        
        elif choice == '2':
            title= input("Enter book name : ")
            author = input("Enter author name : ")
            print(library.remove_book(title, author))

        elif choice == '3':
            title= input("Enter book name : ")
            author = input("Enter author name : ")
            print(library.search_book(title, author))

        elif choice == '4':
            library.show_books()

        elif choice == '5':
            break

        else:
            print("unvalid number")


if __name__ == "__main__":
    main()