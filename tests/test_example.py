# Copyright (C) 2024 twyleg
import pytest

import logging
from pathlib import Path


#
# General naming convention for unit tests:
#               test_INITIALSTATE_ACTION_EXPECTATION
#


FILE_DIR = Path(__file__).parent


class TestExample:
    def test_InitialStatew_Action_Expectation(self, caplog, tmp_path):
        logging.info("Tmp path: %s", tmp_path)
        assert 1 == 1
