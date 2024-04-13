import gradio as gr
from joblib import load

def predict_price(latitude, longitude):
    loaded_model = load('models/regression_model_3_23_pm_13_apr_2024.joblib')
    predicted_price = loaded_model.predict([[float(latitude), float(longitude)]])
    return str(round(predicted_price[0]))

inputs = [
    gr.inputs.Textbox(label="Latitude"),
    gr.inputs.Textbox(label="Longitude")
]

output = gr.outputs.Textbox(label="Predicted Price")

gr.Interface(fn=predict_price, inputs=inputs, outputs=output, title="Charger price prediction",
             description="Enter latitude and longitude to predict charger price.").launch()
