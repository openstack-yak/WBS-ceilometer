#!/usr/bin/env python
from os import path
import sys

import json
import yaml

if len(sys.argv) > 1:
    print("usage:\n\t{} < your_json_file > your_yaml_file".format(
            path.basename(sys.argv[0])))
    sys.exit(1)

yaml.dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)

