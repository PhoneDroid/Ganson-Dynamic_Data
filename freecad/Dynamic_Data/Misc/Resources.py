# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Dynamic Data addon.


import freecad.Dynamic_Data as module
from importlib import resources


icons = resources.files(module) / 'Resources/icons'


def asIcon ( name : str ):

    file = name + '.svg'

    icon = icons / file

    with resources.as_file(icon) as path:
        return str( path )