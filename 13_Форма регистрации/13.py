from flask import Flask, render_template, request
from data.db_session import global_init, create_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        global_init(f"db/mars_explorer.db")
        session = create_session()

        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            return "Пароли не совпадают", 400

        new_user = User(
            email=email,
            hashed_password=password,
            surname=request.form['surname'],
            name=request.form['name'],
            age=request.form['age'],
            position=request.form['position'],
            speciality=request.form['speciality'],
            address=request.form['address']
        )
        session.add(new_user)
        session.commit()
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)


