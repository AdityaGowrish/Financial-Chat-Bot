from data_collector import DataCollector
from questionanswer import Question
from summarization import SummaryChain
from stt import Stt
from tts import Tts

def main():
    data_collect = Data_Collector()
    data = data_collect.Collector()
    
    sum_chain = SummaryChain()
    summarychain = sum_chain.summary_chain(data)
    
    speechtotxt = Stt()
    query = speechtotxt.STT()

    qa = Question()
    answer = qa.QA_Chain(query,data)

    txttospeech = Tts()
    speech = txttospeech.TTS(answer)

if __name__ == "__main__":
     main()
