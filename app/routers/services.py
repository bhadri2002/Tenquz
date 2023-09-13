from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import requests
import json
import os

open_api_key = os.getenv("OPENAI_API_KEY")

router = APIRouter()

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {open_api_key}"
}


@router.get("/service/{topic}/{level}/{mode}/{questions}")
def services(topic, level, mode, questions):
    try:
        qa = f"i need {questions} question in topicc={topic} level={level} mode={mode}"
        response = requests.post(url, json={
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": qa+" and the format should be [{question:'',# question\n questionRelatedTopic:[], # this question related topices\n options:[], # must 4 option correct one randomly place\n correctOption:'', # correct option in the form of int \n  explenation:'' # why the option is correct for \n}]\n\n the question in json format"
                }
            ],
            "temperature": 0.7
        }, headers=headers)
        # Raise an HTTPError if the response status code indicates an error
        response.raise_for_status()
        result = response.json()

        questions = []
        if "choices" in result:
            choices = result["choices"]
            for choice in choices:
                content = choice.get("message", {}).get("content")
                if content:
                    questions.append(content)
        print(questions)
        return JSONResponse(content={"questions": json.loads(questions[0]), "status": True}, status_code=200)

    except requests.exceptions.RequestException as req_err:
        raise HTTPException(
            status_code=500, detail=f"Request to OpenAI API failed: {str(req_err)}")
    except Exception as err:
        raise HTTPException(
            status_code=500, detail=f"An error occurred: {str(err)}")
