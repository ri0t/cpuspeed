#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
# CPUSpeed (C)left 2008-2016, Heiko 'riot' Weinen <riot@c-base.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# And don't you point any lawyers at me!
# Send me a postcard, if you like this software.
#\n
"""

from setuptools import setup

setup(name="cpuspeed",
      version="1.0",
      description="cpuspeed displays your cpu core speed settings (using "
                  "only good old gtk2 for now)",
      author="Heiko 'riot' Weinen",
      author_email="riot@c-base.org",
      url="https://github.com/ri0t/cpuspeed",
      license="GNU General Public License v3",
      scripts=[
          'cpuspeed',
      ],
      long_description="""
cpuspeed is a tiny configurable gtk2 based applet to display the Linux
Kernel's cpu frequency setting for
each core with properly background coloured cells.

See https://github.com/ri0t/cpuspeed""",
      install_requires=[
      ]
      )
