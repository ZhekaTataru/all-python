import sqlite3

bd=sqlite3.connect("user.bd")
sql=bd.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS user (login TEXT,password TEXT,kash INT) """)
bd.commit()
user_login=input("login: ")
user_password=input("password: ")
sql.execute("SELECT login FROM user")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO user VALUES (?,?,?)",(user_login,user_password,0))
    bd.commit()
else:
    print("Такая запись уже существует!")