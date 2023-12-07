import sqlite3 as sq3
def run():
    try:
        sqliteConn = sq3.connect('My_Skillbridge.db') 
        cursor = sqliteConn.cursor()

        query = '''
        CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIVATE KEY,
        matric_no VARCHAR(50) not null,
        name VARCHAR(50) not null,
        email VARCHAR(50) not null,
        password VARCHAR(50) not null,
        dept VARCHAR(20) not null
        );
        '''
        cursor.execute(query)

        query = '''
        CREATE TABLE IF NOT EXISTS skills(
        id INTEGER PRIVATE KEY,
        skill_name VARCHAR(50) not null,
        description VARCHAR(60) not null,
        level_of_expertise VARCHAR(20) not null
        );
        '''
        cursor.execute(query)

        query = '''
        CREATE TABLE IF NOT EXISTS listing(
        id INTEGER PRIVATE KEY,
        available_slots VARCHAR(50) not null,
        price_per_slots VARCHAR(20) not null,
        other_details VARCHAR(20) not null
        );
        '''
        cursor.execute(query)

        query = '''
        CREATE TABLE IF NOT EXISTS request(
        id INTEGER PRIVATE KEY,
        request_date VARCHAR(20) not null,
        status VARCHAR(20) not null,
        other_details VARCHAR(40) not null
        );
        '''
        cursor.execute(query)

        query = '''
        CREATE TABLE IF NOT EXISTS rating(
        id INTEGER PRIVATE KEY,
        rating_value VARCHAR(50) not null,
        review_comment VARCHAR(50) not null,
        rating_date VARCHAR(20) not null
        );
        '''
        cursor.execute(query)

        sqliteConn.commit()
        sqliteConn.close()
    except Exception as e:
        print(f"Error:{e}")
    finally:
        if sqliteConn:
            sqliteConn.close()
            print('SQLite connection closed')

if __name__ == '__main__':
    run()        