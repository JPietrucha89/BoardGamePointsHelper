import streamlit as st
import pandas as pd

players_names_list = []
games_list = []
game_columns_list = []

def gather_info_about_players(number_of_players = None):

    placeholder = st.empty()

    with placeholder.container():
        # input box for number_of_players
        if number_of_players is None:
            number_of_players = st.number_input("Pick number of players:", min_value= 2, max_value=6, value= "min", step = 1, )

        # create submit_form to collect names of all players
        with st.form("my_form"):
            for player_number in range(1, number_of_players + 1):
                st.text_input(
                        f"Enter name for Player#{player_number}:👇",
                        placeholder= f"Player#{player_number}",
                        key = f"player_name_{player_number}"
                    )
            names_submitted = st.form_submit_button()
            if names_submitted:
                for player_number in range(1, number_of_players + 1):
                    players_names_list.append(st.session_state[f'player_name_{player_number}'])
                
    if names_submitted:
        # st.write(players_names_list)
        placeholder.empty()

if __name__ == '__main__':

    # GATHER INFO ABOUT NUMBER OF PLAYERS AND THEIR NAMES
    gather_info_about_players()
    st.write(players_names_list)

    # some kind of selectbox to choose particular game from games_list

    # for this game and given number_of_players import game_columns_list and show this dataframe directly or do a transpose first