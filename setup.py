# Always prefer setuptools over distutils
from setuptools import setup, find_packages

requires = ["blockdiag"]

# VERSION = "0.0.1"
setup(
    name="pandoc_blockdiag_filter",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description="Yet another pandoc filters for blockdiag",
    author="k4zuki",
    author_email="k.yamamoto.08136891@gmail.com",
    url="https://github.com/pandocker/pandoc-blockdiag-filter",
    license="MIT",
    install_requires=requires,
    keywords=["pandoc", "markdown", "blockdiag"],
    classifiers=["Development Status :: 4 - Beta",
                 "Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: 3.6",
                 ],
    python_requires=">=3.5,!=3.0.*,!=3.1.*,!=3.2.*",
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        "console_scripts": [
            "pandocker-blockdiag-inline = blockdiag_filter.inline:main",
            "pandocker-blockdiag = blockdiag_filter.block:main",
            "pandocker-blockdiag-filters = blockdiag_filter:main",
        ],
    },
)
