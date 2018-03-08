import dis, marshal, sys, ctypes

# Header size changed in 3.3. It might change again, but as of this writing, it
# hasn't.
header_size = 12 if sys.version_info >= (3, 3) else 8


def load_code_object_from_pyc(pycfile):
    with open(pycfile, "rb") as f:
        magic_and_timestamp = f.read(header_size)  # first 8 or 12 bytes are metadata
        code = marshal.load(f)
    return code


def get_object_by_id(address):
    return ctypes.cast(address, ctypes.py_object).value


def print_code_names(code):
    from pprint import pprint
    pprint({
        'co_consts': code.co_consts,
        'co_names': code.co_names,
        'co_varnames': code.co_varnames,
        'co_freevars': code.co_freevars,
        'co_cellvars': code.co_cellvars
    })