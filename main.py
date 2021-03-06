from flask import Flask, render_template, request
import db
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
    view_records = db.coll[form].get_all()
    if "view" in request.args:
        view_parameters = dict(request.form)
        view_records = db.coll[form].find(Name=view_parameters['Name'])
    
    if form == 'club':
        return render_template('view_club.html', view_records=view_records)
        
    if form == 'activity':
        return render_template('view_activity.html', view_records=view_records)

    if form == 'class':
        return render_template('view_class.html', view_records=view_records)

    else: #view students
        return render_template('view_student.html', view_records=view_records)
        
@app.route('/add/<form>',  methods=['GET', 'POST'])
def add(form):
    '''
    goes to form for adding, post to send data in the form
    '''
    if "add" in request.args:
        add_parameters = dict(request.form) 
        print(request.form.values, add_parameters)
        db.coll[form].insert(add_parameters)
        return render_template('add_success.html', 
                               record=add_parameters,
                               form_type=form)
        
        
    if form == 'club':
        return render_template('add_club.html')

    else: #add activity
        return render_template('add_activity.html')
         
@app.route('/edit/<form>',  methods=['GET', 'POST'])
def edit(form):
    '''
    goes to form for editing, post request so that changes can be sent to database
    '''
    
    if form == 'membership':
        clubs = db.coll['club'].get_all()
        club_searched = dict(request.form)['Name'].upper()
        club_id = None
        for x in clubs:
            if x[1] == club_searched:
                club_id = (x[0],)
        if club_id is None:
            view_records = 'Club does not exist'
        else:    
            view_records = db.coll['club'].find_students_in_club(club_id)
        return render_template('edit_student-club_membership.html', view_records=view_records)
        
    else:
        return render_template(
            'edit_student-activity_participation.html'
        )

@app.route('/construction',  methods=['GET', 'POST'])
def construction():
    return render_template('construction.html')
    
app.run('0.0.0.0')