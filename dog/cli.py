"""dog: fetch missing man pages

usage: dog [--version] [--help]

options:
-v, --version       Print the version and exit
-h, --help          Print this help
"""

from docopt import docopt


def main():
    arguments = docopt(__doc__, version='dog 0.0.1')
    print "What's up dog?"
    print arguments
    return 0

if __name__ == "__main__":
    exit(main())
