"""
    You will submit two modules: linear.py and parallel.py
    Each module will return a list of tuples, one tuple for
     customer and one for products.
    Each tuple will contain 4 values: the number of records processed,
    the record count in the database prior to running, the record count
    after running,
    and the time taken to run the module.

"""

import pytest
import src.database as d
import src.parallel as p

@pytest.fixture
def _all_answers():
    """
    underscore required on fixture to eliminate an
    invalid redefinition warning
    from pytest pylint

    """

    d.drop_cols("products", "customers", "rentals")
    answers_linear = d.import_data('data','product.csv','customers.csv','rental.csv')
    answers_parallel = p.import_data('data','product.csv')
    d.drop_cols("product")

    return (
        {
        "processed": answers_linear[0],
        "count_prior": answers_linear[1],
        "count_new": answers_linear[2],
        "elapsed": answers_linear[3]
        },
        {
        "processed": answers_parallel[0],
        "count_prior": answers_parallel[1],
        "count_new": answers_parallel[2],
        "elapsed": answers_parallel[3]
        }
        )


def test_submission(_all_answers):
    for answer in _all_answers:
        assert type(answer["processed"]) == int
        assert type(answer["count_prior"]) == int
        assert type(answer["count_new"]) == int
        assert answer["count_prior"] + answer["processed"] == answer["count_new"]
        assert type(answer["elapsed"]) == float
        assert answer["elapsed"] > 0.0
