from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__, template_folder='pages')
# pages folder
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# Static folder
app.config['STATIC_FOLDER'] = 'assets'

@app.route('/')
def index():
    return render_template('dashboard.html', title='Dashboard',pagename='Dashboard')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Process the form data here
        name = request.form.get('name')
        email = request.form.get('email')
        # You can add more fields as needed
        return render_template('form.html', name=name, email=email)
    return render_template('form.html')

# assets route
@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

if __name__ == '__main__':
    app.run(debug=True)