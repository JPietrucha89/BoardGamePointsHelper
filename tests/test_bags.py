import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.tokens import create_starting_bags_of_tokens
from modules.tokens import randomly_remove_one_token_from_bag
import Main

def test_bags_of_tokens_with_Skellige():
# variant with Skellige
    # TRAIL_TOKENS_BAG = []
    # WEAKNESS_TOKENS_BAG = []
    # REMOVED_TRAIL_TOKENS_BAG = []
    # REMOVED_WEAKNESS_TOKENS_BAG = []

    TRAIL_TOKENS_BAG, WEAKNESS_TOKENS_BAG, REMOVED_TRAIL_TOKENS_BAG, REMOVED_WEAKNESS_TOKENS_BAG = create_starting_bags_of_tokens(add_skellige=True)
    assert len(TRAIL_TOKENS_BAG) == 21
    assert len(WEAKNESS_TOKENS_BAG) == 18
    assert len(REMOVED_TRAIL_TOKENS_BAG) == 0
    assert len(REMOVED_WEAKNESS_TOKENS_BAG) == 0

def test_bags_of_tokens_without_Skellige():
# variant without Skellige
    # TRAIL_TOKENS_BAG = []
    # WEAKNESS_TOKENS_BAG = []
    # REMOVED_TRAIL_TOKENS_BAG = []
    # REMOVED_WEAKNESS_TOKENS_BAG = []

    TRAIL_TOKENS_BAG, WEAKNESS_TOKENS_BAG, REMOVED_TRAIL_TOKENS_BAG, REMOVED_WEAKNESS_TOKENS_BAG = create_starting_bags_of_tokens(add_skellige=False)
    assert len(TRAIL_TOKENS_BAG) == 18
    assert len(WEAKNESS_TOKENS_BAG) == 18
    assert len(REMOVED_TRAIL_TOKENS_BAG) == 0
    assert len(REMOVED_WEAKNESS_TOKENS_BAG) == 0

def test_removing_tokens_from_bags_without_Skellige():

    TRAIL_TOKENS_BAG, WEAKNESS_TOKENS_BAG, REMOVED_TRAIL_TOKENS_BAG, REMOVED_WEAKNESS_TOKENS_BAG = create_starting_bags_of_tokens(add_skellige=False)

    for territory_type in ['FOREST', 'WATER', 'MOUNTAIN']:
        for y in range(6):
            randomly_remove_one_token_from_bag('TRAIL', territory_type)
            randomly_remove_one_token_from_bag('WEAKNESS', territory_type)

    assert len(TRAIL_TOKENS_BAG) == 0
    assert len(WEAKNESS_TOKENS_BAG) == 0
    assert len(REMOVED_TRAIL_TOKENS_BAG) == 18
    assert len(REMOVED_WEAKNESS_TOKENS_BAG) == 18

def test_removing_tokens_from_bags_with_Skellige():

    TRAIL_TOKENS_BAG, WEAKNESS_TOKENS_BAG, REMOVED_TRAIL_TOKENS_BAG, REMOVED_WEAKNESS_TOKENS_BAG = create_starting_bags_of_tokens(add_skellige=True)

    for territory_type in ['FOREST', 'WATER', 'MOUNTAIN']:
        for y in range(6):
            randomly_remove_one_token_from_bag('TRAIL', territory_type)
            randomly_remove_one_token_from_bag('WEAKNESS', territory_type)

    assert len(TRAIL_TOKENS_BAG) == 3
    assert len(WEAKNESS_TOKENS_BAG) == 0
    assert len(REMOVED_TRAIL_TOKENS_BAG) == 18
    assert len(REMOVED_WEAKNESS_TOKENS_BAG) == 18

def test_list_emptiness():
    create_starting_bags_of_tokens(add_skellige=True)
    assert Main.check_if_all_lists_are_empty() == False
    Main.clear_all_tokens_lists()
    assert Main.check_if_all_lists_are_empty() == True

if __name__ == '__main__':
    test_bags_of_tokens_with_Skellige()
    test_bags_of_tokens_without_Skellige()
    test_removing_tokens_from_bags_without_Skellige()
    test_removing_tokens_from_bags_with_Skellige()
    test_list_emptiness()
