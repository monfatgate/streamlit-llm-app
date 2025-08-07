import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm_response(input_text: str, expert_type: str) -> str:
    """
    入力テキストと専門家タイプを受け取り、LLMからの回答を返す
    
    Args:
        input_text (str): ユーザーからの入力テキスト
        expert_type (str): 選択された専門家のタイプ
    
    Returns:
        str: LLMからの回答
    """
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    
    system_messages = {
        "医療専門家": "あなたは医療の専門家です。患者の症状に基づいて適切なアドバイスを提供してください。",
        "法律専門家": "あなたは法律の専門家です。法律に関する質問に対して正確な情報を提供してください。"
    }
    # LLMに渡すメッセージリストを変数として定義
    messages = [
        SystemMessage(content=system_messages[expert_type]),
        HumanMessage(content=input_text)
    ]
    # LLMに問い合わせ
    response = llm(messages)
    
    return response.content

options = ["医療専門家", "法律専門家"]
expert_type = st.radio("専門家を選択してください:", options)
user_input = st.text_area("質問を入力してください:")
if st.button("送信"):
    if user_input:
        # LLM関数を呼び出し
        response = get_llm_response(user_input, expert_type)
        # 結果を表示
        st.write(response)
    else:
        st.error("質問を入力してください。")