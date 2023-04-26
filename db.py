import sqlite3 as sqlt

db_name = 'user_database.db'


def start_db():
    base = sqlt.connect(db_name)
    base.execute('CREATE TABLE IF NOT EXISTS "User" ("id"	INTEGER NOT NULL UNIQUE,'
                 '"user_id"     INTEGER,'
                 '"channel_id"  INTEGER,'
                 'PRIMARY KEY("id" AUTOINCREMENT))')
    base.execute('CREATE TABLE IF NOT EXISTS "Message" ("id"	INTEGER NOT NULL UNIQUE,'
                 '"title"       BLOB,'
                 '"chat_id"     INTEGER,'
                 '"message_id"  INTEGER,'
                 'PRIMARY KEY("id" AUTOINCREMENT))')
    base.execute('CREATE TABLE IF NOT EXISTS "User_ivent" ("id"	INTEGER NOT NULL UNIQUE,'
                 '"channel_id"      INTEGER,'
                 '"user_id"         INTEGER,'
                 'PRIMARY KEY("id" AUTOINCREMENT))')
    base.execute('CREATE TABLE IF NOT EXISTS "All_post" ('
                 '"name"        BLOB,'
                 '"chat_id"     INTEGER,'
                 '"message_id"  INTEGER,'
                 'PRIMARY KEY("chat_id", "message_id"))')
    base.commit()


def first_add_post():
    with sqlt.connect(db_name) as conn:
        cur = conn.cursor()
        data = cur.execute('SELECT * FROM All_post').fetchall()
        if not data:
            for index in range(1, 8):
                cur.execute('INSERT INTO All_post VALUES (?, null, null)', (f'{index} шаблон', ))
            return True
        else:
            return False


def add_post(name, chat_id, message_id):
    print('XXXXX')
    with sqlt.connect(db_name) as conn:
        cur = conn.cursor()
        cur.execute('UPDATE All_post SET chat_id= ?, message_id = ? WHERE name = ?', (chat_id, message_id, name))


def update_posts_by_name(old_name, new_name):
    try:
        with sqlt.connect(db_name) as conn:
            cur = conn.cursor()
            cur.execute('UPDATE All_post SET name = ? WHERE name = ?', (new_name, old_name))
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def get_all_post():
    with sqlt.connect(db_name) as conn:
        cur = conn.cursor()
        text = cur.execute('SELECT * from All_post').fetchall()
    return text


def get_all_pattern():
    with sqlt.connect(db_name) as conn:
        cur = conn.cursor()
        text = cur.execute('SELECT * from Message').fetchall()
    return text


def delete_pattern(name):
    with sqlt.connect(db_name) as conn:
        cur = conn.cursor()
        text = cur.execute('SELECT title from Message WHERE title = ?', (name,)).fetchall()
        if text:
            cur.execute('DELETE FROM Message WHERE title = ?', (name,))
            return True
        else:
            return False


def add_user(user_id, channel_id):
    with sqlt.connect(db_name) as conn:
        cur = conn.cursor()
        data = cur.execute('SELECT * FROM User WHERE user_id = ? AND channel_id = ?', (user_id, channel_id)).fetchone()
        if data is None:
            cur.execute('INSERT INTO User VALUES (null, ?, ?)', (user_id, channel_id))
            return True
        else:
            return False


def all_user():
    with sqlt.connect(db_name) as conn:
        cur = conn.cursor()
        users = cur.execute('SELECT * from User').fetchall()
    return users


def add_message(title, chat_id, message_id):
    with sqlt.connect(db_name) as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO Message VALUES (null, ?, ?, ?)', (title, chat_id, message_id))


def get_message():
    with sqlt.connect(db_name) as conn:
        cur = conn.cursor()
        data = cur.execute('SELECT * FROM Message').fetchall()
        if data is None:
            return False
        else:
            return data


def template_selection(ID):
    with sqlt.connect(db_name) as conn:
        cur = conn.cursor()
        data = cur.execute('SELECT * FROM Message WHERE id = ?', (ID,)).fetchall()
        if data is None:
            return False
        else:
            return data


def get_users_in_channel_id(user_id):
    with sqlt.connect(db_name) as conn:
        cur = conn.cursor()
        data = cur.execute('SELECT channel_id FROM User WHERE user_id = ?', (user_id,)).fetchone()
        return data
