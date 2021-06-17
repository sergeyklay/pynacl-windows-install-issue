#!/usr/bin/env python

import os
import shutil
import sys


def find_executable(executable, path=None):
    """
    Find if 'executable' can be run.

    Looks for it in 'path' (string that lists directories separated
    by 'os.pathsep'; defaults to os.environ['PATH']). Checks for all
    executable extensions. Returns full path or None if no command
    is found.
    """
    if path is None:
        path = os.environ.get('PATH', '')

    paths = path.split(os.pathsep)
    extlist = ['']
    if os.name == 'os2':
        (base, ext) = os.path.splitext(executable)
        # executable files on OS/2 can have an arbitrary extension,
        # but .exe is automatically appended if no dot is present in
        # the name
        if not ext:
            executable = executable + '.exe'
    elif sys.platform == 'win32':
        pathext = os.environ.get('PATHEXT', '').lower()
        pathext = pathext.split(os.pathsep)
        (base, ext) = os.path.splitext(executable)
        if ext.lower() not in pathext:
            extlist = pathext
        # Windows looks for binaries in current dir first
        paths.insert(0, '')

    for ext in extlist:
        execname = executable + ext
        for p in paths:
            f = os.path.join(p, execname)
            if os.path.isfile(f):
                return f
    else:
        return None



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
        print(shutil.which(sys.argv[1]))
        print(which(sys.argv[1]))
        print(find_executable(sys.argv[1]))
    else:
        print('usage: find_executable.py <progname>')
