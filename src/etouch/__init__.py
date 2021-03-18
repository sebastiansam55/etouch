#!/usr/bin/python3

import os
import json
import argparse
from pathlib import Path


def load_templates():
    try:
        with open(Path('~/.config/etouch.json').expanduser()) as f:
            data = json.loads(f.read())

            # print(data)
            return data
    except:
        print("Error reading config file (~/.config/etouch.json), using sensible defaults")
        return {".py":"#!/usr/bin/python3",".sh":"#!/bin/bash"}

def main():
    parser = argparse.ArgumentParser(description="Enhanched Touch Tool")
    parser.add_argument('FILE', action="store", nargs='*', help="Filename to create")
    args = parser.parse_args()

    # print(args)

    wd = Path(os.getcwd())

    templates = load_templates()

    for file in args.FILE:
        newfile = wd.joinpath(file)

        if newfile.exists():
            print("File '{}' already exists".format(file))
        else:
            # print("Creating new file")
            newfile.touch()
            suf = newfile.suffix
            if suf in templates:
                # print("adding shebang")
                with open(newfile, 'w') as f:
                    f.write(templates[suf])
            else:
                print("no template found creating empty file")




