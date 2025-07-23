# In Python, the __main__.py file is a special file that allows a directory or
# a package to be executed as a script. When the package or directory is run
# directly, Python looks for the __main__.py file and executes it. This is
# useful for making your package executable from the command line, enabling
# the python -m command to run your package as a script.

from python_template.main import main

if __name__ == "__main__":
    main()
