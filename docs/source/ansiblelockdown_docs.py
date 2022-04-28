#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2016, Rackspace US, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Build documentation from Benchmark files and Ansible tasks."""
from __future__ import print_function, unicode_literals
import os
import re
import glob

from collections import defaultdict

import jinja2
import yaml

try:
    from elementtree.ElementTree import parse, XMLParser, fromstring
except ImportError:
    from xml.etree.ElementTree import parse, XMLParser, fromstring

DOC_SOURCE_DIR = "{0}/..".format(os.path.dirname(os.path.abspath(__file__)))


def split_at_linelen(line, length):
    """Split a line at specific length for code blocks or 
       other formatted RST sections.
    """
    # Get number of splits we should have in line
    i = int(len(line)/length)
    p = 0

    while i > 0:
        p = p+length
        # If position in string is not a space
        # walk backwards until we hit a space
        while line[p] != ' ':
            p -= 1

        # Split the line
        line = line[:p] + '\n' + line[p+1:]
        i -= 1

    return line


def add_monospace(text):
    """Add monospace formatting to RST."""
    paragraphs = text.split('\n\n')

    for key, value in enumerate(paragraphs):

        # Replace all quotes "" with backticks `` for monospacing
        paragraphs[key] = re.sub(u'\u201c(.*?)\u201d',
                                 r'``\1``',
                                 value)

        # If our paragraph starts with a " and it wasn't handled
        # by the backtick substitution it probably means it
        # does not end with a " and is a special block of text
        if value.startswith('"'):
            paragraphs[key] = '.. code-block:: text\n\n    ' + '\n    '.join(split_at_linelen(value.lstrip('"'), 66).split('\n'))

            i = key+1

            # Loop through all the following paragraphs to format
            # and look for the last one
            while i < len(paragraphs):
                last_line = paragraphs[i].endswith('"')
                # Indent this paragraph
                paragraphs[i] = '    ' + '\n    '.join(split_at_linelen(paragraphs[i].rstrip('"'), 66).split('\n'))

                i += 1
                # Break the loop if we found the last paragraph
                if last_line:
                    break

        # If our paragraph ends with a colon and the next line isn't a special
        # note, let's make sure the next paragraph is monospaced.
        # if value.endswith(":"):

        #     if paragraphs[key + 1].startswith('Note:'):

        #         # Indent the paragraph AFTER the note.
        #         paragraphs[key + 2] = '::\n\n    ' + '\n    '.join(
        #             paragraphs[key + 2].split('\n')
        #         )

        #     else:
        #         # Ensure the paragraph ends with double colon (::).
        #         # paragraphs[key] = re.sub(r':$', '::', value)

        #         # Indent the next paragraph.
        #         paragraphs[key + 1] = '::\n\n    ' + '\n    '.join(
        #             paragraphs[key + 1].split('\n')
        #         )

        # If we found a note in the description, let's format it like a note.
        if value.startswith('Note:'):
            paragraphs[key] = ".. note::\n\n    {0}".format(value[6:])

        # If we have a line that starts with a pound sign, this probably needs
        # to be pre-formatted as well.
        if value.startswith('#'):
            paragraphs[key] = '::\n\n    ' + '\n    '.join(value.split('\n'))

        # If there's a command on a line by itself, we probably need to merge
        # it with the next line. The STIG has terrible formatting in some
        # places.
        monospace_strings = ['grep', 'more']
        if (
            key + 1 < len(paragraphs) and
            any(x in value for x in monospace_strings) and
            '\n' not in value and
            not paragraphs[key + 1].startswith('Password')
        ):
            value = "{0}\n{1}".format(
                value,
                '\n    '.join(paragraphs[key + 1].split('\n'))
            )
            del(paragraphs[key + 1])

    return '\n\n'.join(paragraphs)


def get_deployer_notes(path, stig_id):
    """Read deployer notes based on the Benchmark ID."""
    filename = "{0}/{1}.rst".format(path, stig_id)

    # Does this deployer note exist?
    if not os.path.isfile(filename):
        return 'Nothing to report\n'

    # Read the note and parse it with YAML
    with open(filename, 'r') as f:
        rst_file = f.read()

    return rst_file

