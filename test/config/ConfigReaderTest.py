"""
This class contains tests for ConfigReader class.
"""
from unittest import TestCase
from unittest import main

from config.ConfigReader import ConfigReader


class ConfigReaderTest(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.config = ConfigReader('config.yml')

    def test_read_file(self):
        self.assertFalse(hasattr(self.config, 'configuration'))
        self.config.get_property([])
        self.assertTrue(hasattr(self.config, 'configuration'))

    def test_get_property_with_empty_path(self):
        result = self.config.get_property([])
        self.assertIsInstance(result, dict)
        self.assertSetEqual(set(result.keys()), {'option1', 'option2'})

    def test_get_property_with_one_element_path(self):
        result = self.config.get_property(['option2'])
        self.assertEqual(result, 'option2')

    def test_get_property_with_two_elements_path(self):
        result = self.config.get_property(['option1', 'option1.1'])
        self.assertEqual(result, 'option1.1')

    def test_get_property_with_list_returned(self):
        result = self.config.get_property(['option1', 'option1.2'])
        self.assertIsInstance(result, list)
        self.assertSetEqual(set(result), {'option1.2.1', 'option1.2.2'})

    def test_get_property_with_wrong_path(self):
        result = self.config.get_property(['option3'])
        self.assertIsNone(result)


if __name__ == '__main__':
    main()
