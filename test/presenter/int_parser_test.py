from unittest.case import TestCase

from presenter.int_parser import IntParser


__author__ = 'novy'


class IntParserTest(TestCase):
    def setUp(self):
        super(IntParserTest, self).setUp()
        self.object_under_test = IntParser()

    def test_should_return_none_given_none(self):
        self.assertIsNone(self.object_under_test.parse(None))

    def test_should_return_none_given_unparsabble_string(self):
        self.assertIsNone(self.object_under_test.parse("2.0"))
        self.assertIsNone(self.object_under_test.parse("dummy string"))

    def test_should_return_proper_int_value_given_parsable_string(self):
        parsable_int_string = "666"
        self.assertEqual(self.object_under_test.parse(parsable_int_string), 666)