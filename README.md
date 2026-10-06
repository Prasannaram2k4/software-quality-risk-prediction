# Software Quality Analytics and Risk Assessment

A Flask-based prototype for assessing software-module risk from code metrics. The project materials describe using historical software metrics to identify defect-prone modules and prioritize testing. Predictions are presented as **Low Risk**, **Medium Risk**, or **High Risk**.

## How it works

The final-review presentation describes a machine-learning workflow that preprocesses software metrics, trains a Random Forest classifier, and classifies modules by risk. The Flask application in `Code/app.py` collects metric values through a web form, loads a serialized model, and displays its predicted class and probabilities.

The application currently expects these files, which are **not included** in this upload:

- `software_risk_model.pkl` — trained model
- `OnlyTrivial_dt.csv` — numeric dataset used to determine model input columns
- `Code/templates/home.html`, `about.html`, `predict.html`, and `result.html` — Flask templates

The presentations also discuss a cloud-based MLP approach; the supplied Flask code is an inference wrapper and does not include model-training code or enough artifacts to establish which trained algorithm produced the serialized model.

## Screenshots

| Page | Preview |
|---|---|
| Home | ![Home page](Result%20Screenshots/HOME%20PAGE.png) |
| About | ![About page](Result%20Screenshots/ABOUT%20PAGE.png) |
| Entering metric values | ![Metric entry page](Result%20Screenshots/VALUE%20ENTERING.png) |
| Prediction | ![Prediction page](Result%20Screenshots/PREDICT%20PAGE.png) |
| Results | ![Results page](Result%20Screenshots/RESULTS%20PAGE.png) |

## Working demo

[Watch the working demo on Google Drive](https://drive.google.com/file/d/1nedXx2J-WM00mkR7zcalhTJZmjlCj0G4/view?usp=sharing).

## Project materials

- [Application source](Code/app.py)
- [Final project report](Project%20Final%20Report/PROJECT%20FINAL%20REPORT_.pdf)
- [Patent document](Patent/PATENT.pdf)
- [Review presentations](All%20Review%20PPT/) — the student ID has been redacted from the published presentation copies

## Running the application

The upload is missing the model, dataset, and HTML templates, so the application cannot run as-is. After supplying those files in the locations listed above, install the Python dependencies and start Flask from the repository root:

```bash
python -m pip install -r requirements.txt
python Code/app.py
```

The Flask development server runs locally. The source currently enables Flask debug mode; do not use the development server as a production deployment.

## Technology

Python, Flask, pandas, joblib, and a scikit-learn-compatible prediction model. The web interface uses HTML, CSS, and JavaScript (referenced by the project materials; its source files are not included in this upload).
