import argparse


def parse(args):
    pass


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
