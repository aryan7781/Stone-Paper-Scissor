# Stone-Paper-Scissors
## Introduction

<!-- Using mediapipe, we collected a large amount of data in the form of hand landmarks. To predict the user's movement, a Deep Neural Network model was developed using the landmark data.<br> -->

Let’s begin with recalling the classic game of ***“Stone Paper Scissors”***. usually played between two people, in which each player simultaneously forms one of three patterns amongst the stone, paper, or scissors with the hands. This project is a web application, in which users can play the game with the computer using the webcam. So, there is a need to build a classifier that takes images of hands as inputs and gives the user’s expected to move as output.
.<br>

The fundamental rules of Rock, Paper, Scissors apply:<br>
  -> Scissors are defeated by Rock.<br>
  -> Scissors cut paper.<br>
  -> Paper is defeated by Scissors.<br>

## Web App Sample Image
![Sample](https://github.com/aryan7781/Stone-Paper-Scissor/blob/master/images/Sample_game_img.png)

## [Development Of Machine Learning Model](https://github.com/aryan7781/Stone-Paper-Scissor/blob/master/Hand_Tracker/EDA%20and%20Machine%20Learning%20Model%20Selection/Landmarks_Analysis_for_sps.ipynb)<sub>Link to IPython Notebook</sub>
For the project, there is a need to build a classifier that takes images of hands as inputs and gives the user’s expected to move as output. Mediapipe is a library by Google that provides solutions for the recognition of key hand points. We use the library to gather Hand Landmarks for the three patterns that have meaning to the project i.e., Stone, Paper, and Scissors. The Hand Landmark Model in Mediapipe allows us to collect precise key points for 21 hand-knuckle coordinates on x and y axes inside the detected hand region.




**Dataset-** 15 thousand samples each for the patterns: “Stone”, “Paper”, and “Scissors” were collected, and used to construct a Machine Learning Model to classify new images(that has a hand representing one of the above patterns) into its respective class. These samples were used to build a machine learning model for the classification.


**ML Model-** After making required transformations in the dataset, in order to make the training smooth, and increase the expected accuracy of the model, a few fundamental Machine Learning Models like *K-Nearest Neighbors, Support Vector Classifier, Random Forests Classifier, and Extreme Gradient Boosting* were trained over the dataset, and their evaluation metrics were compared.


**Evaluation Of Models-** <br>
	-> We need a model, with high accuracy (of course, accuracy is almost always our first priority when it comes to building machine learning models).<br>
	-> The prediction time for our model, on a given dataset should be as low as possible. This is because the model has to be used to make real-time predictions on live videos of someone playing our game.
	
	
**Chosen Model-**<br>
The model that was chosen to deploy in our project-

Extreme Gradient Boost Classifier

XGBClassifier(

n_estimators = 750,

learning_rate = 0.25,

max_depth = 16

)
