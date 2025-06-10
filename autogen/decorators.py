# autogen/decorators.py

from typing import List, Tuple, Dict, Any
import inspect

# Global registry
MODULE_REGISTRY: Dict[str, Dict[str, Any]] = {}

def c_module(name: str,
             language: str = "c",
             header: str = None,
             category: str = None,
             dependencies: List[str] = None,
             misra_version: str = "C:2012"):
    header = header or f"{name}.h"
    dependencies = dependencies or []
    def wrap(cls):
        functions = []
        # find all methods decorated with _c_fn_spec
        for _, member in inspect.getmembers(cls, inspect.isfunction):
            if hasattr(member, "_c_fn_spec"):
                spec = member._c_fn_spec.copy()
                functions.append(spec)
        spec = {
            "name": name,
            "header": header,
            "language": language,
            "category": category,
            "dependencies": dependencies,
            "misra_version": misra_version,
            "functions": functions
        }
        MODULE_REGISTRY[name] = spec
        cls._spec = spec
        return cls
    return wrap

def c_function(name: str,
               inputs: List[Tuple[str,str]],
               outputs: List[Tuple[str,str]] = None,
               description: str = ""):
    outputs = outputs or []
    def wrap(fn):
        fn._c_fn_spec = {
            "name": name,
            "inputs": inputs,
            "outputs": outputs,
            "description": description
        }
        return fn
    return wrap
