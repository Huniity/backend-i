import sqlite3


with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    # Write the SQL command to create the Students table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Users (
        username TEXT,
        email TEXT,
        password TEXT
    );
    '''
    student_data = ('JaneDoe', 'janedoe@gmail.com', 'janedoe1234')
    # Execute the SQL command
    cursor.execute(create_table_query, student_data)
    # Execute the SQL command
    cursor.execute(create_table_query)

    # Commit the changes
    connection.commit()

    # Print a confirmation message
    print("Table 'Users' created successfully!")


# test a db, table user, emai, password, criar tabela em class

# https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data


# class DatabaseUser:

#     def __init__(self):
#         pass

#     def __enter__(self):
#         pass

#     def __exit__(self):
#         pass

#     def create_user(self):
#         pass


# if __name__ == "__main__":
#     with DatabaseUser("my_database.db") as db:
#         db.create_user()