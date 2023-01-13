 #    ******* PACKAGES*********
import streamlit as st
import pandas as pd
import numpy as np
import requests as req
st.set_page_config(layout="wide")

#    ******* Mise en page du site *********

    #putting an image to the background

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images3.alphacoders.com/114/thumb-1920-11439.png");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
add_bg_from_url()

title = '<h1 style="font-family:verdana; text-align:center; color:Yellow; font-size: 160px;">Star Wars</h1>'
st.markdown(title, unsafe_allow_html=True)

sub_title = '<p style="font-family:courier; text-align:center; color:White; font-size: 45px;"> &#9994 <i> May  THE FORCE BE WITH YOU </i> &#9994 </p>'
st.markdown(sub_title, unsafe_allow_html=True)


base_url = "https://swapi.dev/api/{}/?search={}" # adresse url api de swapi

#****************************************************

    #    ******* Recuperer les infos de l'api  *********

def get_data(url):
    resp = req.get(url)
    return resp.json()

     #    ******* Navigation form *********

with st.form(key='searchform'):
    slct1, slct2 ,slct3= st.columns([3,2,1])

    with slct1:
        option = st.selectbox('**Choose a catgory** ',
          ('','films', 'people', 'planets','starships','species','vehicles'))
    with slct2:
        name = st.text_input("**Name**")
    with slct3:
        st.markdown(":arrow_down_small::arrow_down_small:")
        submit_search= st.form_submit_button(label='Search')

    #    ******* Connexion *********

st.success(f"You search for {name} in {option}")

col1, col2 = st.columns([2,1])

with col1:
    if submit_search:
            #create Search Query
            search_url = base_url.format(option,name)
            #st.write(search_url)
            data = get_data(search_url)
            #st.write(data)
            info = list(data["results"][0].values())
            #for content in :
            #    nom = content["name"]
            #st.write(info)
            if option == "planets":
                st.write("Bienvenue sur la planete {}, qui a une population de {} habitants.".format(info[0],info[8]))
                st.write("Cette planete fait {} km de diametre pour une surface d'eau égale à {}.".format(info[3],info[7]))
                st.write("Le terrain est {} à cause du climat {} et une gravité de {}.".format(info[6],info[4],info[5]))
                st.write("Sa periode de rotation est de  {} USW pour une période orbitale de {} USW.".format(info[1],info[2]))

            elif option == "people":
                st.write("{} is a {} with {} eyes, {} hair and {} skin ".format(info[0],info[7],info[5],info[3],info[4]))
                st.write("He is born on {} and weight {} Kg for a height of {} inches".format(info[6],info[2],info[1]))

            elif option == "films":
                st.write(" Title = {}".format(info[0]))
                st.write("Director = {}".format(info[3]))
                st.write("Producer = {}".format(info[4]))
                st.write("Release_date = {}".format(info[5]))

            elif option == "starships'":
                st.write("Name = {}".format(info[0]))
                st.write("Model = {}".format(info[1]))
                st.write("Manufacturer= {}".format(info[2]))
                st.write("Cost_in_credits= {}".format(info[3]))
                st.write("Lenght = {}".format(info[4]))
                st.write("Max_atmosphering_speed = {}".format(info[5]))
                st.write("Crew= {}".format(info[6]))
                st.write("Passengers= {}".format(info[7]))
                st.write("Cargo_capacity = {}".format(info[8]))
                st.write("Consumables = {}".format(info[9]))
                st.write("Hyperdrive_rating = {}".format(info[10]))
                st.write("MGLT= {}".format(info[11]))
                st.write("Starship_class= {}".format(info[12]))

            elif option == "species":
                st.write("Name = {}".format(info[0]))
                st.write("Classification = {}".format(info[1]))
                st.write("Designation= {}".format(info[2]))
                st.write("Average_height = {}".format(info[3]))
                st.write("Skin_colors = {}".format(info[4]))
                st.write("Hair_colors = {}".format(info[5]))
                st.write("eye_colors = {}".format(info[6]))
                st.write("Average_lifespan = {}".format(info[7]))
                st.write("Homeworld = {}".format(info[8]))
                st.write("Language = {}".format(info[9]))

            else:
                st.write("Name = {}".format(info[0]))
                st.write("Model = {}".format(info[1]))
                st.write("Manufacturer= {}".format(info[2]))
                st.write("Cost_in_credits= {}".format(info[3]))
                st.write("Lenght = {}".format(info[4]))
                st.write("Max_atmosphering_speed = {}".format(info[5]))
                st.write("Crew= {}".format(info[6]))
                st.write("Passengers= {}".format(info[7]))
                st.write(" Consumables = {}".format(info[8]))
                st.write("Vehicles_class = {}".format(info[9]))




#***************************************************
    # Another way to make the home page
    #*******************************************
#def main():
   # menu = ["Home","About","Divers"]
   # choice = st.sidebar.selectbox("Menu",menu)

   # st.title(":red[Stars Wars]") #my site title
   # st.subheader(":fist: _May  THE FORCE BE WITH YOU_ :fist:")

   # if choice == "Home":
    #    st.subheader("Home")
   # elif choice == "About":
   #     st.subheader("About")
   # else :
   #     st.subheader("Divers")

#if __name__ == '__main__':
   ## main()
#st.markdown("**:orange[]**")

    #*************************************************
