#!/usr/bin/env python

import os
import shutil
import sys


def which(name, flags=os.X_OK):  # Taken from pynacl's setup.py
    result = []
    exts = filter(None, os.environ.get("PATHEXT", "").split(os.pathsep))
    path = os.environ.get("PATH", None)
    if path is None:
        return []
    for p in os.environ.get("PATH", "").split(os.pathsep):
        p = os.path.join(p, name)
        if os.access(p, flags):
            result.append(p)
        for e in exts:
            pext = p + e
            if os.access(pext, flags):
                result.append(pext)

    return result


if __name__ == '__main__':
    if sys.argv[1:]:
        print('shutil: ', shutil.which(sys.argv[1]))
        print('which: ', which(sys.argv[1]))
    else:
        print('usage: find_executable.py <progname>')
