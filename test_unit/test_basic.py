import os
from main import main
from unittest import mock

@mock.patch.dict(os.environ, {
    "INPUT_ARGS": "-l python test_data/basic/main.py",
    })
def test_basic():
    main()