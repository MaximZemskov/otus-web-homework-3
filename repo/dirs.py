import os
import errno
import random
import shutil


def create_dir_for_cloned_repo(base_dir):
    tmp_dir = os.path.join(
        base_dir, 'tmp{}'.format(random.randint(1, 1000)))
    try:
        os.makedirs(tmp_dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    return tmp_dir


def delete_dir(path):
    shutil.rmtree(path, ignore_errors=True)


