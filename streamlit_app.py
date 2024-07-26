import pandas as pd
import streamlit as st



name_qty = st.slider("Name Quantity:", 1, 20, 10)


elf_names_df = pd.DataFrame({
    'start': ['E', 'B', 'S', 'T', 'R', 'M', 'F', 'T', 'K', 'Ev', 'L', 'V', 'A', 'Av', 'D', 'Y'],
    'middle': ['le', 'ru', 'ta', 'al', 'ael', 'ol', 'ae', 'y', 'al', 'va', 'ren', 'ya', 'er', 'vi', 'vrae', 'o'],
    'end': ['wen', 'la', 'ki', 'nor', 'pia', 'orna', 'lin', 'wyn', 'andra', 'line', 'stae', 'daen', 'las', 'na', 'dorn', 'rond']
        })

goblin_names_df = pd.DataFrame({
    'start': ['S', 'R', 'S', 'G', 'Z', 'Y', 'T', 'B', 'N', 'Gr', 'Fr', 'Vr', 'Zz'],
    'Middle': ['kr', 'azz', 'chm', 'rizz', 'razz', 't', 'ok', 'wee', 'oo', 'reth', 'on', '', 'joob'],
    'end': ['ap', 'boom', 'zzle', 'z', 'bang', 'stick', 'oop', 'snick', 'snack', 'zick', 'arr', 'squee', 'squick']
})


col_1, col_2 = st.columns(2)
with col1:
    st.button("Reset", type="primary")
    if st.button("Generate Elf Names"):
        st.divider()
        for i in range(name_qty):
            elf_random_start = elf_names_df['start'].sample(n = 1).values[0]
            elf_random_middle = elf_names_df['middle'].sample(n = 1).values[0]
            elf_random_end = elf_names_df['end'].sample(n = 1).values[0]
            st.write(f'{elf_random_start}{elf_random_middle}{elf_random_end}')
with col2:
    st.button("Reset", type= "primary")
    if st.button("Generate Goblin Names"):
        st.divider()
        for i in range(name_qty):
            gob_random_start = goblin_names_df['start'].sample(n = 1).values[0]
            gob_random_middle = goblin_names_df['middle'].sample(n = 1).values[0]
            gob_random_end = goblin_names_df['end'].sample(n = 1).values[0]
            st.write(f'{gob_random_start}{gob_random_middle}{gob_random_end}')

