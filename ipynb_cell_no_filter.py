#!/usr/bin/env python

from pandocfilters import toJSONFilter, Div, RawBlock, CodeBlock

import json

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

 # ,Div ("",["output","error"],[("ename","TypeError"),("evalue","can't multiply sequence by non-int of type 'str'")])
  # [CodeBlock ("",[],[]) "---------------------------------------------------------------------------
  # \nTypeError                                 Traceback (most recent call last)
  # \n<ipython-input-208-4a0a40f1e879> in <module>
  # \n----> 1 '10' * '10'
  # \n\nTypeError: can't multiply sequence by non-int of type 'str'\n"]]
        elif "output" in classes and "error" in classes:
            # main_message = kvs[0][1] + kvs[1][1]
            code_block_att = contents[0]['c'][0]
            trace_message = contents[0]['c'][1]

            # new_content = RawBlock('html',
            #     '<div class="simple_error">'+trace_message+'</div>'
            # )

            # new_content = CodeBlock(code_block_att, trace_message)
            new_content = CodeBlock(["", ["python", "error"], []], trace_message)



            return new_content

if __name__ == "__main__":
    toJSONFilter(cell_no)
