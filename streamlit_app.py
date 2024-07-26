import pandas as pd
import streamlit as st



name_qty = st.slider("Name Quantity:" 1, 20, 10)


names_df = pd.DataFrame({
    'start': ['E', 'B', 'S', 'T', 'R', 'M', 'F', 'T', 'K', 'Ev', 'L', 'V', 'A', 'Av'],
    'middle': ['le', 'ru', 'ta', 'al', 'ael', 'ol', 'ae', 'y', 'al', 'va', 'ren', 'ya', 'er', 'vi'],
    'end': ['wen', 'la', 'ki', 'nor', 'pia', 'orna', 'lin', 'wyn', 'andra', 'line', 'stae', 'daen', 'las', 'na']
        })

st.button("Reset", type="primary")
if st.button("Generage Elf Names"):
    st.divider()
    for i in range(name_qty):
        random_start = names_df['start'].sample(n = 1).values[0]
        random_middle = names_df['middle'].sample(n = 1).values[0]
        random_end = names_df['end'].sample(n = 1).values[0]
        st.write(f'{random_start}{random_middle}{random_end}')
