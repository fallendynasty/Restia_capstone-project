from flask import Flask, render_template, request
# import database_functions
app = Flask(__name__)

@app.route('/') #Splash page (Welcome page)
def index():
    return render_template('index.html') #the login page will be drop down, not implemented

@app.route('/<int:student_id>/profile')  #profile page
def view_profile(student_id):
    breakpoint()
    # records = dict(request.form) #contain stuff needed
    # if 'admin' in request.args: #admin page
    #     return render_template('admin_profile.html')
    # return render_template('student_profile.html') 

# Index page (showing available actions)
app.run('0.0.0.0')