#!/usr/bin/env python
import os
import sys

import importlib.util
import types
from typing import Final, TYPE_CHECKING


def import_from_path(module_name: str, file_path: str) -> types.ModuleType:
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


Gdextension = import_from_path("gdextension", f"{os.getcwd()}/scripts/gdextension.py").Gdextension
load_mod_txt = import_from_path("modconfig", f"{os.getcwd()}/scripts/modconfig.py").load


if TYPE_CHECKING:
    from SCons.Environment import Glob


modtxt = load_mod_txt("mod.txt")

NATIVE_LIB_NAME: Final[str] = "libvostokdebug"
NATIVE_SOURCE_DIR: Final[str] = "native-src"
PLUGIN_SOURCE_DIR: Final[str] = f"mods/{modtxt["mod"]["id"]}"


gdextension = Gdextension(
    entry_symbol = "example_library_init",
    compatibility_minimum = "4.1",
    reloadable = "true",
)


env = SConscript("godot-cpp/SConstruct")


# For reference:
# - CCFLAGS are compilation flags shared between C and C++
# - CFLAGS are for C-specific compilation flags
# - CXXFLAGS are for C++-specific compilation flags
# - CPPFLAGS are for pre-processor flags
# - CPPDEFINES are for pre-processor defines
# - LINKFLAGS are for linking flags

# tweak this if you want to use different folders, or more folders, to store your source code in.
env.Append(CPPPATH=[f"{NATIVE_SOURCE_DIR}/"])
sources = Glob(f"{NATIVE_SOURCE_DIR}/*.cc")


if env["platform"] == "macos":
    library = env.SharedLibrary(
        f"{PLUGIN_SOURCE_DIR}/bin/{NATIVE_LIB_NAME}.{env["platform"]}.{env["target"]}.framework/{NATIVE_LIB_NAME}.{env["platform"]}.{env["target"]}",
        source=sources,
    )
elif env["platform"] == "ios":
    if env["ios_simulator"]:
        library = env.StaticLibrary(
            f"{PLUGIN_SOURCE_DIR}/bin/{NATIVE_LIB_NAME}.{env["platform"]}.{env["target"]}.simulator.a",
            source=sources,
        )
    else:
        library = env.StaticLibrary(
            f"{PLUGIN_SOURCE_DIR}/bin/{NATIVE_LIB_NAME}.{env["platform"]}.{env["target"]}.a",
            source=sources,
        )
else:
    out_path = f"{PLUGIN_SOURCE_DIR}/bin/{NATIVE_LIB_NAME}{env["suffix"]}{env["SHLIBSUFFIX"]}"

    library = env.SharedLibrary(out_path, source=sources,)

    # for arch in ("x86_32", "x86_64"):
    gdextension.add_library(
        env["platform"],
        env["target"].removeprefix("template_"),
        "x86_64",
        out_path
    )


env.NoCache(library)
Default(library)


gdextension_path = os.path.join(os.getcwd(), PLUGIN_SOURCE_DIR, "bin",)

if not os.path.exists(gdextension_path):
    os.makedirs(gdextension_path)

gdextension.write(os.path.join(gdextension_path, "gdexample.gdextension"))






