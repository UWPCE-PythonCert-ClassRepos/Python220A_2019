"""
grade l9 part 3
"""
import pytest

from src import jpgdiscover as sut

@pytest.fixture
def _test_list_jpg_files():
    """ structure from test """
    return  [
        "/Users/viviata/Git/Python220A_2019/students/visokoo/lesson09/assignment/data/old", ["sitting_in_chair_relaxing_400_clr_6028.png", "couple_on_swing_bench_400_clr_12844.png"],
        "/Users/viviata/Git/Python220A_2019/students/visokoo/lesson09/assignment/data/furniture/chair", ["metal_chair_back_isometric_400_clr_17527.png"],
        "/Users/viviata/Git/Python220A_2019/students/visokoo/lesson09/assignment/data/furniture/chair/couch", ["sofa_400_clr_10056.png"],
        "/Users/viviata/Git/Python220A_2019/students/visokoo/lesson09/assignment/data/furniture/table", ["table_with_cloth_400_clr_10664.png", "basic_desk_main_400_clr_17523.png", "desk_isometric_back_400_clr_17524.png"],
        "/Users/viviata/Git/Python220A_2019/students/visokoo/lesson09/assignment/data/new", ["chairs_balancing_stacked_400_clr_11525.png", "hotel_room_400_clr_12721.png"]]

def test_list_jpg_files(_test_list_jpg_files):
    """ student geneartes """
    jpgs = sut.list_jpg_files("/Users/viviata/Git/Python220A_2019/students/visokoo/lesson09/assignment/data/")
    assert jpgs == _test_list_jpg_files
