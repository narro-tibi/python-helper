""" Scripts regarding file generation. """

import os


def next_nonexistent(file):
    """create and increment new file next to sibling"""
    new_file = file
    root, ext = os.path.splitext(file)
    i = 0
    while os.path.exists(new_file):
        i += 1
        new_file = '%s_%i%s' % (root, i, ext)
    return new_file
