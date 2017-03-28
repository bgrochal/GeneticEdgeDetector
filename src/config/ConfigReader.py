"""
This class provides broker-interface for reading configuration file.
"""
import yaml


class ConfigReader:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path

    def get_property(self, property_path):
        def read_file():
            with open(self.config_file_path) as yamlfile:
                self.configuration = yaml.load(yamlfile)

        if not hasattr(self, 'configuration'):
            read_file()

        result = self.configuration
        for key in property_path:
            if key not in result:
                return None
            result = result[key]

        return result
