import streamlit as st
import pandas as pd
import json

players_names_list = []
games_dict = {}
games_list = []
game_columns_list = []

def gather_info_about_players(number_of_players = None) -> list:

    placeholder = st.empty()

    with placeholder.container():
        # input box for number_of_players
        if number_of_players is None:
            number_of_players = st.number_input("Pick number of players:", min_value= 2, max_value=6, value= "min", step = 1, key = 'number_of_players' )

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
        st.session_state.names_submitted = True
        placeholder.empty()

    return players_names_list

def import_json_and_convert_it_to_dict(path_to_json: str) -> dict:
    with open(path_to_json, 'r') as file:
        data = file.read()

    # Convert JSON String to Python
    games_dict = json.loads(data)

    # # Print Dictionary
    # print(games_dict)

    # Add games to games_list using games_dict keys
    for game_name in games_dict.keys():
        games_list.append(game_name)

    return games_dict

def page_config() -> None:
    path_to_icon = "dice_icon.png"
    st.set_page_config(
        page_title="BoardGamePointsHelper",
        page_icon = path_to_icon,
        layout="wide"
    )
    st.logo(path_to_icon, size="large", icon_image=path_to_icon)

def find_highest_score_and_player(results_dict: dict):
    # find key with Maximum value in Dictionary
    player_with_highest_score = max(zip(results_dict.values(), results_dict.keys()))[1]
    highest_score = max(zip(results_dict.values(), results_dict.keys()))[0]
    return player_with_highest_score, highest_score

def create_editable_df_for_scoring(chosen_game: str, players_names_list: list) -> pd.DataFrame:
    
    list_of_zeros = [0 for element in range( len(st.session_state.games_dict[st.session_state.chosen_game]) )]

    dict = {
        "Points category" : st.session_state.games_dict[st.session_state.chosen_game]
        }

    for player in st.session_state.players_names_list:
        dict[player] = list_of_zeros

    df = pd.DataFrame(dict)
    return df

def prepare_results_dict() -> dict:
    results_dict = {}
    for i in range(len(st.session_state.players_names_list)):
        player_name = st.session_state.players_names_list[i]
        current_player_score = edited_df[st.session_state.players_names_list[i]].sum()
        results_dict[player_name] = current_player_score
    return results_dict

def print_contents_of_dict_with_scores(highest_score: int) -> None:
    st.markdown("<h1 style='text-align: center; color: grey;'>PLAYERS</h1>", unsafe_allow_html=True)
    st.session_state.columns_list_names = st.columns(len(st.session_state.players_names_list), border = True)

    for i in range(len(st.session_state.columns_list_names)):
        with st.session_state.columns_list_names[i]:
            current_player_name = st.session_state.players_names_list[i]
            current_player_score = edited_df[st.session_state.players_names_list[i]].sum()
            results_dict[current_player_name] = current_player_score

            st.markdown(f"<h1 style='text-align: center; color: orange;'>{current_player_name}</h1>", unsafe_allow_html=True)

            if current_player_score == highest_score: #and current_player_name == player_with_highest_score:
                st.markdown(f'''<h1 style='text-align: center; color: green;'>{current_player_score}</h1>''', unsafe_allow_html=True)
            else: 
                st.markdown(f"<h1 style='text-align: center;'>{current_player_score}</h1>", unsafe_allow_html=True)
    pass

if __name__ == '__main__':
    page_config()

# DONE GATHER INFO ABOUT NUMBER OF PLAYERS AND THEIR NAMES
    if 'names_submitted' not in st.session_state:
        st.session_state.players_names_list = gather_info_about_players()

# DONE PICK A GAME FROM LIST
    if len(st.session_state.players_names_list) > 0 and 'game_dict' not in st.session_state: # and 'chosen_game' not in st.session_state:
        # DONE import JSON as dict
        st.session_state.games_dict = import_json_and_convert_it_to_dict('games_list.json')

        # DONE get games_list based on dict.keys
        # selectbox to choose particular game from games_list
        chosen_game = st.selectbox(
            "Choose a game to create a scoring board:", 
            games_list, 
            key = 'chosen_game',
            index = None,
            placeholder = "Select one game..."
        )

# DONE for this game and given number_of_players import game_columns_list and show this dataframe
    if len(st.session_state.players_names_list) > 0 and 'chosen_game' in st.session_state and st.session_state.chosen_game is not None:
        st.header("SCORING SHEET", divider = 'green')

        df = create_editable_df_for_scoring(chosen_game, players_names_list)
        edited_df = st.data_editor(df, hide_index = True, num_rows="dynamic", use_container_width=True)

# DONE PRINT SUM RESULTS
    # DONE CREATE DICT WITH SCORES AND FIND HIGHEST SCORE
        results_dict = prepare_results_dict()
        player_with_highest_score, highest_score = find_highest_score_and_player(results_dict)

    # DONE PRINT CONTENTS OF DICT WITH COLORS AND ICONS
        container = st.container(border = True)
        with container:
            print_contents_of_dict_with_scores(highest_score)

    quit()
    st.session_state