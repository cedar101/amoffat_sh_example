import sys
from pathlib import Path

# from .biz.common import version
import thinq_parser.biz.common as common

def parse(line):
    return f'version {common.version} result: {line}'

if __name__ == "__main__":
    parse()