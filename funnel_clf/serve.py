import logging
import os
import fastapi
from fastapi import FastAPI

import pkg_resources

from funnel_clf.api_models import EmailPost, EmailPostResponse
from funnel_clf.core import FunnelClf

# Read in the Log Level from env variables
LOG_LEVEL = logging.getLevelName(os.environ.get("LOG_LEVEL", "DEBUG"))

logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

# Two global objects, the fastapi ASGI server object and the Kmeans Model Classifier
MODEL_PATH = pkg_resources.resource_filename('funnel_clf', 'data/kmeans_model.joblib')
VECTORIZER_PATH = pkg_resources.resource_filename('funnel_clf', 'data/tfidf_vectorizer.joblib')

CLASSIFIER = FunnelClf.load(model_path=MODEL_PATH, vectorizer_path=VECTORIZER_PATH)
app = FastAPI()


@app.get("/")
def welcome_home():
    logger.debug("THis is a debug message.")
    return "E.T. phone  home."


@app.post("/predict", response_model=EmailPostResponse)
def predict_topic(email_model: EmailPost):
    """Predict the top topic for a given email."""
    try:
        top_topic = CLASSIFIER.predict(email_model.email)
        return EmailPostResponse(top_topic=top_topic)
    except:
        logger.error("An error occured while predicting the top topic", exc_info=True)
        raise fastapi.HTTPException(500, detail="There was an error creating the prediction response!")
