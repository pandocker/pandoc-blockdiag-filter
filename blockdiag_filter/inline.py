#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" blockdiag-inline
Yet another pandoc filter which plays with blockdiag interpreter
the filter finds out URL link of "blockdiag" class,
then throws given code or file to blockdiag,
saves generated image in specified directory.
the URL link will be replaced by an image link

applies MIT License (c) 2018 pandocker/Kazuki Yamamoto(k.yamamoto.08136891@gmail.com)
"""
import os
import panflute as pf
from .block import Blockdiag


class inline_blockdiag(Blockdiag):

    def __init__(self):
        super().__init__()

    def action(self, elem, doc, **kwargs):
        if isinstance(elem, pf.Link) and "blockdiag" in elem.classes:
            fn = elem.url
            options = elem.attributes
            idn = elem.identifier
            caption = elem.content
            with open(fn, "r", encoding="utf-8") as f:
                data = f.read()

            self.render_message = "[inline] generate blockdiag from"
            elem = self.render(options, data, elem, doc).content[0]
            elem.content = caption

            return elem


def main(doc=None):
    bd = inline_blockdiag()
    return pf.run_filter(bd.action, doc=doc)


if __name__ == "__main__":
    main()
