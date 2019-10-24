from tkinter import *
from database import DB
from functools import partial
from book_frame import BookFrame
from author_frame import AuthorFrame
from category_frame import CategoryFrame


# for gui
class MyWindow:
    def __init__(self, win):

        self.window = win
        self.db = DB('booksappdb.db')

        self.books_frame = Frame(win)
        self.books_frame.pack(fill="both", expand="yes")
        self.book_frame_object = BookFrame(
            self.books_frame, self.db)

        self.authors_frame = Frame(win)
        self.authors_frame.pack(fill="both", expand="yes")
        self.authors_frame_object = AuthorFrame(
            self.authors_frame, self.db)

        self.category_frame = Frame(win)
        self.category_frame.pack(fill="both", expand="yes")
        self.category_frame_object = CategoryFrame(
            self.category_frame, self.db)

        self.init_app()

    def init_app(self):
        self.book_frame_object.load_book_content()
        self.authors_frame_object.load_author_content()
        self.category_frame_object.load_category_content()


def main():
    window = Tk()
    mywin = MyWindow(window)
    window.title('Book App')
    window.geometry("900x600+10+10")
    window.mainloop()


if __name__ == "__main__":
    main()
