import streamlit as st
import pandas as pd

st.title("📈 Simulatore reddito")

righe = []
reddito_guadagnato = 0
i = 0

while i < 21:
    i += 1
    reddito_guadagnato += 100
    diminuzione_pc = (reddito_guadagnato - 100) / 100 * 60
    righe.append({
        "Iterazione": i,
        "Reddito guadagnato": reddito_guadagnato,
        "Diminuz complementare": diminuzione_pc,
    })

df = pd.DataFrame(righe)

st.dataframe(df, use_container_width=True)

st.line_chart(
    df.rename(columns={
        "Iterazione": "iterazione",
        "Reddito guadagnato": "reddito",
        "Diminuz  Prestaz Compl.": "diminuzione",
    }).set_index("iterazione")
)
