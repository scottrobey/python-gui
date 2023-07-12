
Primer:
https://towardsdatascience.com/5-python-gui-frameworks-to-create-desktop-web-and-even-mobile-apps-c25f1bcfb561

GUI Frameworks for Python
- Tkinter - the only GUI framework built into Python https://realpython.com/python-gui-tkinter/
  - Modern version - https://github.com/TomSchimansky/CustomTkinter
  - Themed Tkinkter - https://docs.python.org/3/library/tkinter.ttk.html
  - Tkinter course - https://python-course.eu/tkinter/
  - Tkinter reference - https://docs.python.org/3/library/tk.html

- Kivy - https://kivy.org/doc/stable/guide/basic.html
        https://github.com/kivy/kivy-sdk-packager/tree/master/osx
- PyQt framework: https://www.riverbankcomputing.com/software/pyqt/
- PySimpleGUI - https://realpython.com/pysimplegui-python/ - wrapper around other GUi frameworks?
- PySide2 - the official Python module from the Qt for Python project, which provides access to the complete Qt 5.12+ framework.
- EasyGui - https://easygui.readthedocs.io/en/master/

Modern looking GUIs in Python?
https://www.reddit.com/r/learnpython/comments/fmyr9j/are_there_any_modern_looking_guis_for_python/


Project

To implement a GUI for transferring files from one computer to another, using [Magic Wormhole](https://github.com/magic-wormhole/magic-wormhole)

Magic Wormhole is a command line utility, the GUI will wrap the commands for either sending or receiving files. 
Later, may consider supporting other utilities for transferring files, like using Dropbox or maybe SCP, etc.

Features:
* Add support for sending and receiving - text message and directories
* Logging or debug window - proper file menu
* Add details about file being sent / received like size, etc.
* Config settings - location to wormhole binary, etc.
* Progress bar for file transfer - use wormhole --dump-timing to get timing data?
* Enhanced Error Checking
* Links to open files? like what? link to wormhole itself
* History
* Drag and drop files to send
* Support for multiple files
* Modern look


Then discovered there are already a few GUI utilities that wrap Wormhole:
*  https://gitlab.gnome.org/World/warp
*  https://gitlab.com/lukas-heiligenbrunner/wormhole