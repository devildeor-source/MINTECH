import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure upload settings
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Simple database (in-memory for now) to store doctor profiles
doctors_db = []

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    # Pass the database of doctors to the HTML template
    return render_template('index.html', doctors=doctors_db)

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    # Handle both the file upload and the doctor details
    name = request.form.get('doctorName')
    degree = request.form.get('doctorDegree')
    file = request.files['doctorPhoto']

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # 1. Save the file from the gallery to the /uploads folder
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # 2. Add the path to the database
        doctor_path = url_for('static', filename='uploads/' + filename)
        doctors_db.append({'name': name, 'degree': degree, 'photo': doctor_path})
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Ensure the upload folder exists on first run
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    # Important for mobile: run on all interfaces (0.0.0.0)
    app.run(host='0.0.0.0', port=5000, debug=True)
  
