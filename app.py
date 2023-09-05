import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Titre de l'application
st.title("Web Scraping")

# Entrées utilisateur
url = st.text_input("Entrez l'URL de la page à scraper:")
selector = st.text_input("Entrez le sélecteur CSS (par exemple, .s-line-clamp-4):")

# Bouton pour déclencher le scraping
if st.button("Extraire les données"):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        elements = soup.select(selector)
        data = [elem.text for elem in elements]

        # Afficher les données dans Streamlit
        st.write(data)

        # Option pour télécharger les données au format CSV
        df = pd.DataFrame(data, columns=['Données'])
        st.download_button("Télécharger les données au format CSV", df.to_csv(index=False), "donnees.csv")

    except Exception as e:
        st.error(f"Une erreur s'est produite : {e}")

