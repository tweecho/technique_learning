# Data Science Interview Questions and Answers (数据科学面试问题及答案)

## Contents
#### Q1 How would you create a taxonomy(分类) to identify key customer trends in unstructured data? 
```
- check with the business owner and understand their objectives before categorizing the data.
- follow an iterative approach by pulling new data samples and improving the model accordingly by validating it for accuracy  by solidating(征求) feedback from the business stakeholders. 
- This would help you ensure the model is producing actionable results and improving over the time.
```
#### Q2 Python or R -- Which one would you prefer for text analytics?
```
- Python is a general purpose programming language 
- R contains more statistical libraries
- Python has Pandas library which provides easy to use data structure and high performance data analysis tools
- R has some existed packages for analysing clean texts
```
#### Q3 Which technique is used to predict categorical responses?
```
-Classification technique is used widely in classifying data
```
#### Q4 What is logistic regression? Or state an example when you have used logistic regression recently?
```
- Logistic regression, often referred as logit model, is a technique to predict the **binary** outcome from a linear combination of predictor variables.
- e.g. Applying for the mortgage, giving the credit score range from 300-800, if you have a credit score 600, the logistic regression model should be able to predict whether you'll be approved for the mortgage or not.
- The probability given by LR has to be between 0 and 1, but it's not true for other regression models.
  - (simple linear regression is one quantitative variable predicting another quantitative variable and multiple regression is simple linear regression with more independent variables, not using for this type of questions)
```
#### Q5 What are Recommender Systems?
```
- One of the information filtering systems which focus on predicting preferences of a user or ratings that a user would give to a product. Recommender systems are widely used for online-shopping platforms, news, movies, music, etc. 
```
#### Q6 Why data cleaning plays a vital role in analysis?
```
- The data cleaning process is a cumbersome and time-costing process and it might take up to 80% of the time just cleaning data to make it a critical part of analysis task
- The analysis results would be affected by the quality of the data, thus data cleaning is very important, well begun is half done
```
#### Q7 Differentiate between univariate, bivariate and multivariate analysis
```
- Descriptive statistical analysis techniques(描述性统计分析技术) which varies from each other based on the number of variables involved at a given point of time
- Univariate analysis, only one variable is involved in the analysis
- Bivariate analysis, attempting to understand the difference between 2 variables
- Multivariate analysis, dealing with more than 2 variables to understand the effect of variables
```
#### Q8 What do you understand by the term Normal Distribution?
```
- Data is ususally distributed in different ways with a bias to the left or to the right, or it can all be jumbled up(混乱)
- Normal distribution means that the data is distributed around a central curve value without any bias to the left or to the right and it is distributed in the form of a bell shaped curve
- The random variables are distributed in the form of a symmetrical bell shaped curve
```
#### Q9 What is linear regression?
```
- A statistical technique where the score of Y is predicted from the score of a second variable X. X is referred to as the predictor variable and Y as the criterion variable
```
#### Q10 What is Interpolation() and Extrapolation?
```
- Interpolation, estimating a value from 2 known values from a list of values
- Extrapolation, approximating a value by extending a known set of values or facts
```
#### Q11 What is power analysis(功效分析)?
```
- An experimental design technique for determining the effect of a given sample size with a given degree of confidence
```
#### Q12 What is K-means? How can you select K for K-means?
``` 
- K-means is a clustering algorithm (K-nearest neighbor is a calssification algorithm), handle with unsupervised problems. K-means clustering aims to partition n observations into K clusters in which each observation belongs to the cluster with the nearest mean, serving as a prototype of the cluster.
- The number of clusters can be chosen visually or compute the SSE (sum of squared error) for some values of K to find a good K.
```
#### Q13 What is Collaborative filtering?
```
- A method of making automatic predictions about the interests of a user by collecting preferences or taste information from many users (collaborating).
- It is used in most of the recommender systems.
```
#### Q14 What is the difference between Cluster and Systematic Sampling?
```
- They differ in how they pull sample points from the population included in the sample. Cluster sampling breaks the population down into clusters, while systematic sampling uses fixed intervals from the larger population to create the sample. 
- Systematic sampling selects a random starting point from the population, and then a sample is taken from regular fixed intervals of the population depending on its size.   
  - **1** 2 3 **5** 2 4 2 **2** 1 4 **3** 4          (**x** are the selected numbers)
- Cluster sampling divides the population into clusters and then takes a simple random sample from each cluster. (It is considered less precise than other methods of sampling but sacing costs on obtaining a sample)
  - 1 2 3 5 || **2** **4** **2** **2** || 1 4 3 4    (**x** are the selected numbers)
- Stratified sampling (using simple random sampling)
  - 1 **1** || **2** 2 2 2 || **3** 3 || **4** 4 4 || 5  
```
#### Q15 Are expected value and mean value different?
```
- They are the same but the terms are used in different contexts. Mean is generally referred when talking about a probability distribution or sample population whereas expected value is generally referred in a random variable context 
  - For sampling data
    Mean value is the only value that comes from the sampling data 
    Expected value is the population mean
  - For distributions
    Mean value and expected value are same irrespective of the distribution, under the condition that the distribution is in the same population
```
#### Q16 What does P-value signify about the statistical data?
```
- P-value is used to determine the significance of results after a hypothesis test in statistics. P-value helps the readers to draw conclusion and is always between 0 and 1.
  - P-value > 0.5 denotes weak evidence against the null hypothesis which means the null hypothesis cannot be rejected.
  - P-value < 0.5 denotes strong evidence against the null hypothesis which means the null hypothesis can be rejected.
  - P-value = 0.5 the marginal value indicating it is possible to go either way.
```
#### Q17 Do gradient methods always converge to same point?
```
- No, they do not. Because in some cases it reaches a local optima or a local optima point, not the global optima point. It depends on the data and the starting conditions.
```
#### Q18 What are categorical variables?
```
- Categorical variable is one that has two or more categories, but there is no intrinsic ordering to the categories. e.g. Gender, hair color...
```
#### Q19 A test has a true positive rate of 100% and false positive rate of 5%. There is a population with a 1/1000 rate of having the condition the test identifies. Considering a positive test, what is the probability of having that condition?
```
- Let’s suppose you are being tested for a disease, if you have the illness the test will end up saying you have the illness. However, if you don’t have the illness- 5% of the times the test will end up saying you have the illness and 95% of the times the test will give accurate result that you don’t have the illness. Thus there is a 5% error in case you do not have the illness.
  - Out of 1000 people, 1 person who has the disease will get true positive result.
  - Out of the remaining 999 people, 5% will also get true positive result.
  - Close to 50 people will get a true positive result for the disease.
- This means that out of 1000 people, 51 people will be tested positive for the disease even though only one person has the illness. There is only a 2% probability of you having the disease even if your reports say that you have the disease.
```
#### Q20 How you can make data normal using Box-Cox transformation?
```
- The calculation fomula of Box-Cox can be found at https://en.wikipedia.org/wiki/Power_transform, It change the calculation between log, sqrt and reciprocal operation by changing lambda. Find a suitable lambda based on specific data set.
- Box Cox transformation is a way to transform non-normal dependent variables into a normal shape.
```   
#### Q21 What is the difference between Supervised Learning an Unsupervised Learning?
```
- If an algorithm learns from labeled data, then it is referred to as Supervised Learning. e.g. Classification
- If an algorithm does not learn from labeled data, hten it is referred to as Unsupervised Learnining. e.g. Clustering
```
#### Q22 Explain the use of Combinatorics(组合) in data science.
```
- Combinatorics used a lot in data science, from feature engineer to algorithms(ensemble algorithms).Creat new features by merge original feature and merge several networks in one to creat news, like bagging, boosting and stacking.
```
#### Q23 Why is vectorization considered a powerful method for optimizing numerical code?
```
- Vectorization can change original data to be structured.
```
#### Q24 What is the goal of A/B Testing?
```
- It is a statistical hypothesis testing for randomized experiment with two variables A and B. The goal of A/B Testing is to identify any changes to the web page to maximize or increase the outcome of an interest. Anexample for this could be identifying the click through rate for a banner ad.
```
#### Q25 What is an Eigenvalue and Eigenvector?
```
- Eigenvectors are used for understanding linear transformations. 
- In data analysis, we usually calculate the eigenvectors for a correlation or covariance matrix. Eigenvectors are the directions along which a particular linear transformation acts by flipping, compressing or stretching. Eigenvalue can be referred to as the strength of the transformation in the direction of eigenvector or the factor by which the compression occurs.
```


   
   
   
   
## Reference
- Interview questions: https://github.com/zhiqiangzhongddu/Data-Science-Interview-Questions-and-Answers-General-
- Logistic regression: https://towardsdatascience.com/introduction-to-logistic-regression-66248243c148
- 2018 100 DS Interview questions: https://www.dezyre.com/article/100-data-science-interview-questions-and-answers-general-for-2018/184
- 2017 41 Essential machine learning interview questions: https://www.springboard.com/blog/machine-learning-interview-questions/?from=message&isappinstalled=0
