from flask import Flask, render_template, request
import db as DB
app = Flask(__name__)

@app.route('/') #Splash page (Welcome page)
def index():
    return render_template('index.html') 

#form pages
@app.route('/view/<form>', methods=['GET', 'POST'])
def view(form):
    '''
    views the form of specified type
    '''
    view_records = []
    if "view" in request.args:
        view_parameters = dict(request.form)
        view_records.append(DB.get_data(view_parameters, form))

    if form == 'club':
        return render_template('view_club.html', view_records=view_records)
        
    if form == 'activity':
        return render_template('view_activity.html', view_records=view_records)

    if form == 'class':
        return render_template('view_class.html', view_records=view_records)

    else:
        return render_template('view_student.html', view_records=view_records)
        
@app.route('/add/<form>',  methods=['GET', 'POST'])
def add(form):
    '''
    goes to form for adding, post to send data in the form
    '''
    if "add" in request.args:
        add_parameters = dict(request.form)
        DB.add(add_parameters, form)
        return render_template('add_success.html', 
                               record=add_parameters,
                               form_type=form)
        
    if form == 'club':
        return render_template('add_club.html')

    else:
        return render_template('add_activity.html')

        
@app.route('/edit/<form>',  methods=['GET', 'POST'])
def edit(form):
    '''
    goes to form for editing, post request so that changes can be sent to database
    '''
    # edit to be implemented
    # if "edit" in request.args:
    #     edit_parameters = dict(request.form)
    #     DB.edit(edit_parameters, form)
    #     return render_template('edit_success.html',
    #                           record=edit_parameters,
    #                           form_type=form)

    if form == 'student-club_membership':
        return render_template('edit_student-club_membership.html')
        
    else:
        return render_template('edit_student-activity_participation.html')
        
app.run('0.0.0.0')
#profile page to be implemented
# @app.route('/<int:student_id>/profile')  
# def view_profile(student_id):
#     breakpoint()
#     records = dict(request.form) #contain stuff needed
#     if 'admin' in request.args: #admin page
#         return render_template('admin_profile.html')
#     return render_template('student_profile.html') 



