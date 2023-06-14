# CSVquerybot
This Generative LLM bot helps to extract useful insights from the given csv file in a simple QA fashion.

**Functionalities:**
1. Ask user to upload a CSV file.
    - using chainlit for conversation between user and bot.
    - read the CSV file into pandas DataFrame object.
2. Process the message of the user to answer the queries on the uploaded CSV file.
    - Use langchain to create CSV agent to answer user questions on the CSV file.


