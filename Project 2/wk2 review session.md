# wk 2 
Tell us two things that you can tell from Pearson's Coefficient and what range is it in?

In OLS, why do we square the distance?

Why is cross validation better than train test split?
	provides a better prediction for out of sample
	
What does patsy do?
	it takes the columns of a dataframe a
	
What are independent events and how would you calculate each of their probabilities?
	'you can multiply them'
	
What is pickling and why is it important?
	saves as binary data and is fast to load
	
what's the probability of two coins landing on heads and a die landing on a 6?
	1/24
	
whats the relationship between matplotlib and seaborn and when would you use each?
	seaborn sits on top of matplotlib.  seaborn has a lot of prebuilt stuff and is pretty without much work. matplotlib has a 'knobs' so you can build something more customized from scratch
	
what's the difference between a list and a tuple?
	tuple: immutable, list: mutable
	tuples can be used as keys in dicts
	
	
	
# wk 3:


what's durbin watson and what are the danger zones?
	
what are the assuptions for linear regression?

what does the omnibus tell you?

what is the difference between homoskedacicity and hetero?

what's the difference between lasso and ridge? and when would you use elasticnetcv?

- ridge uses squares of the coefficients. allows values to be closed to zero but not zero. helpful when there's a lot of features with some collinearity.
- lasso uses absolute values of coefficients. lasso zeroes coefficients out. it punishes coefficients the same amount no matter how big they are. lasso is useful when you want to get rid of some features but you're not sure which
- ridge/lasso are not great for inference (analyzing the coefficients). but good with predicting out of sample.

what does kurtosis mean?

- amount of peakedness in a distribution. mean: first moment. variance: second moment. skewness: third moment. kurtosis/peakness: 4 moment

what is the F-statistic used for:

- null hypothesis: if all betas are equal to 0.

what do the coefficients' p-values indicate?

- null hypothesis: we happen to come across these coefficients by chance.

what are regex and why are they useful?


what would you do if one of your features' distributions is right skewed?

what's the difference between a probability of 95% and a confidence interval of 95%?

- confidence interval: we're 95% confident that a result falls within some interval
- probability of 95%: in 95% cases, this thing happens.