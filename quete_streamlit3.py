import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'Damien',
   'password': 'Damdam',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()


if st.session_state["authentication_status"]:
    with st.sidebar:
        authenticator.logout("Déconnexion", "sidebar")  # Le bouton de déconnexion
        selection = option_menu(
        menu_title=None,
        options = ["Accueil", "Photos de mon chien"],
        icons=["house", "camera"],
        menu_icon="cast",
    )
    if selection == "Accueil":
        st.title("Bienvenu sur ma page")
        st.image("https://pngimg.com/uploads/welcome/welcome_PNG78.png")
    elif selection == "Photos de mon chien":
        st.title("Voici des photos de mon chien")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Suki bébé")
            st.image("images/20170606_071225-COLLAGE.jpg") 
        with col2:
            st.header("Suki couchée")
            st.image("images/IMG_20171210_212500.jpg") 
        with col3:
            st.header("Suki pirate")
            st.image("images/IMG_20181119_195916.jpg") 

        
    
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
