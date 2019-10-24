from tkinter import *
from database import DB
from functools import partial


class BookFrame:
    def __init__(self, win, db):
        self.main_frame = win
        self.db = db
        self.books_container = None

    def load_book_content(self):
        books_container_frame = LabelFrame(
            self.main_frame, text="Books")
        books_container_frame.pack(fill="both", expand="yes")
        self.books_container = books_container_frame

        left_frame = Frame(books_container_frame)
        left_frame.pack(side=LEFT, padx=20)

        right_frame = Frame(books_container_frame)
        right_frame.pack(side=RIGHT, padx=20)

        book_input_frame = LabelFrame(
            right_frame, text="New Book", font="Helvetica 12 bold",
            borderwidth=0, highlightthickness=0
        )
        book_input_frame.pack(side=LEFT, padx=20)

        book_delete_frame = LabelFrame(
            right_frame, text="Delete Book", font="Helvetica 12 bold",
            borderwidth=0, highlightthickness=0
        )
        book_delete_frame.pack(side=LEFT, padx=20)

        self.__process_books_data(left_frame)

        self.__create_frame_input_new_category(book_input_frame)

        self.__create_frame_delete_book(book_delete_frame)

    def __process_books_data(self, frame):
        books = self.db.get_books()

        title_frame = LabelFrame(
            frame, text="Title", font="Helvetica 12 bold",
            borderwidth=0, highlightthickness=0)
        title_frame.pack(side=LEFT, padx=20)

        author_frame = LabelFrame(
            frame, text="Author", font="Helvetica 12 bold",
            borderwidth=0, highlightthickness=0)
        author_frame.pack(side=LEFT, padx=20)

        genre_frame = LabelFrame(
            frame, text="Genre", font="Helvetica 12 bold",
            borderwidth=0, highlightthickness=0)
        genre_frame.pack(side=LEFT, padx=20)

        for i in range(len(books)):
            book_title = Label(title_frame, text=books[i]['book_title'])
            book_title.pack()

            book_author = Label(author_frame, text=books[i]['author_name'])
            book_author.pack()

            book_category = Label(genre_frame, text=books[i]['category_name'])
            book_category.pack()

    def __create_frame_input_new_category(self, frame):
        new_book_title = Label(frame, text="Title")
        new_book_title.pack()

        new_book_title_entry = Entry(frame)
        new_book_title_entry.pack()

        new_book_author = Label(frame, text="Author")
        new_book_author.pack()

        new_book_author_entry = Entry(frame)
        new_book_author_entry.pack()

        new_book_category = Label(frame, text="Category")
        new_book_category.pack()

        new_book_category_entry = Entry(frame)
        new_book_category_entry.pack()

        submit_button = Button(
            frame, text="Submit",
            command=partial(
                self.__submit_new_book,
                new_book_title_entry,
                new_book_author_entry,
                new_book_category_entry
            )
        )
        submit_button.pack()

    def __submit_new_book(self, title_entry, author_entry, category_entry):
        title = title_entry.get()
        author = author_entry.get()
        category = category_entry.get()

        if title != '' and author != '' and category != '':
            self.db.insert_book(title, author, category)
            self.refresh_book_content()
        else:
            print('fail submit: empty book attribute input')

    def __create_frame_delete_book(self, frame):
        del_book_title = Label(frame, text="Title")
        del_book_title.pack()

        del_book_title_entry = Entry(frame)
        del_book_title_entry.pack()

        submit_button = Button(
            frame, text="Submit",
            command=partial(
                self.__submit_delete_book,
                del_book_title_entry
            )
        )
        submit_button.pack()

    def __submit_delete_book(self, title_entry):
        title = title_entry.get()

        if title != '':
            self.db.delete_book(title)
            self.refresh_book_content()
        else:
            print('fail submit: empty book title')

    def refresh_book_content(self):
        self.books_container.destroy()
        self.load_book_content()
