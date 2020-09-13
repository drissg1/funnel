# FunnelCLF
A simple text classifier trained on an unlabeled dataset. The classifier is served via the ASGI framework fastapi and uvicorn. To deploy this model in production a process manager like gunicorn should be used. 

## Installation
Clone this repository and start an venv:
```bash
virtualenv ~/virtualenvs/funnel
source ~/virtualenvs/funnel/bin/activate
```
Once your virutalenv has started set your working directory to the newly cloned directory
and use pip to install the package funnel_clf
```bash
cd funnel
pip install .
```
This will install all the necessary dependencies for the project which are specified in the setup.py file.

## Usage
To actually start the fastapi server type in the following command in your venv.
```bash
export LOG_LEVEL=DEBUG
uvicorn funnel_clf.serve:app --reload
```
The log_level can be set to the usual suspects, INFO, WARN, CRITICAL, ERROR
and the --reload argument specifies that any changes to the source code will be reload the app (for debugging purposes)
There are other arguments like the number of workers that can be found here: [Uvicorn](https://www.uvicorn.org/settings/)

However, to run this app in production it suggested to use gunicorn with --uvicorn workers specified. The details can be found here [Uvicorn Deployment](https://www.uvicorn.org/deployment/)


## REST API
A detailed display of all the endpoints and their schemas can be found at the `/docs` endpoint of the server. One of the great features the fastapi framework. Just incase the main endpoint of interest is described below:


Currently there is only one endpoint defined for the application `/predict`
### Predict

Predict the nearest cluster of documents to a new document for classification

**URL** : `/predict`

**Method** : `POST`

**Request Format**

```json
{
  "email": "string"
}
```
**Response Format**
```json
{
  "top_topic": 0,
  "topic_distribution": [0],
  "email_topics": ["string"]
}
```
Python sample code for hitting endpoint:
```python
resp = requests.post('http://127.0.0.1:8000/predict',json={'email':email_str})
resp.json()
```


