# # Real-time Financial Chat-bot with OpenAI's Chat LLM

Welcome to the Real-time Financial Chat-bot project! This repository contains the code and resources for creating a interactive chat-bot that provides accurate and real-time information about the stock exchange using OpenAI's Chat Language Model (LLM).

The project uses Langchain, a versatile library for working with language models, and leverages FastAPI to deploy the chat-bot with ease. By combining advanced natural language processing with real-time financial data extraction and summarization, this chat-bot offers answers for users seeking insights into the stock market.

## Features

- **Real-time Financial Information**: The chat-bot utilizes Langchain to connect with OpenAI's Chat LLM, allowing users to ask questions about stock exchange trends and updates.

- **Data Extraction and Summarization**: The chat-bot is deployed using FastAPI. It extracts and summarizes real-time financial data, ensuring that users receive concise and up-to-date information.

- **Accurate User Queries**: The chat-bot processes user queries and responds with accurate answers related to stock exchange data, enhancing the user's understanding of financial markets.

- **Interactive Communication**: With the integration of the Whisper API and Google Text to Speech API, the chat-bot can communicate with users in a conversational manner, making interactions more engaging and informative.

- **Modular Coding Approach**: The project is built using a modular coding approach, making it easy to understand, extend, and maintain. The FastAPI framework provides a solid foundation for deploying the chat-bot effectively.

## Setup and Usage

1. Clone this repository to your local machine.
   
   ```bash
   git clone https://github.com/AdityaGowrish/Financial-Chat-Bot.git
   cd financial-chat-bot
   ```

2. Install the required dependencies using `pip`.

   ```bash
   pip install -r requirements.txt
   ```

3. Configure API Keys:
   - Obtain your OpenAI API key and update it in the appropriate configuration file.
   - Obtain Whisper API and Google Text to Speech API keys and update them as needed.

4. Run the FastAPI server:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

5. Access the chat-bot by opening a web browser and navigating to `http://localhost:8000`.

---
