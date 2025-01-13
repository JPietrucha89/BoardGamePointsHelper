import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from modules.tokens import create_starting_bags_of_tokens
# from modules.tokens import randomly_remove_one_token_from_bag
# import Main

def test_basic():
    assert 1 > 0

if __name__ == '__main__':
    test_basic()
