# -*- coding: utf-8 -*-
# Copyright 2011 Machinalis: http://www.machinalis.com/
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


__author__ = "Matias Herranz (matiasherranz@gmail.com)"
__version__ = "0.1"


import os

LINE_TO_ADD_TO_FORMS = '{% csrf_token %}\n'


# Base directory path from where to walk template directories.
# Set the paths according to your project.
CURRENT_PATH = os.path.realpath(".")
BASE_PATH = CURRENT_PATH + '/trunk/'
print BASE_PATH

def csrf_form_adder():
    for root, dirs, files in os.walk(BASE_PATH):
        for name in files:
            if ('.svn' not in root) and name.endswith('.html'):
                print '==> root: ', root

                print 'root: ', root
                print 'name: ', name

                make_replacements(root, name)


def make_replacements(root, name):
    filepath = os.path.join(root, name)

    f = open(filepath, 'r')
    lines = f.readlines()
    f.close()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if  ('<form' in line) and (not '</' in line) and (not '"form' in line):
                               # exclude form closing   exclude form as a css classname
            new_lines.append(LINE_TO_ADD_TO_FORMS)
            print 'Added csrf token ok.\n'
    new_content = ''.join(new_lines)

    f = open(filepath, 'w')
    f.write(new_content)
    f.close()


if __name__ == '__main__':
    csrf_form_adder()
