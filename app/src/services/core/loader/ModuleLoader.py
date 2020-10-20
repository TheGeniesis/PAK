import sys
from importlib import import_module
from importlib.util import find_spec


class ModuleLoader:
    def load(self, module_name: str, prefix: str):
        module_name = "%s.%s" % (prefix, module_name)
        if not find_spec(module_name):
            print('%s: No such module.' % module_name, file=sys.stderr)
            exit(1)
        module = import_module(module_name)

        class_name = module_name.rsplit('.', 1)[-1]

        try:
            return getattr(module, class_name)
        except AttributeError:
            print('%s: No such class.' % class_name, file=sys.stderr)
            exit(1)
