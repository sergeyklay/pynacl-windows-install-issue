import os


def which(name, flags=os.X_OK):  # Taken from pynacl's setup.py
    result = []
    exts = filter(None, os.environ.get("PATHEXT", "").split(os.pathsep))
    path = os.environ.get("PATH", None)
    if path is None:
        return []
    for p in os.environ.get("PATH", "").split(os.pathsep):
        p = os.path.join(p, name)
        if os.access(p, flags):
            print(f'[DEBUG] found (1) {name}: {p}')
            result.append(p)
        for e in exts:
            pext = p + e
            if os.access(pext, flags):
                print(f'[DEBUG] found (2) {name}: {pext}')
                result.append(pext)

    return result


result = which('make')
print(f'result = {result}')
