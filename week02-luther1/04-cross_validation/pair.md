#### Pair Problem

We'll use `statsmodels` to fit some (Ordinary Least Squares) linear models using random data.

First make a response `y` of 200 random numbers. Then generate 20 random features in an `X` to predict with. Fit a linear model using both the 'Famous Equation' and the python built-ins.  Check the `summary()` output of the results from the python built-ins. Do you have any features with `P>|t|` less than 0.05? (Repeat the process until you have at least one.)

Check out the model's `R-squared` and `Adj. R-squared`. Repeat the feature generation and model fitting process with 40, 60, 80, and 100 features. What happens with `R-squared` and `Adj. R-squared`?

If you have time, automate this experimental procedure and make a plot of `R-squared` and `Adj. R-squared` against number of features for one to one hundred features.
