from yaml import safe_load

# Loads the contents of config.yml as a dict named 'configuration' and closes the file
with open('config.yml') as handle: configuration = safe_load(handle)

# A configuration object to easily access the contents of config.yml.
## eg: config.username or specify a default with config.get('username', ['default_value'])  None will be used if no default specified
### Top-level keys can be accessed with: str(config) or config.__str__() or config.keys()
class Configuration():
    def __init__(self, params=None):
        self.params = params

    def __str__(self):
        return str(list(configuration.keys()))

    def __getattr__(self, property):
        if property in configuration:
            return configuration[property]
        else: raise KeyError(property)

    def get(self, property, default=None):
        try:
            return self.__getattr__(property)
        except KeyError:
            return default

    def keys(self):
        return self.__str__()

config = Configuration()  # Save the Configuration() object as config for easy access from external scripts
