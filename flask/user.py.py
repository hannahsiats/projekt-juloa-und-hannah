import sqlite3

class User:
    def __init__(self, username, firstname, lastname):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    def to_db(self):
        connection = sqlite3.connect("database.db") # Muss vorher angelegt werden.
        cursor = connection.cursor()
        sql = f"INSERT INTO users(username, firstname, lastname) VALUES ('{self.username}', '{self.firstname}', '{self.lastname}')"
        cursor.execute(sql)
        connection.commit()
        connection.close()

    @classmethod
    def from_db(cls, username):
        connection = sqlite3.connect("database.db") # Muss vorher angelegt werden.
        cursor = connection.cursor()
        sql = f"SELECT username FROM users WHERE username = {username}"
        cursor.execute(sql)
        row = cursor.fetchone()
        connection.close()
        return User(row[0], row[1], row[2])

user = User.from_db("asbl")

@app.route("add_user", methods=["GET", "POST"])
def form():
        if request.method == "GET":
        return '''
                  <form method="POST">
                      <div><label>Username: <input type="text" name="username"></label></div>
                      <div><label>Firstname: <input type="text" name="first_name"></label></div>
                      <div><label>Lastname: <input type="text" name="last_name"></label></div>
                      <input type="submit" value="Submit">
                  </form>'''
    else:
        username = request.form.get("username")
        firstname = request.form.get("first_name")
        lastname = request.form.get("last_name")
        user = User(username, firstname, lastname)
        user.to_db()
        return f"Benutzer {username} wurde hinzugefügt"

     