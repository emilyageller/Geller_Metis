from flask import Flask, request, render_template
from seedling_identifier import identify
import datetime as dt

app = Flask(__name__)
appfilepath = '/Users/emilygeller/ds/metis/metisgh/Geller_Metis/Project 5/app'

@app.route('/')
def entry_page():
    return render_template('index.html', result=False)


@app.route('/identify/', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      now = dt.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
      imagepath = '/static/uploads/user_upload' + now + '.png'
      filepath = appfilepath + imagepath
      f = request.files['file']
      f.save(filepath)
      message = identify(filepath)
      return render_template(
        'index.html',
        result= True,
        message=message,
        imagepath=imagepath)
      

if __name__ == '__main__':
    app.run(debug=False)