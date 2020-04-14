# @app.route('/profile')
# def profile():
#     return render_template('profile.html')

# @app.route('/user')
# def user():
#     if 'username' in session:
#         return 'You are logged in as ' + session['username']

#     return render_template('user.html')


# @app.route('/login', methods=['POST'])
# def login():
#     users = mongo.db.users
#     login_user = users.find_one({'name' : request.form['username']})

#     if login_user:
#         if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
#             session['username'] = request.form['username']
#             return redirect(url_for('user'))

#     return 'Invalid username/password combination'

# @app.route('/register', methods=['POST', 'GET'])
# def register():
#     if request.method == 'POST':
#         users = mongo.db.users
#         existing_user = users.find_one({'name' : request.form['username']})

#         if existing_user is None:
#             hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
#             users.insert({'name' : request.form['username'], 'password' : hashpass})
#             session['username'] = request.form['username']
#             return redirect(url_for('user'))
        
#         return 'That username already exists!'

#     return render_template('register.html')


# login python authentication and index and register.html copied from https://www.youtube.com/watch?v=vVx1737auSE