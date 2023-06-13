import os
import pandas as pd
from pandasai import PandasAI
from dotenv import load_dotenv
from pandasai.llm.openai import OpenAI

env_loaded = load_dotenv()

# Sample DataFrame
df = pd.read_csv("Transactions.csv")

api_token = ""
if env_loaded:
    api_token = os.getenv("OPENAI_API_KEY")

llm = OpenAI(api_token=api_token)

pandas_ai = PandasAI(llm)
basic_prompt = """amount column has "€" which mean euro currency. preserve "-" symbol in the amount  column
before converting to decimal"""
print(pandas_ai(df, prompt=basic_prompt+"Display the negative and positive amount transaction amounts seperately?"))