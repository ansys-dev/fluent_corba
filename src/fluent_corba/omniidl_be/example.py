# -*- python -*-
#                           Package   : omniidl
# example.py                Created on: 1999/11/26
#			    Author    : Duncan Grisby (dpg1)
#
#    Copyright (C) 1999 AT&T Laboratories Cambridge
#
#  This file is part of omniidl.
#
#  omniidl is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see http://www.gnu.org/licenses/
#
# Description:
#   
#   Example back-end which prints the names of all operations in an
#   IDL file.

"""Example IDL compiler back-end."""

from omniidl import idlast, idlvisitor, idlutil


class ExampleVisitor (idlvisitor.AstVisitor):

    def visitAST(self, node):
        for n in node.declarations():
            n.accept(self)

    def visitModule(self, node):
        for n in node.definitions():
            n.accept(self)

    def visitInterface(self, node):
        name = idlutil.ccolonName(node.scopedName())

        if node.mainFile():
            for c in node.callables():
                if isinstance(c, idlast.Operation):
                    print(name + "::" + c.identifier() + "()")

def run(tree, args):
    visitor = ExampleVisitor()
    tree.accept(visitor)
