import streamlit as st
import requests
import pandas as pd
from typing import Optional, Union, Dict, Any

FASTAPI_URL = "http://localhost:8000"

def get_data(endpoint: str, input_params: Optional[Dict[str, Any]] = None, method: str = "GET") -> Union[pd.DataFrame, Dict[str, Any], None]:
    if input_params is None:
        input_params = {}

    if method == "GET":
        response = requests.get(f"{FASTAPI_URL}/{endpoint}", params=input_params)
        if response.status_code == 200:
            payload = response.json()
            rows = payload.get("data", [])
            return pd.DataFrame(rows)
        else:
            st.error(f"Error fetching data: {response.status_code}")
            return pd.DataFrame()

    if method == "POST":
        response = requests.post(f"{FASTAPI_URL}/{endpoint}", json=input_params)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error posting data: {response.status_code}")
            return None

    st.error(f"Unsupported request method: {method}")
    return None

   