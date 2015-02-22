import argparse
import os
import logging


class BookCreator:
    def __init__(self, directory):
        self.directory = directory

    def create(self):
        pass

    def build(self):
        pass


def create_parser():
    help = {
        'directory': 'Use directory where files are stored.'
    }
    parser = argparse.ArgumentParser(description='Create mobi file.')
    parser.add_argument('directory', help=help['directory'])
    return parser


def check_dir(path):
    return os.path.isdir(path)


def main():
    parser = create_parser()
    args = parser.parse_args()
    if check_dir(args.directory):
        logging.info('Directory found.')
        bc = BookCreator(args.directory)
        bc.create()
        bc.build()
    else:
        logging.warning('Directory not exists.')


if __name__ == '__main__':
    main()