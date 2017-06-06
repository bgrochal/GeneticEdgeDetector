"""
This class provides broker-interface for reading configuration file.
"""
import yaml


class ConfigReader(dict):
    def __init__(self, config_file_path, **kwargs):
        self.configuration = self.__read_file(config_file_path)
        super().__init__(**kwargs)

    @staticmethod
    def __read_file(config_file_path):
        with open(config_file_path) as yamlfile:
            return yaml.load(yamlfile)

    def __getitem__(self, key):
        return self.configuration.get(key)
