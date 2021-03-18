# etouch

Basic template tool for the command line


Operates like the basic GNU coreutils tool `touch`, 
it checks the extension provided against a json file in the `~/.config/etouch.json` 
each entry should be in the format of:

```
{
    ".py":"#!/usr/bin/python3",
    ".sh":"#!/bin/bash"
}
```

If the suffix (file extension) of the file to be created is an exact match 
then the created file will contain the matching contents.

If there is not a match the script will make an empty file like expected of regular `touch`

## Installation

```
git clone https://github.com/sebastiansam55/etouch
python3 setup.py install --user
```

Shouldn't require

