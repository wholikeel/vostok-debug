import configparser



class Gdextension:

    def __init__(self, entry_symbol: str, compatibility_minimum: str, reloadable: str):
        self._entry_symbol = entry_symbol
        self._compatibility_minimum = compatibility_minimum
        self._reloadable = reloadable

        self._libraries: dict[str, str] = {}
        self._dependencies: dict[str, str] = {}

    def add_library(self, platform: str, target: str, arch: str | None, library_path: str) -> None:
        variant = ".".join(filter(None, (platform, target, arch)))
        self._libraries[variant] = library_path

    def add_dependency(self, platform: str, target: str, arch: str | None, dependency_path: str) -> None:
        variant = ".".join(filter(None, (platform, target, arch)))
        self._dependencies[variant] = dependency_path


    def write(self, path: str) -> None:
        
        config = self._build()

        with open(path, "w") as file:
            config.write(file)


    def _build(self) -> configparser.ConfigParser:
        config = configparser.ConfigParser()
        config["configuration"] = {
            "entry_symbol": self._entry_symbol,
            "compatibility_minimum": self._compatibility_minimum,
            "reloadable": self._reloadable
        }
        config["libraries"] = self._libraries
        config["dependencies"] = self._dependencies

        return config


__all__ = [ "Gdextension" ]