extends Node


func _ready() -> void:
    pass



func load_overrides(override_dir: String = "res://mods/vostok-debug/overrides") -> void:
    var dir: DirAccess = DirAccess.open(override_dir)

    if dir == null:
        printerr("Could not open: " + override_dir)
        return

    for file: String in dir.get_files():
        var script_path: String = dir.get_current_dir() + "/" + file
        var script: Script = load(script_path)
        script.reload()
        var parent = script.get_base_script()
        script.take_over_path(parent.resource_path)
        print("Overriding '" + parent.resource_path + "' with '" + script_path + "'.")

