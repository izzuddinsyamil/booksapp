from tkinter import *
from database import DB
from functools import partial


class CategoryFrame():
    def __init__(self, win, db):
        self.main_frame = win
        self.db = db
        self.categories_container = None

    def load_category_content(self):
        categories_container_frame = LabelFrame(
            self.main_frame, text="Categories")
        categories_container_frame.pack(fill="both", expand="yes")
        self.categories_container = categories_container_frame

        left_frame = Frame(categories_container_frame)
        left_frame.pack(side=LEFT, padx=20)

        right_frame = Frame(categories_container_frame)
        right_frame.pack(side=LEFT, padx=20)

        category_input_frame = LabelFrame(
            right_frame, text="New Category", font="Helvetica 12 bold",
            borderwidth=0, highlightthickness=0)
        category_input_frame.pack(side=LEFT, padx=20)

        category_delete_frame = LabelFrame(
            right_frame, text="Delete Category", font="Helvetica 12 bold",
            borderwidth=0, highlightthickness=0)
        category_delete_frame.pack(side=LEFT, padx=20)

        self.__process_category_data(left_frame)

        self.__create_frame_input_new_category(category_input_frame)

        self.__create_frame_delete_category(category_delete_frame)

    def __process_category_data(self, frame):
        category_list_frame = LabelFrame(frame, text="Name", font="Helvetica 12 bold",
                                         borderwidth=0, highlightthickness=0)
        category_list_frame.pack()

        categories = self.db.get_categories()

        for i in range(len(categories)):
            category_name = Label(
                category_list_frame, text=categories[i]['name']
            )
            category_name.pack()

    def __create_frame_input_new_category(self, frame):
        new_category_name = Label(frame, text="Name")
        new_category_name.pack()

        new_category_entry = Entry(frame)
        new_category_entry.pack()

        submit_button = Button(
            frame, text="Submit",
            command=partial(
                self.__submit_new_category,
                new_category_entry
            ))
        submit_button.pack()

    def __submit_new_category(self, name_entry):
        name = name_entry.get()

        if name != '':
            self.db.insert_category(name)
            self.__refresh_content()
        else:
            print('fail submit: empty category name')

    def __create_frame_delete_category(self, frame):
        del_category_name = Label(frame, text="Name")
        del_category_name.pack()

        del_category_name_entry = Entry(frame)
        del_category_name_entry.pack()

        submit_button = Button(
            frame, text="Submit",
            command=partial(
                self.__submit_delete_category,
                del_category_name_entry
            )
        )
        submit_button.pack()

    def __submit_delete_category(self, name_entry):
        name = name_entry.get()

        if name != '':
            self.db.delete_category(name)
            self.__refresh_content()
        else:
            print('fail submit: empty category name')

    def __refresh_content(self):
        self.categories_container.destroy()
        self.load_category_content()
