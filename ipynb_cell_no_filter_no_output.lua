function Div(elem)
	if elem.classes[1] == "cell" and elem.classes[2] == "code" then
		local exec_count = elem.attributes['execution_count']

		local function isempty(s)
		  return s == nil or s == ''
		end

		if isempty(exec_count) then
		  exec_count = " - "
		end

		local new_exec_count = table.concat({'<div class="exec_count">[', exec_count, ']:</div>'}, "")
		elem.classes = {"new_code_cell"}

		return pandoc.Div({
			pandoc.RawBlock('html', new_exec_count),
			elem
		},
		{class="new_cell_container"})

	elseif elem.classes[1] == "output" and elem.classes[2] == "error" then

		local error_message = table.concat({
			elem.attributes['ename'], '\n', elem.attributes['evalue']
		})
		return pandoc.CodeBlock(
			error_message,
			{class='python error'}
		)
		-- return pandoc.Div({
		-- 	pandoc.RawBlock('html', error_message)
		-- })
		-- elem.content[1].classes = {"python", "error"}

		-- return elem.content[1]

	end

end