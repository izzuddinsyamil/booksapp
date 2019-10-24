import sqlite3


class DB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = self.__create_connection(db_name)

        sql_authors_creation = '''
            CREATE TABLE 'authors' ('id' INTEGER NOT NULL, 'name' TEXT NOT NULL, 'gender' TEXT NOT NULL, PRIMARY KEY('id'))
        '''

        sql_books_creation = '''
            CREATE TABLE 'books' ('id' INTEGER NOT NULL, 'title' TEXT NOT NULL, 'author_id' INTEGER NOT NULL, 'category_id' INTEGER NOT NULL, PRIMARY KEY('id'))
        '''

        sql_categories_creation = '''
            CREATE TABLE 'categories' ('id' INTEGER NOT NULL, 'name' TEXT NOT NULL, PRIMARY KEY('id'))
        '''
        if self.connection:
            self.__create_table_authors(sql_authors_creation)
            self.__create_table_books(sql_books_creation)
            self.__create_table_categories(sql_categories_creation)

        else:
            print('connection not available')

    def __create_connection(self, db_file):
        try:
            connection = sqlite3.connect(db_file)
            print('database %s successfully created' % db_file)
            return connection
        except sqlite3.Error as error:
            print(error)
            return None

    def __create_table_authors(self, sql):
        if self.connection:
            cursor = self.connection.cursor()
            try:
                cursor.execute(sql)
                print('table authors created')
            except sqlite3.Error as error:
                print(error)
        else:
            print('No connection')

    def __create_table_books(self, sql):
        if self.connection:
            cursor = self.connection.cursor()
            try:
                cursor.execute(sql)
                print('table books created')
            except sqlite3.Error as error:
                print(error)
        else:
            print('No connection')

    def __create_table_categories(self, sql):
        if self.connection:
            cursor = self.connection.cursor()
            try:
                cursor.execute(sql)
                print('table categories created')
            except sqlite3.Error as error:
                print(error)
        else:
            print('No connection')

    def get_books(self):
        c = self.__create_connection('booksappdb.db')

        if c:
            sql_get_books = '''
                select books.title, authors.name, categories.name
                from books, authors, categories
                where books.author_id = authors.id
                and books.category_id = categories.id;
            '''

            cursor = self.connection.cursor()
            cursor.execute(sql_get_books)

            books = []

            for row in cursor:
                book = {}
                book['book_title'] = row[0]
                book['author_name'] = row[1]
                book['category_name'] = row[2]
                books.append(book)

            c.close()
            return books
        else:
            print('No connection')

    def insert_book(self, title, author_name, category_name):
        author_id = self.__get_author_id(author_name)
        category_id = self.__get_category_id(category_name)

        c = self.__create_connection('booksappdb.db')
        if c and author_id and category_id:

            sql_insert_book = '''
                INSERT INTO books (title, author_id, category_id)
                VALUES ("{}", {}, {});
            '''.format(title, author_id, category_id)

            cursor = c.cursor()

            try:
                cursor.execute(sql_insert_book)
                c.commit()
                c.close()
                print('success insert ', title)
            except sqlite3.Error as error:
                print(error)

        else:
            print('No connection')

    def __get_author_id(self, name):
        c = self.__create_connection('booksappdb.db')
        if c:
            sql_get_author_id = 'SELECT id FROM authors WHERE name="{}";'.format(
                name)
            cursor = c.cursor()

            try:
                cursor.execute(sql_get_author_id)
                author_id = cursor.fetchone()[0]
                c.close()

                return author_id
            except Exception as error:
                c.close()
                print(error)
        else:
            print('No connection')

    def __get_category_id(self, name):
        c = self.__create_connection('booksappdb.db')
        if c:
            sql_get_category_id = 'SELECT id FROM categories WHERE name="{}";'.format(
                name)
            cursor = c.cursor()

            try:
                cursor.execute(sql_get_category_id)
                category_id = cursor.fetchone()[0]
                c.close()

                return category_id
            except Exception as error:
                c.close()
                print(error)
        else:
            print('No connection')

    def delete_book(self, title):
        c = self.__create_connection('booksappdb.db')
        if c:
            sql_delete_book = 'DELETE FROM books WHERE title="{}"'.format(
                title)
            cursor = c.cursor()

            try:
                cursor.execute(sql_delete_book)
                c.commit()
                c.close()
                print('success delete: ', title)
            except sqlite3.Error as error:
                print(error)

        else:
            print('No connection')

    def get_authors(self):
        c = self.__create_connection('booksappdb.db')
        if c:
            sql_get_authors = 'SELECT * FROM authors;'

            cursor = c.cursor()
            cursor.execute(sql_get_authors)

            authors = []

            for row in cursor:
                author = {}
                author['name'] = row[1]
                author['gender'] = row[2]
                authors.append(author)

            c.close()
            return authors
        else:
            print('No connection')

    def insert_author(self, name, gender):
        c = self.__create_connection('booksappdb.db')
        if c:
            sql_insert_author = 'INSERT INTO authors (name, gender) VALUES ("{}", "{}");'.format(
                name, gender)
            cursor = c.cursor()

            try:
                cursor.execute(sql_insert_author)
                c.commit()
                c.close()
                print('success insert ', name)
            except sqlite3.Error as error:
                print(error)

        else:
            print('No connection')

    def delete_author(self, name):
        c = self.__create_connection('booksappdb.db')
        if c:
            sql_delete_author = 'DELETE FROM authors WHERE name="{}"'.format(
                name)
            cursor = c.cursor()

            try:
                cursor.execute(sql_delete_author)
                c.commit()
                c.close()
                print('success delete: ', name)
            except sqlite3.Error as error:
                print(error)

        else:
            print('No connection')

    def get_categories(self):
        c = self.__create_connection('booksappdb.db')
        if c:
            sql_get_categories = 'SELECT * FROM categories;'

            cursor = c.cursor()
            cursor.execute(sql_get_categories)

            categories = []

            for row in cursor:
                category = {}
                category['name'] = row[1]
                categories.append(category)

            c.close()
            return categories
        else:
            print('No connection')

    def insert_category(self, name):
        c = self.__create_connection('booksappdb.db')
        if c:
            sql_insert_category = 'INSERT INTO categories (name) VALUES ("{}");'.format(
                name)
            cursor = c.cursor()

            try:
                cursor.execute(sql_insert_category)
                c.commit()
                c.close()
                print('success insert ', name)
            except sqlite3.Error as error:
                print(error)

        else:
            print('No connection')

    def delete_category(self, name):
        c = self.__create_connection('booksappdb.db')
        if c:
            sql_delete_category = 'DELETE FROM categories WHERE name="{}"'.format(
                name)
            cursor = c.cursor()

            try:
                cursor.execute(sql_delete_category)
                c.commit()
                c.close()
                print('success delete: ', name)
            except sqlite3.Error as error:
                print(error)

        else:
            print('No connection')
