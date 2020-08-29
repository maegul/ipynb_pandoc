## Functional ipynb to HTML converter with Pandoc

Example usage:

```shell
pandoc -s --ipynb-output=all --to html
    --filter ./ipynb_cell_no_filter.py
    -c ./ipynb_cell_no_style.css
    notebook.ipynb -o notebook.html
```

### Requirements

`pandoc v2.10.*`

`pandocfilters` (python package)

### ToDo

* Error Messages
    - At the moment, they are full of ANSI escape sequences that just clog up the HTML for no reason.
    - John McFarlane (pandoc creater) seems to be fixing this: [see GH issue](https://github.com/jgm/pandoc/issues/5633)
    - In the mean time another filter should be able to get it functional.  But at the moment __this is an arguably prohibitive regression__.
* Performance
    - Check that performance on the hub is worthwhile
    - Some things can be done to improve performance:
        + The python filter can be adapted to a lua filter which promises a performance increase (lua is embedded into pandoc, so no lua installations are necessary, which is why it's supposed to be faster)
        + The use of a filter can be avoided entirely by using a simpler regex approach, perhaps with `sed`.  Provided the regex allows for the extraction of groups, something functional would be straightforward (simply insert an additional div before a code cell using the execution_count number).  This will probably make it more difficult to rearrange the divs as has been done by the current filter, which allows for a truer replication of the notebook's look.

* Media
    - Check that media can work as desired: include any/all etc.
    - `--ipynb-output=all` includes everything.  Don't know about interactive javascript stuff.
