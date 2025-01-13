from modules.tokens import get_color_for_token

def test_get_color_for_token():
    assert get_color_for_token('TRAIL_FOREST_') == 'green'
    assert get_color_for_token('TRAIL_WATER_') == 'blue'
    assert get_color_for_token('TRAIL_MOUNTAIN') == 'grey'
    assert get_color_for_token('WEAKNESS_FOREST_') == 'green'
    assert get_color_for_token('WEAKNESS_WATER_') == 'blue'
    assert get_color_for_token('WEAKNESS_MOUNTAIN') == 'grey'