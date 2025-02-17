import configparser
from typing import TypedDict


class ModConfig(TypedDict):
    name: str
    id: str
    version: str
    author: str
    url: str

class UpdatesConfig(TypedDict):
    modworkshop: int
    

class Config(TypedDict):
    mod: ModConfig
    autoload: dict[str, str]
    updates: UpdatesConfig


def load(path: str) -> Config:
    parser = configparser.ConfigParser()
    parser.read(path)
    # turn nested ConfigParser sections into dicts and remove quotes.
    return {k: {k2: v2.replace("\"", "") for k2, v2 in dict(v).items()} for k, v in dict(parser).items() if k != "DEFAULT"}



__all__ = [ "load" ]
