from langchain.llms import OpenAI

class Models:
  def llm_model(self):
    key = "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"
    llm = OpenAI(model_name = "gpt-3.5-turbo", openai_api_key = key, temperature = 0.7)
    return llm
