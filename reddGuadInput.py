import streamlit as st
import pandas as pd

st.title("📉 Simulatore diminuzione reddito")

redditoGuadagnato= st.number_input("quanto hai guadagnato? ")# qui chiedo all'utente quindi dovrò annullare il ciclo while 
#i=0
#diminuzionePc =0
#while i<21:
 # i+=1
  #redditoGuadagnato+=100
diminuzionePc= (redditoGuadagnato - 100)/100*67
print("redditoGuadagnato =",   redditoGuadagnato, " >>> diminuzionePc =", diminuzionePc)

# Tabella di confronto per qualche valore di riferimento
#valori_riferimento = [100, 200, 500, 800, 1000]
#tabella = pd.DataFrame([
  #  {
   #     "Reddito": v,
    #    "Diminuzione %": max(0, (v - 100) / 100 * 60),
    #}
    #for v in valori_riferimento
#])
#st.dataframe(tabella, use_container_width=True)
