#!/usr/bin/env python

from pandocfilters import toJSONFilter, Div, RawBlock

# ,Div ("",["cell","code"],[("execution_count","6")])
def cell_no(key, value, format, meta):

    if key == 'Div':
        [[ident, classes, kvs], contents] = value
        if "code" in classes and "cell" in classes:
            # exec_count = kvs[0][1]
            exec_count = ' - '
            if len(kvs) > 0:
                if type(kvs[0]) == list and kvs[0][0] == 'execution_count':
                    exec_count = kvs[0][1]

            new_content = Div([str(exec_count), ["new_cell_container"], kvs],
                [
                    RawBlock('html',
                        '<div class="exec_count">['+str(exec_count)+']:</div>'
                    ),
                    Div([ident, ["new_code_cell"], kvs], contents)
                ]
            )

            return new_content

if __name__ == "__main__":
    toJSONFilter(cell_no)
