import os
import sys
from importlib import import_module
from importlib.util import find_spec


class ModuleLoader:
    def load(self, module_name: str, prefix: str, class_name=""):
        module_name = "%s.%s" % (prefix, module_name)
        if not find_spec(module_name):
            print('%s: No such module.' % module_name, file=sys.stderr)
            exit(1)
        module = import_module(module_name)

        if len(class_name) == 0:
            class_name = module_name.rsplit('.', 1)[-1]

        try:
            return getattr(module, class_name)
        except AttributeError:
            print('%s: No such class.' % class_name, file=sys.stderr)
            exit(1)

    def loadFromDir(self, file, path: str):
        # we have filename = /path/filename.py, we
        # first we remove path
        # os.sep returns correct "/" per os
        class_name = file.rsplit(os.sep, 1)[-1]
        # we have class_name = filename.py
        # and now we remove extension
        class_name = class_name[:-3]
        # we have class_name = filename

        return self.load(class_name, path)
