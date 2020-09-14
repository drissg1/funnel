from joblib import load
import email
import logging
import time

logger = logging.getLogger(__name__)


class FunnelClf:
    def __init__(self, model, vectorizer):
        """The Wrapper Class around sklearn model and vectorizer

        Args:
            model: The sklearn model to be used for prediction
            vectorizer: The vectorizer that has a transform method on strings to vectorizer for model
        """
        self.model = model
        self.vectorizer = vectorizer
        self.email_parser = email.parser.Parser()

    @classmethod
    def load(cls, vectorizer_path: str, model_path: str):
        logger.info(f"Loading the model from {model_path}")
        logger.info(f"Loading the vectorizer from {vectorizer_path}")
        model = load(model_path)
        vectorizer = load(vectorizer_path)
        return cls(model=model, vectorizer=vectorizer)

    def predict(self, email: str):
        """Used to predict which cluster the email belongs to

        Args:
            email: The string representing the subject + body
        """
        start = time.perf_counter()
        email_msg = self.email_parser.parsestr(email)
        subject = email_msg.get("Subject", "")
        body = get_body(email_msg)
        doc = subject + body
        logger.debug(f"Predicting on doc of size {len(doc)}")
        email_bow = self.vectorizer.transform([doc])
        top_topic = self.model.predict(email_bow)[0]
        end = time.perf_counter()
        print(f"Predicted the top topic in  {end - start:0.4f} seconds")
        return top_topic


def get_body(email_msg):
    """Grab the body from a parsed email object

    Args:
        email_msg: The parsed email message
    """
    body = ""
    if email_msg.is_multipart():
        for payload in email_msg.get_payload():
            body += payload.get_payload().strip()
    else:
        body = email_msg.get_payload().strip()
    if body:
        return body
    else:
        return ""
