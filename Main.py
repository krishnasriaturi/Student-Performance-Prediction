import tensorflow as tf
import pandas as pd

model = tf.keras.models.load_model("ecnn_v2_model.keras")
data = pd.read_csv("oulad_merged_preprocessed.csv")
preds = pd.read_csv("ecnn_v2_predictions.csv")
