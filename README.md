# Text Review Prediction App 📊

## Description  
This app predicts the sentiment of text reviews using different machine learning models: **Decision Tree (DT)**, **Support Vector Machine (SVM)**, and **Logistic Regression (LR)**. Users can input a review, and the app will predict the sentiment using the chosen model.

## Features  
- **Multiple models**: Choose between **DT**, **SVM**, and **LR** models for predicting the sentiment of a text review.  
- **Text preprocessing**: The app preprocesses the input text before making predictions.  
- **Real-time predictions**: Predictions are displayed immediately after entering a review and pressing the prediction button.

## Installation  
To run the application locally, follow these steps:

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/text-review-prediction-app.git
   cd text-review-prediction-app
Install the required dependencies:
pip install -r requirements.txt

Run the Streamlit app:
streamlit run app.py

Input Features
The app requires the following input:

Text Review: Enter your review for sentiment analysis.
The review can be any textual input that needs to be classified by the model.
Model Details
Decision Tree (DT): A tree-based model that classifies the input text based on learned patterns from the training data.
Support Vector Machine (SVM): A powerful classifier that finds the optimal hyperplane to separate text into categories.
Logistic Regression (LR): A linear model that predicts sentiment by analyzing text features.

Text Preprocessing
Before making predictions, the input text is processed to:

Remove unwanted characters
Tokenize and normalize the text
Perform other necessary text cleaning steps.
Files
app.py: Main application file for the Streamlit app.
dt.pkl: Pre-trained Decision Tree model.
svc.pkl: Pre-trained Support Vector Machine model.
lr.pkl: Pre-trained Logistic Regression model.
helper.py: Contains text preprocessing functions.
requirements.txt: List of Python dependencies.
Dependencies
Streamlit
Pickle
Scikit-learn
Pandas
Numpy
Example Usage
Enter the text review in the input box for any of the models.
Click the "Predict_dt", "Predict_SVM", or "Predict_lr" button to get the sentiment prediction from the respective model.
The prediction will be displayed immediately, showing the model's classification.
Screenshots
Here’s how the app looks:

Author
👨‍💻 Nader Nageh Mansour

Email: nadernageh22508@gmail.com
GitHub: [Your GitHub Profile](https://github.com/nader108)
License
This project is licensed under the MIT License.
Feel free to use it, modify it, and share it.

