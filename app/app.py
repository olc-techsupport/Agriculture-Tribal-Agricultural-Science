from pathlib import Path
import pandas as pd
import streamlit as st
ROOT=Path(__file__).resolve().parents[1]; PROCESSED=ROOT/"data"/"processed"
st.set_page_config(page_title="Tribal Agriculture & Land Health",layout="wide")
st.title("Tribal Agriculture & Land Health")
st.warning("Local governed-data view. Do not publish or export without documented Tribal authority.")
files=sorted(PROCESSED.glob("*.parquet"))
if not files: st.info("No processed datasets. Run the local pipeline after adding authorized inputs.")
else:
    selected=st.selectbox("Dataset",files,format_func=lambda p:p.stem.replace("_"," ").title())
    frame=pd.read_parquet(selected); st.metric("Validated rows",len(frame)); st.dataframe(frame,use_container_width=True)
    st.caption("Exports are intentionally disabled.")
