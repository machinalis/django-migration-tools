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
import re


# Base directory path from where to walk template directories.
CURRENT_PATH = os.path.realpath(".")
TEMPLATES_PATH = CURRENT_PATH + '/trunk/expo/_templates'
print TEMPLATES_PATH

def sanitizer():
    for root, dirs, files in os.walk(TEMPLATES_PATH):
        for name in files:
            if ('.svn' not in root) and name.endswith('.html'):
                print '==> root: ', root

                print 'root: ', root
                print 'name: ', name
                print''

                make_replacements(root, name)

#            else:
#                print '==> Directory excluded: ', root
#                print''


def make_replacements(root, name):
    filepath = os.path.join(root, name)

    data = open(filepath).read()

    o = open(filepath, "w")
    o.write(re.sub("http://www.laexpo.com.ar/", "{{ SITE_URL }}/", data))
    o.close()


if __name__ == '__main__':
    sanitizer()
