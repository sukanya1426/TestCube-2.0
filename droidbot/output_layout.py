"""Where TestCube writes run artifacts.

Visible under -o: events/, feature_test/, feature_coverage/.
Everything else goes under .droidbot/ so the run folder stays small.
"""

import os


HIDDEN_DIRNAME = ".droidbot"
VISIBLE_TOPLEVEL = ("events", "feature_test", "feature_coverage")


def hidden_root(output_dir):
    if not output_dir:
        return None
    path = os.path.join(output_dir, HIDDEN_DIRNAME)
    os.makedirs(path, exist_ok=True)
    return path


def hidden_subdir(output_dir, name):
    root = hidden_root(output_dir)
    if not root:
        return None
    path = os.path.join(root, name)
    os.makedirs(path, exist_ok=True)
    return path


def hidden_file(output_dir, filename):
    root = hidden_root(output_dir)
    if not root:
        return None
    return os.path.join(root, filename)
