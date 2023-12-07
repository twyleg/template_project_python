# Copyright (C) 2023 twyleg
import sys
import unittest
import tempfile
import shutil
import logging

from pathlib import Path
from template_project_utils.initializer import init_template


#
# General naming convention for unit tests:
#               test_INITIALSTATE_ACTION_EXPECTATION
#

FORMAT = "[%(asctime)s][%(levelname)s][%(name)s]: %(message)s"
FILE_DIR = Path(__file__).parent


class ExampleTestCase(unittest.TestCase):
    @classmethod
    def prepare_output_directory(cls) -> Path:
        tmp_dir = tempfile.mkdtemp()
        return Path(tmp_dir)

    def setUp(self) -> None:
        logging.basicConfig(stream=sys.stdout, format=FORMAT, level=logging.DEBUG)
        self.output_dir_path = self.prepare_output_directory()

    def test_ArrangedState_Action_Assertion(self):
        config_filepath = self.output_dir_path / "template_config.yaml"
        shutil.copyfile(FILE_DIR / "resources/test_config_0.yaml", config_filepath)

        init_template(config_filepath)



if __name__ == "__main__":
    unittest.main()
