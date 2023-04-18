# Naive Bayes classifier
Naive Bayes is a simple technique for constructing classifiers: models that assign class labels to problem instances, represented as vectors of feature values, where the class labels are drawn from some finite set. There is not a single algorithm for training such classifiers, but a family of algorithms based on a common principle: all naive Bayes classifiers assume that the value of a particular feature is independent of the value of any other feature, given the class variable. For example, a fruit may be considered to be an apple if it is red, round, and about 10 cm in diameter. A naive Bayes classifier considers each of these features to contribute independently to the probability that this fruit is an apple, regardless of any possible correlations between the color, roundness, and diameter features.
(referenced from wikipidia)

# Project Description
+ In this projcet, I implement a Naive Bayes Classifier (NBC) for sentiment analysis on a dataset containing reviews and their respective star ratings.
+ In this projcet, I use only built-in packages like cvs, sys, and so on

# Project Implementation
+ For execution, you need to download the following file.
  + train.csv: using for taining 
  + test.csv: using for testing model
  + stop_word.txt: list of stop words that should be removed

# How to use Project
+ Function NBC
  + The NBC function receives the percent of training set as a parameter.
  + Extract 1,000 features using the training set according to the specified percent and print top 20 to 50 print out one at a line before testing
  + Calculate the conditional probability for each feature
  + In the test step, each input line is classified with the probability calculated in the training step
  + Finally, return the Accuracy.
    + The Accuracy is as follows

+ Function Learning Curve
  + If you store the results of the NBC function and pass them to the Learning Curve function in the form of an list, it is a function that draws the Learning Curve
    + The Learning Curve is as follows
