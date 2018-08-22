from flask import Flask, render_template, request, flash, redirect, session
from calculateTotalReturn import calculate_total_return

ALLOWED_EXTENSIONS = set(['xlsx'])

app = Flask(__name__)
app.secret_key = "super secret key"

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def home(name=None):
    totalReturn = 0

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part, please attach a file')
            return redirect(request.url)
        file = request.files['file']

        if file and not allowed_file(file.filename):
            flash('Invalid file extension, please attach a xlsx file')

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file, please attach a file ')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            totalReturn = calculate_total_return(file)
            return render_template('index.html', name=name, totalReturn=totalReturn)

            # filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file',
            #                         filename=filename))
    return render_template('index.html', name=name, totalReturn=totalReturn)


