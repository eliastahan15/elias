library = []
first_book=input('Enter the name of a book you own: ').lower()
library.append(first_book)
second_book=input("Enter the name of another book you own or press 'Enter' or 'skip':").lower()

if second_book== "skip":
    print(f"your library is:{library}")
elif second_book != "":
    library.append(second_book)
    print(f"your library is:{library}")

wishlist = []
first_book_1=input("Enter the name of a book you wish to have in the future :").lower()
wishlist.append(first_book_1)
second_book_1=input("Enter the name of another book you wish to have (or press 'Enter' or 'skip'):").lower()

if second_book_1== "skip":
    print(f"your wishlist is:{wishlist}")
elif second_book_1 != "":
    wishlist.append(second_book_1)
    print(f"your wishlist is:{wishlist}")

acuired_book=input("""Enter the name of a book from your wishlist that you've 
acquired (or press'Enter to skip):""").lower()

if acuired_book in wishlist:
    wishlist.remove(acuired_book)
    library.append(acuired_book)
    print(f"your updated library is:{library}")
    print(f"your updated wishlist is:{wishlist}")
else:
    print(f"{acuired_book} is not in your wishlist. No changes made.")

donate_book=input("""Enter the name of a book from your library you wish 
to donate (or press 'Enter' to skip):""").lower()

if donate_book in library:
    library.remove(donate_book)
    print(f"Final Library after Donations:{library}")
else:
    print(f"{donate_book} is not in your library. No changes made.")