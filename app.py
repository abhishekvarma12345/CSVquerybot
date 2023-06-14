import os
import pandas as pd
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import chainlit as cl
from Lib.io import BytesIO

CUSTOM_PREFIX = """
You are working with a pandas dataframe in Python. The name of the dataframe is `df`.
if Question is about the amount then report in euros. 
You should use the tools below to answer the question posed of you:"""
llm = OpenAI(temperature=0)


@cl.on_chat_start
async def ask_file():
    files = None

    while files == None:
        files = await cl.AskFileMessage(
            content = "Upload a CSV file to begin analysis!",
            accept=["text/csv"],
            max_size_mb=100,
            timeout=120
        ).send()
    
    file = files[0]
    cl.user_session.set("data", file.content) # storing the content to user session
    
    msg = cl.Message(content=f"{file.name} Upload Successful!")
    await msg.send()
    await cl.sleep(2)
    await msg.update(content="I am ready to answer the queries on {file.name}.")
    

@cl.on_message
async def request(question: str):
    bytes_data = cl.user_session.get("data")
    df = pd.read_csv(BytesIO(bytes_data))
    agent = create_pandas_dataframe_agent(llm, df, prefix=CUSTOM_PREFIX, verbose=True)
    result = agent.run(question)
    await cl.Message(content=f"{result}").send()



