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
    'middle': ['kr', 'azz', 'chm', 'rizz', 'razz', 't', 'ok', 'wee', 'oo', 'reth', 'on', '', 'joob'],
    'end': ['ap', 'boom', 'zzle', 'z', 'bang', 'stick', 'oop', 'snic', 'snack', 'zick', 'arr', 'squee', 'squick']
})

dwarf_names_df = pd.DataFrame({
    'start': ['R', 'Br', 'T', 'Tr', 'Th', 'Hr', 'Kr', 'K', 'N', 'Gr', 'Fr', 'Vr', 'Dr', 'D'],
    'middle': ['ok', 'ak', 'or', 'as', 'us', 'ar', 'orn', 'yr', 'o', 'er', 'on', '', 'arn', 'a'],
    'end': ['grim', 'nar', 'brok', 'gard', 'mer', 'li', 'and', 'bard', 'ric', 'dor', 'zad', 'agg', 'rek', 'tak']
})

type = st.radio("Choose a species:", ["Elf", "Dwarf", "Goblin"])
st.divider()
st.button("Reset", type="primary")
if st.button("Generate"):

    if type == "Elf":
        for i in range(name_qty):
            st.divider()
            elf_random_start = elf_names_df['start'].sample(n = 1).values[0]
            elf_random_middle = elf_names_df['middle'].sample(n = 1).values[0]
            elf_random_end = elf_names_df['end'].sample(n = 1).values[0]
            st.write(f'{elf_random_start}{elf_random_middle}{elf_random_end}')
    elif type == "Goblin":
        for i in range(name_qty):
            st.divider()
            gob_random_start = goblin_names_df['start'].sample(n = 1).values[0]
            gob_random_middle = goblin_names_df['middle'].sample(n = 1).values[0]
            gob_random_end = goblin_names_df['end'].sample(n = 1).values[0]
            st.write(f'{gob_random_start}{gob_random_middle}{gob_random_end}')
    elif type == "Dwarf":
            st.divider()
            dwa_random_start = dwarf_names_df['start'].sample(n = 1).values[0]
            dwa_random_middle = dwarf_names_df['middle'].sample(n = 1).values[0]
            dwa_random_end = dwarf_names_df['end'].sample(n = 1).values[0]
            st.write(f'{dwa_random_start}{dwa_random_middle}{dwa_random_end}')
    else:
        st.divider()
        st.write("Make a selection.")
