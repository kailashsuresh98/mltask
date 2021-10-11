from fastapi import FastAPI, File, UploadFile
from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow as tf
app =  FastAPI()

model = tf.keras.models.load_model('./app/prediction_model')
classes = ['Bed', 'Chair', 'Sofa']

def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image

def predict(image: Image.Image):
    image = np.asarray(image.resize((224, 224)))[..., :3]
    image = np.expand_dims(image, 0)
    image = image / 255.
    
    response = np.argmax(model.predict(image))

    return classes[response]

@app.post("/predict/image")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = predict(image)
    return prediction