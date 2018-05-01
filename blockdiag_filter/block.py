#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Blockdiag
Yet another pandoc filter which plays with blockdiag interpreter
the filter finds out code block of "blockdiag" class,
then throws given code or file to blockdiag,
saves generated image in specified directory.
the codeblock will be replaced by an image link

applies MIT License (c) 2018 pandocker/Kazuki Yamamoto(k.yamamoto.08136891@gmail.com)
"""

import os
import panflute as pf
import hashlib
from blockdiag import command


class Blockdiag(object):

    def __init__(self):
        self.defaultdir_to = "svg"
        self.doc = ""
        self.render_message = ""
        self.blockdiag = command.BlockdiagApp()

    def render(self, options, data, element, doc):
        self.doc = doc
        self.source = options.get("input")
        self.toPNG = bool(options.get("png", True))
        self.toSVG = bool(options.get("svg", False))
        self.toPDF = True if doc.format in ["latex"] else bool(options.get("pdf", False))
        self.caption = options.get("caption", "Untitled")
        self.dir_to = options.get("directory", self.defaultdir_to)

        if os.path.exists(self.dir_to) != 1:
            os.mkdir(self.dir_to)

        self.counter = hashlib.sha1(data.encode("utf-8")).hexdigest()[:8]
        self.basename = "/".join([self.dir_to,
                                  str(self.counter)])

        if not self.source and data is not None:
            # pf.debug("not source and data is not None")
            self.source = ".".join([self.basename, "txt"])
            code = data
            open(self.source, "w", encoding="utf-8").write(data)
        else:  # source and data is "dont care"
            code = open(self.source, "r", encoding="utf-8").read()

        assert self.source is not None, "option input is mandatory"
        assert isinstance(self.toPNG, bool), "option png is boolean"
        assert isinstance(self.toPDF, bool), "option pdf is boolean"

        self.svg = ".".join([self.basename, "svg"])
        self.png = ".".join([self.basename, "png"])
        self.pdf = ".".join([self.basename, "pdf"])

        # parsed = self.blockdiag.module.parser.parse_string(code)
        args = ["-T", "svg", "-a", "-o", self.svg, self.source]
        self.blockdiag.run(args)

        if(self.toPDF):
            args = ["-T", "pdf", "-a", "-o", self.pdf, self.source]
            self.blockdiag.run(args)

        if(self.toPNG):
            args = ["-T", "png", "-a", "-o", self.png, self.source]
            self.blockdiag.run(args)

        if self.doc.format in ["latex"]:
            linkto = self.pdf
        elif self.doc.format in ["html", "html5"]:
            linkto = self.svg
        else:
            if not (self.toPNG):
                args = ["-T", "png", "-a", "-o", self.png, self.source]
                self.blockdiag.run(args)
            linkto = self.png

        caption = pf.convert_text(self.caption)
        caption = caption[0]
        caption = caption.content

        render_message = " ".join(["generate blockdiag from", linkto])
        self.render_message = render_message if not self.render_message else " ".join([self.render_message, linkto])
        pf.debug(self.render_message)
        element.classes.remove("blockdiag")
        linkto = os.path.abspath(linkto).replace("\\", "/")
        img = pf.Image(*caption, classes=element.classes, url=linkto,
                       identifier=element.identifier, title="fig:", attributes=element.attributes)
        # pf.debug(img)
        ans = pf.Para(img)
        # pf.debug(ans)

        return ans


def main(doc=None):
    bd = Blockdiag()
    return pf.run_filter(pf.yaml_filter, tag="blockdiag", function=bd.render, doc=doc)


if __name__ == '__main__':
    main()
