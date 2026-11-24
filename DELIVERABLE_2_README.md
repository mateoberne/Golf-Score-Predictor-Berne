## Deliverable 2 – Working Prototype (November 23, 2026)

The prototype uses a Random Forest regression model to estimate an 18-hole golf score from driving distance, fairways hit, greens in regulation, total putts, and handicap. The model was trained on 2,000 synthetic rounds for demonstration purposes.

### How to run

Use Python 3.11 or 3.12. In the project folder, run:

```bash
python3 -m pip install -r requirements.txt
python3 -m streamlit run app.py
```

Enter five statistics and click Predict Score. Example: 230 yards, 6 fairways, 4 greens, 36 putts, handicap 25 produces a prediction of 97.

### Current status

- Created a synthetic dataset and trained and saved the Random Forest model.
- Tested the model and Python prediction class together.
- Created the Streamlit interface; local browser demonstration still needs verification.
- Remaining: SQLite prediction history, interface improvements, additional testing, and final documentation.

The model achieved a mean absolute error of 2.59 strokes on held-out synthetic data. This is not evidence of real-world predictive accuracy.

### AI disclosure

AI assisted with code generation, organization, and model testing. I will review and test the application locally before demonstrating it.
