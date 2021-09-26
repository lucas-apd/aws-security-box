from flask import Flask, render_template, request
from tempshare import upload_file
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='template')


@app.route('/', methods=['GET', 'POST'])

def index(res = None):

    if request.method == 'POST':
       
        uploaded_file = request.files['fname']
        if uploaded_file.filename:
            uploaded_file.save(uploaded_file.filename)
            res = upload_file(uploaded_file.filename)
        return render_template('index.html', result=res)
    return render_template('index.html')
  
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080,debug=True)