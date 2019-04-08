# Tests

---

### Integration Test w/ Coverage

From the assignment directory in lesson01, run:

`python3 -m coverage run -m unittest tests/integration_test.py`
Contains 1 test that adds 3 items [Furniture, Appliance, Item] and checks
the contents of the values with option 2 of the menu and quits after.

`test_main (tests.integration_test.ModuleTests)`

### Unit Tests w/ Coverage

From the assignment directory in lesson01, run:

`python3 -m coverage run -m unittest tests/unit_tests.py`
Runs 15 tests that go through each available method in class files present in
the `./inventory_management` directory.

```bash
test_dict (tests.unit_tests.ElectricAppliancesTests)
test_init (tests.unit_tests.ElectricAppliancesTests)
test_dict (tests.unit_tests.FurnitureTests)
test_init (tests.unit_tests.FurnitureTests)
test_dict (tests.unit_tests.InventoryTests)
test_init (tests.unit_tests.InventoryTests)
test_add_item_furniture (tests.unit_tests.MainTests)
test_add_item_reg (tests.unit_tests.MainTests)
test_exit (tests.unit_tests.MainTests)
test_get_info (tests.unit_tests.MainTests)
test_get_latest_price (tests.unit_tests.MainTests)
test_get_price (tests.unit_tests.MainTests)
test_main_menu_add (tests.unit_tests.MainTests)
test_main_menu_get (tests.unit_tests.MainTests)
test_main_menu_quit (tests.unit_tests.MainTests)
```

### Pylint

From the assignment directory in lesson01, run:

`python3 -m pylint --rcfile pylintrc inventory_management/`

```bash
Report
======
99 statements analysed.

Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |6      |6          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |3      |3          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|method   |6      |6          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|function |6      |6          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+

Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |137    |61.16 |137      |=          |
+----------+-------+------+---------+-----------+
|docstring |45     |20.09 |45       |=          |
+----------+-------+------+---------+-----------+
|comment   |6      |2.68  |6        |=          |
+----------+-------+------+---------+-----------+
|empty     |36     |16.07 |36       |=          |
+----------+-------+------+---------+-----------+

Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |=          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+

Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |0      |0        |=          |
+-----------+-------+---------+-----------+
|refactor   |0      |0        |=          |
+-----------+-------+---------+-----------+
|warning    |0      |0        |=          |
+-----------+-------+---------+-----------+
|error      |0      |0        |=          |
+-----------+-------+---------+-----------+

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

## Directory Structure

```bash
.
├── README.md
├── __pycache__
│   └── unit_tests.cpython-37.pyc
├── inventory_management
│   ├── ElectricAppliancesClass.py
│   ├── FurnitureClass.py
│   ├── InventoryClass.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── ElectricAppliancesClass.cpython-37.pyc
│   │   ├── FurnitureClass.cpython-37.pyc
│   │   ├── InventoryClass.cpython-37.pyc
│   │   ├── __init__.cpython-37.pyc
│   │   ├── integration_test.cpython-37.pyc
│   │   ├── main.cpython-37.pyc
│   │   ├── market_prices.cpython-37.pyc
│   │   └── unit_tests.cpython-37.pyc
│   ├── main.py
│   └── market_prices.py
├── pylintrc
└── tests
    ├── README.md
    ├── __pycache__
    │   ├── __init__.cpython-37.pyc
    │   ├── integration_test.cpython-37-PYTEST.pyc
    │   ├── integration_test.cpython-37.pyc
    │   └── unit_tests.cpython-37.pyc
    ├── integration_test.py
    └── unit_tests.py
```