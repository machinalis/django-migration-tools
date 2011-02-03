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

file1 = open('./orig.txt', 'r')
file2 = open('./dest.txt', 'r')

lines1 = [line[:-1] for line in file1]
lines2 = [line[:-1] for line in file2]

for i in range(0, 78):
    print 'Renaming: %s -> %s' % (lines1[i], lines2[i])
    os.rename(lines1[i], lines2[i])
