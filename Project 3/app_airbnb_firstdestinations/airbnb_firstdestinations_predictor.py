import pickle


model = pickle.load( open( "airbnb_firstdestinations_model.p", "rb" ), encoding='latin1' )

def airbnb_firstdestination(gender, 
                            signup_method, 
                            signup_app, 
                            langues_en, 
                            diff_account_to_first_active, 
                            diff_account_to_first_booking, 
                            age, 
                            total_sessions_on_mac, 
                            total_sessions_on_windows, 
                            total_sessions_on_iphone, 
                            total_sessions_on_android):
    # categorical features:
    gender_inputs = {'male': [0,1,0], 'female': [1,0,0], 'other': [0,0,1], 'unknown': [0,0,0]}
    signup_method_inputs = {'facebook': [1,0], 'google': [0,1], 'direct': [0,0]}
    signup_app_inputs = {'moweb': [1,0,0], 'web': [0,1,0], 'ios':[0,0,1], 'android':[0,0,0]}
    language_en_inputs = {'true': [1], 'false': [0]}
    
    # numerical features
    total_sessions_on_mac = int(total_sessions_on_mac)
    total_sessions_on_windows = int(total_sessions_on_windows)
    total_sessions_on_iphone = int(total_sessions_on_iphone)
    total_sessions_on_android = int(total_sessions_on_android)
    diff_account_to_first_active = int(diff_account_to_first_active)
    diff_account_to_first_booking = int(diff_account_to_first_booking)
    
    total_sessions_input = total_sessions_on_mac + total_sessions_on_windows + total_sessions_on_iphone + total_sessions_on_android
    if age == '':
        no_age_entered = 1
        age = 37 # mean age
    else:
        no_age_entered = 0
        age = int(age)
        
    inputs = []
    inputs.extend(gender_inputs[gender])
    inputs.extend(signup_method_inputs[signup_method])
    inputs.extend(signup_app_inputs[signup_app])
    inputs.extend(language_en_inputs[langues_en])
    inputs.append(diff_account_to_first_active)
    inputs.append(diff_account_to_first_booking)
    inputs.append(age)
    inputs.append(total_sessions_input)
    inputs.append(total_sessions_on_mac)
    inputs.append(total_sessions_on_windows)
    inputs.append(total_sessions_on_iphone)
    inputs.append(total_sessions_on_android)
    inputs.append(no_age_entered)
    
    return model.predict_proba([inputs])