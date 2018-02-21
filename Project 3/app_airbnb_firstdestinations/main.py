from flask import Flask, request, render_template
from airbnb_firstdestinations_predictor import airbnb_firstdestination

app = Flask(__name__)

@app.route('/')
def entry_page():

    default_values = {
    'gender' : 'male',
    'signup_method' : 'facebook',
    'signup_app' : 'moweb',
    'langues_en' : 'true',
    'diff_account_to_first_active' : '0',
    'diff_account_to_first_booking' : '10',
    'age' : '20',
    'total_sessions_on_mac' : '20',
    'total_sessions_on_windows' : '0',
    'total_sessions_on_iphone' : '30',
    'total_sessions_on_android' : '0' 
    }

    return render_template('index.html', form_values=default_values)

@app.route('/predict/', methods=['POST'])
def render_message():
    print(request.form)


    output = airbnb_firstdestination(
        request.form['gender'],
        request.form['signup_method'],
        request.form['signup_app'],
        request.form['langues_en'],
        request.form['diff_account_to_first_active'],
        request.form['diff_account_to_first_booking'],
        request.form['age'],
        request.form['total_sessions_on_mac'],
        request.form['total_sessions_on_windows'],
        request.form['total_sessions_on_iphone'],
        request.form['total_sessions_on_android']
        )
    
    

    if output[0][0] < 0.5:
        message = 'Domestic'
    else:
        message = 'International'

    percent_chance_international = 100 * output[0][0]
    percent_chance_domestic = 100 * output[0][1]

    return render_template(
        'index.html', 
        result=True, 
        message=message, 
        form_values=request.form,
        domestic_chance=percent_chance_domestic,
        international_chance=percent_chance_international

        )



if __name__ == '__main__':
    app.run(debug=True)