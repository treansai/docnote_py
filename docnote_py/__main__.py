# main.py
import fastapi
import uvicorn
from app.logger import logger
from app.model import Model

app = fastapi.FastAPI()
model = Model(
    model_name="Clinical-AI-Apollo/Medical-NER",
    prefix="filigran-ner-",
    tokenizer_name="Clinical-AI-Apollo/Medical-NER")

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/predict")
async def predict(text: str):
    logger.info(f"Predicting {text}")
    predictions = model.predict(text)
    
    # Convert the predictions to a serializable format
    formatted_predictions = []
    for pred in predictions:
        formatted_pred = {
            'entity': pred['entity'],
            'word': pred['word'],
            'score': float(pred['score']),  # Convert numpy.float32 to Python float
            'start': pred['start'],
            'end': pred['end'],
            'index': pred['index']
        }
        formatted_predictions.append(formatted_pred)
    
    return formatted_predictions

if __name__ == "__main__":
    logger.info("Starting app")
    uvicorn.run(app, host="0.0.0.0", port=8090)