from flask import Flask, render_template , url_for, request ,  redirect
from dbc import dbconnect

 
username = None

app = Flask(__name__)

posts = [
            {
                'student':'David Ger',
                'teacher':'Kingsley', 
                'training':'Python Training' 
            },
            {
                'student':'David Ger',
                'teacher':'Mad Doctor',
                'training':'Priscilla'
            }

        ]


# for index route to
@app.route('/')
def index():
    return redirect('/login')
#For the purpose of login methods
@app.route ('/login', methods = ['POST', 'GET'])
def login():
    #We use post http request to check
    if request.method == 'POST':
        data = request.values
        #Ensure the user name and data is not empty
        if data['user'] == ''or data['pwd'] == '' :
            return redirect('/login')
        #If username and data is there the we check in the db
        else:
            #We pick from the dbc script 
            flaskdb = dbconnect('flaskdb','david','root')
            flaskdbcur = flaskdb.cursor()
            flaskdbcur.execute('SELECT * FROM users WHERE name = %s',(data['user'],))
            if flaskdbcur.rowcount > 0:
                users = flaskdbcur.fetchone()
                if users[2] == data['pwd']:
                    global username
                    username = users[1]
                    return redirect ('/home/' + users[1])
                else:
                    return redirect('/login')
            else:
                return redirect ('/login')
    else:
        return render_template('login.html')

@app.route ('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        data = request.values
        if data['user'] == '' or data['pwd'] == '' or data['pwd2'] == '':
            return redirect('/register')
        elif data['pwd'] != data['pwd2']:
            
            return redirect ('/register' )
        else :
            flaskdb = dbconnect('flaskdb','david','root')
            flaskdbcur = flaskdb.cursor()
            flaskdbcur.execute('INSERT INTO users(name, password) VALUES(%s, %s)',(data['user'],data['pwd']))
            flaskdb.commit()
            return redirect ('/login')

    else:
        return render_template('register.html')

@app.route('/home/<user>')
def home(user):
    
    return render_template('index.html',posts = posts , title = 'Profile', user = user)

#Update Password
@app.route ('/updatepass', methods = ['POST', 'GET'])
def updatepass():

        if request.method == 'POST':
            data = request.values
            #Ensure the user name and data is not empty
            if data['pwd'] == '' or data['npwd'] == '':
                return redirect('/updatepass')
            #If username and data is there the we check in the db
            else:
                #We pick from the dbc script
                flaskdb = dbconnect('flaskdb','david','root')
                flaskdbcur = flaskdb.cursor()
                flaskdbcur.execute('UPDATE users SET password = %s   WHERE name = %s', (data['npwd'], username))
                flaskdb.commit()
                return redirect('/product')

            
        else:
            return render_template('updatepass.html')


@app.route ('/deletepass', methods = ['POST', 'GET'])
def deletepass():

        if request.method == 'POST':
            data = request.values
            flaskdb = dbconnect('flaskdb','david','root')
            flaskdbcur = flaskdb.cursor()
            flaskdbcur.execute('DELETE FROM users WHERE name =%s ', (username,))
            flaskdb.commit()
            return redirect('/login')
            
            #If username and data is there the we check in the db
        else:
            #We pick from the dbc script
            return render_template('updatepass.html')

            
        


@app.route ('/project')
def project():
    return render_template('project.html')

@app.route ('/product')
def product():
    return render_template('product.html')

@app.route ('/contactus')
def contact_us():
    return render_template('contactus.html')

@app.route ('/about')
def about():
    return render_template('about.html')

