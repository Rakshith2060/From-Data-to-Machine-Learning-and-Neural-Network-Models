import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained Linear Regression model from pickle file
@st.cache(allow_output_mutation=True, hash_funcs={pickle.Unpickler: pickle.Unpickler})
def load_model():
    with open('linear_regression_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Main function
def main():
    st.title('NOx Emission Rate Predictor')

    # Load the trained model
    model = load_model()

    # Feature input from user
    st.header('Feature Selection')
    features = ['Gross Load (MW)', 'SO2 Mass (lbs)', 'Heat Input (mmBtu)', 'NOx Mass (lbs)',
                'CO2 Rate (short tons/mmBtu)', 'CO2 Mass (short tons)', 'SO2 Rate (lbs/mmBtu)']

    input_features = []
    for feature in features:
        key = f"{feature}_slider"  # Unique key based on feature name
        value = st.slider(feature, min_value=0.0, max_value=5.0, step=0.01, key=key)
        input_features.append(value)

    if st.button('Predict'):
        input_data = np.array(input_features).reshape(1, -1)
        prediction = model.predict(input_data)
        st.write('Predicted NOx Emission Rate:', prediction[0])

if __name__ == "__main__":
    main()
