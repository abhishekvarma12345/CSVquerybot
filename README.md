# CSVquerybot
This Generative LLM bot helps to extract useful insights from the given csv file in a simple QA fashion.

**Core Packages:**
1. [Langchain](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/pandas.html) for pandas dataframe agent. Dataframe agent takes the query and responds based on the data source. 
2. [Chainlit](https://docs.chainlit.io/overview) for easy and fast development of LLM apps. It has got the api's to spawn ChatGPT like interface in a matter of minutes. Supports simultaneous multi-user interaction with the app without extra code.

**Steps to get the app up and running:**
1. Clone the repository.
    ```bash
    git clone https://github.com/abhishekvarma12345/CSVquerybot.git
    ```
2. Edit the filename `.env.template` to `.env` and then copy and paste the OpenAI api-key.
3. Run the bash script `init_setup.sh` to create the conda environment with required dependencies.
    ```bash
    bash init_setup.sh
    ```
4. The activate the environment using the following command.
    ```bash
    source activate ./env
    ```
5. Hurray! run the script. option `-w` for automatic reload of app for code changes.
    ```bash
    chainlit run app.py -w
    ```


    



