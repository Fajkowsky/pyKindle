import argparse
import os
import logging
import re

# SETTINGS
BUILD_DIR = 'build/'


# UTILS
def create_dir(dir=BUILD_DIR):
    if not os.path.exists(dir):
        os.makedirs(dir)


def delete_dir(dir=BUILD_DIR):
    if os.path.exists(dir):
        os.rmdir(dir)


def check_dir(path):
    return os.path.isdir(path)


# MAIN PACKAGE
class BookCreator:
    def __init__(self, directory):
        self.directory = directory
        self.files = self.search_files()

    def search_files(self):
        return sorted([
            file for file in os.listdir(self.directory)
            if re.match(r'\d+.txt', file)
        ])

    def create(self):
        create_dir()


    def build(self):
        delete_dir()


# RUN
def create_parser():
    helpers = {
        'directory': 'Use directory where files are stored.'
    }
    parser = argparse.ArgumentParser(description='Create mobi file.')
    parser.add_argument('directory', help=helpers['directory'])
    return parser


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