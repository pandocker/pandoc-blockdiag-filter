import panflute as pf
from . import block, inline


def main(doc=None):
    ibd = inline.inline_blockdiag()
    bd = block.Blockdiag()
    return pf.run_filters([ibd.action, pf.yaml_filter], tag="blockdiag", function=bd.render, doc=doc)


if __name__ == "__main__":
    main()
