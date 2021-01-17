import cx_Freeze

executables = [cx_Freeze.Executable("project/main.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["project/data/fon1.png"], ['project/data/fruit.png']:
                               ['project/data/gameover.png'], ['project/data/kor.png']:
                               ['project/data/muzlo.wav']}},
    executables=executables

)
