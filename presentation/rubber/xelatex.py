# This file is part of Rubber and thus covered by the GPL
# (c) Emmanuel Beffara, 2002--2006
# (c) Wouter Bolsterlee, 2009
"""
XeLaTeX support for Rubber.
"""
import sys
import rubber
from rubber import _, msg
class Module (rubber.rules.latex.Module):
    def __init__ (self, doc, dict):
        doc.vars["program"] = "xelatex"
        doc.vars["engine"] = "XeLaTeX"
        if doc.env.final != doc and doc.prods[0][-4:] != ".pdf":
            msg.error(_("there is already a post-processor registered"))
            sys.exit(2)
        doc.prods = [doc.src_base + ".pdf"]
