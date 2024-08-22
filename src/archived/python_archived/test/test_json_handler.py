"""
This module contains test cases for class JSONHandler from module json_handler.
"""

from python_archived.helper.json_handler import JSONHandler

from python_archived.test.test_setup import unittest, TestCourse

class TestJSONHandler(TestCourse):
    """
    Test cases for class JSONHandler from module json_handler.
    """

    def setUp(self):
        super().setUp()
        self.path1 = ''
        self.path2 = ' '
        self.path3 = 'python/test/sample/subjects.json'
        self.path4 = 'python/test/sample/empty.json'
        self.path5 = 'python/test/sample/subjects.csv'
        self.path6 = 'python/test/wrongsample/subjects.json'
        self.url1 = ''
        self.url2 = ' '
        self.url3 = 'https://app.coursedog.com/api/v1/cm/umn_umntc_peoplesoft/courses/?limit=2'
        self.url4 = 'https://app.coursedog.com/api/v1/cm/umn_umntc_peoplesoft/?limit=2'

    #############################################################################
    def test_get_from_path(self):
        """
        Test method get_from_path of class JSONHandler.
        """

        self.assertRaises(
            FileNotFoundError,
            JSONHandler.get_from_path, self.path1
        )
        self.assertRaises(
            FileNotFoundError,
            JSONHandler.get_from_path, self.path2
        )
        self.assertRaises(
            FileNotFoundError,
            JSONHandler.get_from_path, self.path6
        )
        self.assertRaises(
            FileExistsError,
            JSONHandler.get_from_path, self.path3
        )

    #############################################################################
    def test_get_from_url(self):
        """
        Test method get_from_url of class JSONHandler.
        """

        # TODO
        pass

    #############################################################################
    def test_write_to_path(self):
        """
        Test method write_to_path of class JSONHandler.
        """

        # TODO
        pass
