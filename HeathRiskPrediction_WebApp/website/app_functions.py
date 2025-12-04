import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load Keras model for images
def get_image_model(path):
    return load_model(path, compile=False)

# Predict from image
def pred_image(path, model_path):
    img = load_img(path, target_size=(224, 224))
    data = img_to_array(img) / 255.0
    data = np.expand_dims(data, axis=0)
    model = get_image_model(model_path)
    predicted = np.round(model.predict(data)[0])[0]
    return predicted

# Predict from tabular data
def ValuePredictor(to_predict_list):
    # Heart disease prediction (11 features)
    if len(to_predict_list) == 11:
        page = 'heart'
        feature_names = [
            "age", "sex", "cp", "trestbps", "chol", "fbs",
            "restecg", "thalach", "exang", "oldpeak", "slope"
        ]

        # Descriptive thresholds for basic guidance
        thresholds = {
            "resting blood pressure": 130,   # trestbps
            "cholesterol": 200,              # chol
            "fasting blood sugar": 1,        # fbs
            "maximum heart rate": 140,       # thalach
            "depression level": 1.0          # oldpeak
        }

        name_map = {
            "trestbps": "resting blood pressure",
            "chol": "cholesterol",
            "fbs": "fasting blood sugar",
            "thalach": "maximum heart rate",
            "oldpeak": "depression level"
        }

        risky_features = []
        suggestions = []

        for i, feature in enumerate(feature_names):
            if feature in name_map:
                descriptive_name = name_map[feature]
                threshold = thresholds[descriptive_name]
                val = to_predict_list[i]

                if (descriptive_name == "maximum heart rate" and val < threshold) or \
                   (descriptive_name != "maximum heart rate" and val > threshold):
                    risky_features.append(descriptive_name)
                    suggestions.append(
                        f"Your {descriptive_name} value ({val}) is outside the recommended range ({threshold}). "
                        "Consider lifestyle changes or consulting a doctor."
                    )

        # Load heart model and predict
        with open('./website/app_models/heart_model.pkl', 'rb') as f:
            model = pickle.load(f)
        pred = model.predict(np.array(to_predict_list).reshape(1, -1))

        return pred[0], page, risky_features, suggestions

    # Unsupported feature length
    else:
        raise ValueError("Only heart prediction is supported. Provide 11 features for heart prediction.")
