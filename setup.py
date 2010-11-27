from distutils.core import setup
import py2exe

##setup(console=['googlizer.py'])

setup(
    windows = [
        {
            "script": "googlizer.py",
            "icon_resources": [(1, "googlizer.ico")]
        }
    ],
)