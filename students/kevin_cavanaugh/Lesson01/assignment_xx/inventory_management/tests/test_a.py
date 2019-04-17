"""

I am test_a.py in students/kevin_cavanaugh/lessons/lesson01/assignment/tests
run me from  students/kevin_cavanaugh/lessons/lesson99/assignment/src


Linting:
pytest --pylint

Test and coverage:
python -m pytest -vv --cov=.  ../tests/


Note my import conventions. Verbose maybe, but it makes it
COMPLETELY CLEAR where the imported functionality comes from

"""

from a import main
from b import print_mess
from c import show_mess


def test_a():
    '''
    tests a
    :return:
    '''
    main()
    assert 1


def test_b():
    '''
    tests b
    :return:
    '''
    print_mess("B")
    assert 2


def test_c():
    '''
    tests c
    :return:
    '''
    show_mess("C")
    assert 3
