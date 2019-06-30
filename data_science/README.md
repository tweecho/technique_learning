# Data Science Interview Questions and Answers (数据科学面试问题及答案)

## Contents
### Q1 How would you create a taxonomy(分类) to identify key customer trends in unstructured data? 
```
- check with the business owner and understand their objectives before categorizing the data.
- follow an iterative approach by pulling new data samples and improving the model accordingly by validating it for accuracy  by solidating(征求) feedback from the business stakeholders. 
- This would help you ensure the model is producing actionable results and improving over the time.
```
### Q2 Python or R -- Which one would you prefer for text analytics?
```
- Python is a general purpose programming language 
- R contains more statistical libraries
- Python has Pandas library which provides easy to use data structure and high performance data analysis tools
- R has some existed packages for analysing clean texts
```
### Q3 Which technique is used to predict categorical responses?
```
-Classification technique is used widely in classifying data
```
### Q4 What is logistic regression? Or state an example when you have used logistic regression recently?
```
- Logistic regression, often referred as logit model, is a technique to predict the **binary** outcome from a linear combination of predictor variables.
- e.g. Applying for the mortgage, giving the credit score range from 300-800, if you have a credit score 600, the logistic regression model should be able to predict whether you'll be approved for the mortgage or not.
- The probability given by LR has to be between 0 and 1, but it's not true for other regression models.
  - (simple linear regression is one quantitative variable predicting another quantitative variable and multiple regression is simple linear regression with more independent variables, not using for this type of questions)
```
### Q5 What are Recommender Systems?
```
- One of the information filtering systems which focus on predicting preferences of a user or ratings that a user would give to a product. Recommender systems are widely used for online-shopping platforms, news, movies, music, etc. 
```
### Q6 Why data cleaning plays a vital role in analysis?
```
- The data cleaning process is a cumbersome and time-costing process and it might take up to 80% of the time just cleaning data to make it a critical part of analysis task
- The analysis results would be affected by the quality of the data, thus data cleaning is very important, well begun is half done
```
### Q7 Differentiate between univariate, bivariate and multivariate analysis
```
- Descriptive statistical analysis techniques(描述性统计分析技术) which varies from each other based on the number of variables involved at a given point of time
- Univariate analysis, only one variable is involved in the analysis
- Bivariate analysis, attempting to understand the difference between 2 variables
- Multivariate analysis, dealing with more than 2 variables to understand the effect of variables
```
### Q8 What do you understand by the term Normal Distribution?
```
- Data is ususally distributed in different ways with a bias to the left or to the right, or it can all be jumbled up(混乱)
- Normal distribution means that the data is distributed around a central curve value without any bias to the left or to the right and it is distributed in the form of a bell shaped curve
- The random variables are distributed in the form of a symmetrical bell shaped curve
```
### Q9 What is linear regression?
```
- A statistical technique where the score of Y is predicted from the score of a second variable X. X is referred to as the predictor variable and Y as the criterion variable
```
### Q10 What is Interpolation() and Extrapolation?
```
- Interpolation, estimating a value from 2 known values from a list of values
- Extrapolation, approximating a value by extending a known set of values or facts
```
### Q11 What is power analysis(功效分析)?
```
- An experimental design technique for determining the effect of a given sample size with a given degree of confidence
```
### Q12 What is K-means? How can you select K for K-means?
``` 
- K-means is a clustering algorithm (K-nearest neighbor is a calssification algorithm), handle with unsupervised problems. K-means clustering aims to partition n observations into K clusters in which each observation belongs to the cluster with the nearest mean, serving as a prototype of the cluster.
- The number of clusters can be chosen visually or compute the SSE (sum of squared error) for some values of K to find a good K.
```
### Q13 What is Collaborative filtering?
```
- A method of making automatic predictions about the interests of a user by collecting preferences or taste information from many users (collaborating).
- It is used in most of the recommender systems.
```
### Q14 What is the difference between Cluster and Systematic Sampling?
```
- 
```


## Reference
- Interview questions: https://github.com/zhiqiangzhongddu/Data-Science-Interview-Questions-and-Answers-General-
- Logistic regression: https://towardsdatascience.com/introduction-to-logistic-regression-66248243c148
- 2018 100 DS Interview questions: https://www.dezyre.com/article/100-data-science-interview-questions-and-answers-general-for-2018/184
- 2017 41 Essential machine learning interview questions: https://www.springboard.com/blog/machine-learning-interview-questions/?from=message&isappinstalled=0
