I thought that Tkinkter was built into Python3 but as it turns out, I still had to install the Python3 tk module. 
Seems weird to say that this library is built-in to Python yet we have to install a package to use it, but whatevs


On mac:
```agsl
pip3 install --upgrade pip
pip3 install tk
```

Ok, so now I try to create a simple hello world GUI using Tkinter according to the online tutorial
```agsl
AttributeError: module 'tkinter' has no attribute 'Tk'

```

After some googling and reading SO posts, it appears that lots of people have had this issue and in most cases, it came 
down to a naming collision between local Python modules, and shared libraries being imported.
So of course using a local Python module named after the GUI framework I'm using (`tkinter` in this case) is going to cause issues.

Lesson Learned: Qualify our local Python modules so they don't collide with any shared libs! 

This led me to discover the Python style guide, which Python noobs should probably take a good look at: 
[PEP 8](https://peps.python.org/pep-0008/#package-and-module-names)


