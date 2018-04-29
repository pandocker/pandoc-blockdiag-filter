# pandoc-blockdiag-filter
yet another pandoc filter to import blockdiag diagram similar to <https://github.com/D3f0/pandoc_blockdiag>

# samples
`````markdown
[blockdiag sample](diag.diag){.blockdiag}

```blockdiag
---
{
  "This is" -> another -> blockdiag -> sample;
}
```
`````

[inline blockdiag sample](diag.diag){.blockdiag}

```blockdiag
caption: blockdiag codeblock sample
---
{
  "This is" -> another -> blockdiag -> sample;
}
```
