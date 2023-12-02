# Copyright (C) 2023 twyleg
import unittest
import tempfile

from pathlib import Path


#
# General naming convention for unit tests:
#               test_INITIALSTATE_ACTION_EXPECTATION
#


class ExampleTestCase(unittest.TestCase):
    @classmethod
    def prepare_output_directory(cls) -> Path:
        tmp_dir = tempfile.mkdtemp()
        return Path(tmp_dir)

    def setUp(self) -> None:
        self.output_dir_path = self.prepare_output_directory()

    def test_ArrangedState_Action_Assertion(self):
        self.assertTrue(True)



if __name__ == "__main__":
    unittest.main()
