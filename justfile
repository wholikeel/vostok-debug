set shell := ["powershell", "-c"]

python-venv := ".venv"
# need to fix for unix systems
scons := python-venv / "Scripts/scons.exe"

# windows | linux | macos
scons-platform := "windows" 

requirements-file := "./requirements.txt"
godot := "godot"

alias b := build


deps:
    python -m venv {{python-venv}}
    {{python-venv}}/Scripts/pip.exe install -r {{requirements-file}}
    git submodule update --init

libs:
    {{python-venv}}/Scripts/activate
    {{godot}} --dump-extension-api
    cd godot-cpp
    scons platform={{scons-platform}} custom_api_file="../extension_api.json"


dev:
    {{python-venv}}/Scripts/activate

build:
    {{python-venv}}/Scripts/activate
    scons platform={{scons-platform}}


build-release:
    {{python-venv}}/Scripts/activate
    scons platform={{scons-platform}} target=template_release


clean:
    rm native-src/*.obj
    rm native-src/*.import
    Remove-Item scripts/__pycache__ -Recurse -Force -Confirm:$false