from flask import Flask, request, render_template
from seedling_identifier import identify
import datetime as dt

app = Flask(__name__)

@app.route('/')
def entry_page():
    return render_template('index.html')



@app.route('/identify/', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      now = dt.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
      filepath = '/Users/emilygeller/ds/metis/metisgh/Geller_Metis/Project 5/app/uploads/user_upload' + now + '.png'
      f = request.files['file']
      f.save(filepath)
      return identify(filepath)
        



# @app.route('/identify/', methods=['POST'])
# def render_message():
#     print(request.form)


#     # output = identify(
        
#     #     )
    
    

#     if output[0][0] < 0.5:
#         message = 'Domestic'
#     else:
#         message = 'International'

#     percent_chance_international = 100 * output[0][0]
#     percent_chance_domestic = 100 * output[0][1]

#     return render_template(
#         'index.html', 
#         result=True, 
#         message=message, 
#         form_values=request.form,
#         domestic_chance=percent_chance_domestic,
#         international_chance=percent_chance_international

#         )



if __name__ == '__main__':
    app.run(debug=False)