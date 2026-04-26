import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("ecnn_v2_model.keras")

@st.cache_data
def load_data():
    data = pd.read_csv("oulad_merged_preprocessed.csv")
    return data

@st.cache_data
def preprocess_data(data):
    selected_columns = [
        'studied_credits',
        'num_of_prev_attempts',
        'total_clicks',
        'score',
        'gender',
        'highest_education',
        'age_band',
        'imd_band',
        'region',
        'code_module'
    ] 
    if 'final_result' in data.columns:
        X = data[selected_columns].copy()
    else:
        X = data[selected_columns].copy()
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    X_cnn = np.expand_dims(X_scaled, axis=-1)
    return X, X_cnn, selected_columns
st.set_page_config(page_title="🎓 Student Performance Prediction", layout="wide")
st.title("🎓 Student Performance Prediction Dashboard")
model = load_model()
data = load_data()
X, X_cnn, selected_columns = preprocess_data(data)
st.sidebar.header("🔎 Search Student Record")
student_index = st.sidebar.number_input(
    f"Enter Student Row Number (0 - {len(data)-1})",
    min_value=0, max_value=len(data)-1, value=0
)
student = data.iloc[student_index:student_index+1][selected_columns + ['final_result']].copy()
pred_probs = model.predict(X_cnn[student_index:student_index+1])
pred_label = np.argmax(pred_probs, axis=1)[0]
confidence = np.max(pred_probs) * 100
result_map = {0: "Fail", 1: "Withdrawn", 2: "Pass", 3: "Distinction"}
st.subheader("🎯 Prediction Result")
st.write(f"**Predicted Outcome:** {result_map.get(pred_label, pred_label)}")
st.write(f"**Model Confidence:** {confidence:.2f}%")
st.subheader("📘 Student Details")
st.dataframe(student.T, use_container_width=True)
st.subheader("📊 Class Probabilities")
chart_data = pd.DataFrame({
    "Class": [result_map.get(i, str(i)) for i in range(len(pred_probs[0]))],
    "Probability": pred_probs[0]
})
st.bar_chart(chart_data.set_index("Class"))
with st.expander("📁 View Full Dataset (First 100 Rows)"):
    st.dataframe(data.head(100), use_container_width=True)
