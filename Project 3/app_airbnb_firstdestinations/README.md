### Airbnb First Destinations Web App

**Step 1: Pickle your model**
* Create a model in Python and save it as a pickle file

**Step 2: You will be working with 4 files**
1. `main.py` - This is the main Python code that uses Flask and calls airbnb_firstdestinations_predictor.py to use the model
2. `airbnb_firstdestinations_predictor.py` - This is a separate Python script that reads in the pickled model and also preps the data for the model
3. `airbnb_firstdestinations_model.p` - The pickled model
4. `index.html` (in a templates folder) - This is the webpage that will be able to take inputs for the model and output a result on the webpage
