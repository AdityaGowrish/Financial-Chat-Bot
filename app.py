from typing import Union, Dict
from fastapi import FastAPI
from pydantic import BaseModel
from data_collector import Data_Collector
from questionanswer import Question
from summarization import Summary_Chain
from stt import Stt
from tts import Tts
import llm_model 
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def inputs():
  return {"Message" : "Give me a link"}

@app.get("/Link")
def read_item(Links: str):
  return {"Your Link is " : Links}

@app.get("/LLM")
def main(link: str):
    data_collect = Data_Collector()
    data = data_collect.Collector(link)

    sum_chain = Summary_Chain()
    summarychain = sum_chain.summary_chain(data)

    speechtotxt = Stt()
    query = speechtotxt.STT()

    qa = Question()
    answer = qa.QA_Chain(query,data)

    txttospeech = Tts()
    speech = txttospeech.TTS(answer)
    return {"Your Answer is : " : answer}
    
@app.get(path="/api/media-file")
async def post_media_file():
    return FileResponse("1.mp3", media_type="audio/mpeg")  

if __name__ == "__main__":
     main()
