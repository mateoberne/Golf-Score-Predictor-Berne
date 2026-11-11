# Golf Score Predictor

**CIS 3400 – Advanced Programming**  
**Project 2 – Deliverable 1: Proposal & Design**  
**Chosen Option:** Option 1 – Machine Learning Predictive Web Application

**Prototype Due:** November 23, 2026

## 1. Problem and Intended Users

Golf can be difficult, especially for beginners (like me). Many golfers want to know what score they might shoot based on their playing statistics.

For my project, I want to create a simple application that predicts a golfer's score for 18 holes.

The intended users are beginner and amateur golfers who want to understand their game and see how different statistics can affect their scores.

## 2. Chosen Project Option

I chose Option 1 – Machine Learning Predictive Web Application.

I will use Python and machine learning to predict golf scores. I will create a simple web application using Streamlit where users can enter their golf statistics and receive a predicted score.

## 3. Planned Features and Technologies

The application will allow users to:

- Enter their average driving distance.
- Enter how many fairways they hit.
- Enter how many greens in regulation they hit.
- Enter their total number of putts.
- Enter their golf handicap.
- Click a button to predict their 18-hole score.
- View previous predictions.

### Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| pandas | Organize the data |
| scikit-learn | Train the prediction model |
| Streamlit | Create the web application |
| joblib | Save the trained model |
| SQLite | Save previous predictions |
| Jupyter Notebook | Train and test the model |

## 4. Data, Model, and Application Architecture

I plan to find a golf dataset with information about player statistics and final scores.

If I cannot find a suitable dataset, I will create sample data for this project. Predictions using sample data will only be for demonstration.

I will use pandas to prepare the data and scikit-learn to train a Random Forest regression model.

The application will work like this:

1. The user enters their golf statistics.
2. The application checks the inputs.
3. The machine learning model predicts a score.
4. The predicted score appears on the screen.
5. The user can save and view previous predictions.

### Planned Project Files

- `train_model.ipynb` – Train the prediction model.
- `golf_predictor.py` – Python class that makes predictions.
- `app.py` – Streamlit web application.
- `database.py` – Save and load previous predictions.
- `golf_model.joblib` – Saved machine learning model.
- `README.md` – Project information and instructions.

## 5. Preliminary Interface Sketch

### Golf Score Predictor

**Average driving distance:** 230 yards

**Fairways hit:** 6

**Greens in regulation:** 4

**Total putts:** 36

**Golf handicap:** 25

**[ PREDICT SCORE ]**

**Predicted 18-hole score: 98**

*This is only an example result.*

**[ VIEW PREVIOUS PREDICTIONS ]**

## 6. Implementation Sequence and Milestones

| Date | Planned Work |
|---|---|
| November 16 | Submit project proposal |
| November 17–19 | Find or create data and train model |
| November 20–22 | Build the Streamlit application |
| November 23 | Show working prototype |
| November 24–30 | Add prediction history |
| December 1–7 | Test and fix errors |
| December 8 | Submit final project |

For the prototype, I want users to be able to enter their statistics and receive a predicted score.

For the final project, I want a complete application with a simple interface and prediction history.

## 7. Anticipated Challenges

Some challenges I might face are:

- Finding good golf data.
- Training the machine learning model.
- Connecting the model to Streamlit.
- Saving previous predictions.
- Fixing errors in the code.

I will test the application while building it and try to fix any problems.

## 8. AI Development Plan and Disclosure

I plan to use AI to help me understand Python code, fix errors, and build parts of my application.

I will review and test the code to make sure I understand how it works. I will also explain how I used AI in my final submission.
