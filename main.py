from flask import Flask, render_template, request
# import database_functions
app = Flask(__name__)

@app.route('/') #Splash page (Welcome page)
def index():
    return render_template('index.html') 

#form pages
@app.route('/view/<form>')
def view(form):
    if form == 'club':
        return render_template('view_club.html')
        
    if form == 'activity':
        return render_template('view_activity.html')

    if form == 'class':
        return render_template('view_class.html')

    else:
        return render_template('view_student.html')
        
@app.route('/add/<form>')
def add(form):
    if form == 'club':
        return render_template('add_club.html')

    else:
        return render_template('add_activity.html')

        
@app.route('/edit/<form>')
def edit(form):
    if form == 'student-club_membership':
        return render_template('edit_student-club_membership.html')
        
    else:
        return render_template('edit_student-activity_participation.html')

#profile page to be implemented
# @app.route('/<int:student_id>/profile')  
# def view_profile(student_id):
#     breakpoint()
#     records = dict(request.form) #contain stuff needed
#     if 'admin' in request.args: #admin page
#         return render_template('admin_profile.html')
#     return render_template('student_profile.html') 

# Index page (showing available actions)
app.run('0.0.0.0')


