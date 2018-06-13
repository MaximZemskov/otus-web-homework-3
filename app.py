import argparse
import os

from repo.pull import clone_repository
from repo.dirs import create_dir_for_cloned_repo, delete_dir
from filestat.stat import get_top_verbs_in_path

BASE_DIR = os.getcwd()


def parse(args):
    path_to_clone = create_dir_for_cloned_repo(BASE_DIR)
    clone_repository(args.r, path_to_clone)
    print(get_top_verbs_in_path(path_to_clone))
    delete_dir(path_to_clone)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '-repository', help='Repository to clone .git')
    parser.add_argument('--p', '--part_speech', nargs='?', default='v',
                        help='v - for verbs, n - for nouns')
    parser.add_argument('--t', '--type', nargs='?', default='function',
                        help='functions - for functions, variables - for '
                             'variables')
    parser.add_argument('--ot', '--output_type', nargs='?',
                        default='json', help='Type of output. json or csv.')
    args = parser.parse_args()
    print(args)
    if args.r:
        parse(args)
    else:
        print('No git repository passed.')
