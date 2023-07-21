from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pickle

with open('model/model_sms_classification.pkl', 'rb') as file:
    loaded_model = pickle.load(file)


app = FastAPI()

@app.get("/check-spam/{text}")

def check_spam(text: str):

    if loaded_model.predict([text]) == 1:
        response = {
            "code": 200,
            "message": "spam"
        }
    else:
        response = {
            "code": 200,
            "message": "not spam"
        }

    return JSONResponse(content=response)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)