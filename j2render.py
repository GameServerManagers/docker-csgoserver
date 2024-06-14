#!/usr/bin/env python

import os
import sys

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

env = Environment(
        loader=FileSystemLoader('./'),
        autoescape=select_autoescape(),
        undefined=StrictUndefined,
)

variables = dict(os.environ)

try:
    template_path = sys.argv[1]
except IndexError:
    print("ERROR: provide path to the template file", file=sys.stderr)
    sys.exit(1)

tpl = env.get_template(template_path)
print(tpl.render(**variables))
