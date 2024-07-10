import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents.format_scratchpad.openai_tools import format_to_openai_tool_messages
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain.memory import ConversationBufferMemory
import os
import json
from tools import request_bank_balance_iso_format, request_paytm_balance_enquiry, tools

# Set page config at the very top
st.set_page_config(page_title="Financial Request Generator", page_icon="💰")

# Load OpenAI API key from Streamlit secrets
openai_api_key = st.secrets["openai"]["api_key"]

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    openai_api_key=openai_api_key  # Pass the API key to the LLM
)

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an intelligent assistant specialized in generating structured financial requests based on user queries. 
    Your primary function is to interpret user inputs and create appropriate JSON or ISO 8583 formatted requests for various financial operations.
    
    Follow these steps:
    1. If the user mentions 'bank balance' without specifying the type, ask them to clarify whether they want a Paytm balance or an ISO format bank balance.
    2. Once the type is clear, check if all required parameters are provided.
    3. If any required information is missing, ask the user to provide it.
    4. Only generate the request when all necessary information is available.
    5. Do not include any sensitive information like actual account numbers or passwords in your responses.
    6. Use emojis occasionally to maintain a friendly tone.

    Available request types:
    1. Paytm Balance Enquiry (JSON format)
    2. Bank Balance Enquiry (ISO 8583 format)
    
    Remember to always clarify the type of balance enquiry before proceeding.
    Always strictly remember the output you give must be either in JSON format or ISO format strictly based on the user query
    If user mentions about generating request for Paytm Bank Balance Enquiry you must respond the request in JSON format
    If user mentions about generating request for Bank Balance enquiry you must respond in ISO 8583 format
    """),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

llm_with_tools = llm.bind_tools(tools)

agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(x["intermediate_steps"])
    }
    | prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def process_user_input(user_input: str):
    """
    Process user input and generate the appropriate financial request.
    
    :param user_input: The user's query or input
    :return: The generated financial request and any additional information
    """
    response = agent_executor.invoke({"input": user_input})
    return response

def main():
    st.title("💰 Financial Request Generator")
    st.write("Welcome! This tool helps you generate structured financial requests. Just type your request, and I'll help you create the appropriate JSON or ISO 8583 format.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What financial request would you like to generate?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = process_user_input(prompt)
            
            # Display the assistant's response
            message_placeholder.markdown(full_response['output'])
            
            # Display the JSON structure
            if 'intermediate_steps' in full_response and full_response['intermediate_steps']:
                tool_response = full_response['intermediate_steps'][0][1]
                try:
                    json_response = json.loads(tool_response)
                    st.json(json_response)
                except json.JSONDecodeError:
                    st.code(tool_response, language='xml')
            
        st.session_state.messages.append({"role": "assistant", "content": full_response['output']})

if __name__ == "__main__":
    main()
