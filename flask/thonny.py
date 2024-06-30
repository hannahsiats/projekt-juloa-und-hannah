from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'  


class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


users = [
    User(1, 'user1', 'password1'),
    User(2, 'user2', 'password2'),
    
]

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user.username == username and user.check_password(password):
                login_user(user)
                return redirect(url_for('protected'))
        return 'Invalid username or password', 401
    return render_template('login.html')

@app.route('/protected')
@login_required
def protected():
    return render_template('protected.html', username=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    
    
