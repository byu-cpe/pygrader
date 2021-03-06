#!/usr/bin/python3

import unittest
import pathlib
import sys
import filecmp


ROOT_PATH = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_PATH))

from pygrader import Grader, CodeSource

TEST_PATH = ROOT_PATH / "test"
TEST_RESOURCES_PATH = TEST_PATH / "resources"


class TestGithub(unittest.TestCase):
    def test_me(self):
        grader = Grader(
            name="test_github",
            lab_name="lab1",
            points=10,
            work_path=TEST_PATH / "temp",
            code_source=CodeSource.GITHUB,
            grades_csv_path=TEST_RESOURCES_PATH / "grades1.csv",
            grades_col_names="lab1",
            github_csv_path=TEST_RESOURCES_PATH / "github.csv",
            github_csv_col_name="github_url",
            github_tag="master",
            build_only=True,
        )

        grader.run()


class TestLearningSuite(unittest.TestCase):
    def test_me(self):
        grades_path = TEST_RESOURCES_PATH / "grades2.csv"
        grades_path_golden = TEST_RESOURCES_PATH / "grades2_golden.csv"
        grader = Grader(
            name="test_learningsuite",
            lab_name="lab1",
            points=(10,),
            work_path=TEST_PATH / "temp",
            code_source=CodeSource.LEARNING_SUITE,
            grades_csv_path=grades_path,
            grades_col_names=("lab1",),
            learning_suite_submissions_zip_path=TEST_RESOURCES_PATH / "submissions.zip",
            run_on_milestone=self.runner,
        )

        grader.run()

        self.assertTrue(filecmp.cmp(grades_path, grades_path_golden))

    def runner(self, **kw):
        print("Modified time:", kw["modified_time"])

        self.assertIn("section", kw)
        self.assertIn("homework_id", kw)
        return 3
