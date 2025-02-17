import configparser



class QuotedConfigParser(configparser.ConfigParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set(self, section, option, value):
        super().set(section, option, f'"{value}"' if not value.isnumeric() and not value in ["true", "false"] else value)


class Gdextension:

    def __init__(self, entry_symbol: str, compatibility_minimum: str, reloadable: str):

        self._libraries: dict[str, str] = {}
        self._dependencies: dict[str, str] = {}

        self._config = QuotedConfigParser()
        self._config.add_section("configuration")
        self._config.add_section("libraries")
        self._config.add_section("dependencies")
        self._config.set("configuration", "entry_symbol", entry_symbol)
        self._config.set("configuration", "compatibility_minimum", compatibility_minimum)
        self._config.set("configuration", "reloadable", reloadable)

    def add_library(self, platform: str, target: str, arch: str | None, library_path: str) -> None:
        variant = ".".join(filter(None, (platform, target, arch)))
        self._config.set("libraries", variant, f"res://{library_path}")

    def add_dependency(self, platform: str, target: str, arch: str | None, dependency_path: str) -> None:
        variant = ".".join(filter(None, (platform, target, arch)))
        self._config.set("dependencies", variant, f"res://{dependency_path}")


    def write(self, path: str) -> None:
        
        with open(path, "w") as file:
            self._config.write(file)



__all__ = [ "Gdextension" ]