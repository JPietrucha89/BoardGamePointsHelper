import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit_app

# from modules.tokens import create_starting_bags_of_tokens
# from modules.tokens import randomly_remove_one_token_from_bag
# import Main

def test_basic():
    assert 1 > 0

def test_find_highest_score_and_player():
    test_dict = {
        "a" : 10,
        "b": 0,
        "c" : 300   
    }
    returned_key, returned_value = streamlit_app.find_highest_score_and_player(test_dict)
    assert returned_key == 'c'
    assert returned_value == test_dict['c']
    
if __name__ == '__main__':
    test_basic()
