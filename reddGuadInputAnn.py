import streamlit as st
import pandas as pd

st.title("📉 Simulatore diminuzione complementare")
redditoGuadagnato = 1500
redditoGuadagnato=st.number_input("quanto hai guadagnato annualmente?") #, step=1 )# qui chiedo all'utente quindi dovrò annullare il ciclo while 
#i=0
diminuzionePc =0
#while i<21:
 # i+=1
#redditoGuadagnato+=100
diminuzionePc= (redditoGuadagnato - 1500)/100*67
if redditoGuadagnato >= 1500:
    st.write("redditoAnnualeGuadagnato =",   redditoGuadagnato, " >>> diminuzioneAnnualePc =", diminuzionePc)

# Tabella di confronto per qualche valore di riferimento
valori_riferimento = [1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
tabella = pd.DataFrame([
    {
        "Reddito": v,
        "Diminuzione ": max(0, (v - 1500) / 100 * 67),
    }
    for v in valori_riferimento
])
st.dataframe(tabella, use_container_width=True)
