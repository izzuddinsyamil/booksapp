from tkinter import *
from database import DB
from functools import partial


class AuthorFrame():
    def __init__(self, win, db):
        self.main_frame = win
        self.db = db
        self.authors_container = None

    def load_author_content(self):
        authors_container_frame = LabelFrame(
            self.main_frame, text="Authors")
        authors_container_frame.pack(fill="both", expand="yes")
        self.authors_container = authors_container_frame

        left_frame = Frame(authors_container_frame)
        left_frame.pack(side=LEFT, padx=20)

        right_frame = Frame(authors_container_frame)
        right_frame.pack(side=LEFT, padx=20)

        new_author_frame = LabelFrame(
            right_frame, text="New Author", font="Helvetica 12 bold",
            borderwidth=0, highlightthickness=0)
        new_author_frame.pack(side=LEFT, padx=20)

        delete_author_frame = LabelFrame(
            right_frame, text="Delete Author", font="Helvetica 12 bold",
            borderwidth=0, highlightthickness=0
        )
        delete_author_frame.pack(side=LEFT, padx=20)

        self.__process_authors_data(left_frame)

        self.__create_frame_input_new_author(new_author_frame)

        self.__create_frame_delete_author(delete_author_frame)

    def __process_authors_data(self, frame):
        author_name_frame = LabelFrame(
            frame, text="Name", font="Helvetica 12 bold",
            borderwidth=0, highlightthickness=0)
        author_name_frame.pack(side=LEFT, padx=20)

        author_gender_frame = LabelFrame(
            frame, text="Gender", font="Helvetica 12 bold",
            borderwidth=0, highlightthickness=0)
        author_gender_frame.pack(side=LEFT, padx=20)

        authors = self.db.get_authors()

        for i in range(len(authors)):
            author_name = Label(author_name_frame, text=authors[i]['name'])
            author_name.pack()

            author_gender = Label(author_gender_frame,
                                  text=authors[i]['gender'])
            author_gender.pack()

    def __create_frame_input_new_author(self, frame):
        new_author_name = Label(frame, text="Name")
        new_author_name.pack()

        new_author_name_entry = Entry(frame)
        new_author_name_entry.pack()

        new_author_gender = Label(frame, text="Gender")
        new_author_gender.pack()

        new_author_gender_entry = Entry(frame)
        new_author_gender_entry.pack()

        submit_button = Button(
            frame, text="Submit",
            command=partial(
                self.__submit_new_author,
                new_author_name_entry, new_author_gender_entry))
        submit_button.pack()

    def __submit_new_author(self, name_entry, gender_entry):
        name = name_entry.get()
        gender = gender_entry.get()

        if name != '' and gender != '':
            self.db.insert_author(name, gender)
            self.__refresh_content()
        else:
            print('fail submit: empty author attribute input')

    def __create_frame_delete_author(self, frame):
        del_author_name = Label(frame, text="Name")
        del_author_name.pack()

        del_author_name_entry = Entry(frame)
        del_author_name_entry.pack()

        submit_button = Button(
            frame, text="Submit",
            command=partial(self.__submit_delete_author, del_author_name_entry))
        submit_button.pack()

    def __submit_delete_author(self, name_entry):
        name = name_entry.get()

        if name != '':
            self.db.delete_author(name)
            self.__refresh_content()
        else:
            print('fail submit: empty author name')

    def __refresh_content(self):
        self.authors_container.destroy()
        self.load_author_content()
