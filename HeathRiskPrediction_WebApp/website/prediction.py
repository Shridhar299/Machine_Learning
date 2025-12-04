from flask import Blueprint, render_template, request
from .app_functions import ValuePredictor
import os

prediction = Blueprint('prediction', __name__)

@prediction.route('/predict', methods=["POST", 'GET'])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        
        result, page, risky_features, suggestions = ValuePredictor(to_predict_list)

        return render_template(
            "result.html",
            prediction=result,
            page=page,
            risky_features=risky_features,
            suggestions=suggestions
        )
    else:
        return render_template('base.html')
