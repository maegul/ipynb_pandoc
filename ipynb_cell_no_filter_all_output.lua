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

 		local function isempty(s)
		  return s == nil or s == ''
		end

		local error_message = elem.content[1]['text']

		if isempty(error_message) then
		  error_message = " - "
		end

		local ansi_pattern = table.concat({'s/', string.char(27), [=[\[[;0-9]*[a-zA-Z]//g]=]})

		local new_error_message = pandoc.pipe(
			"sed", {"-E",ansi_pattern}, error_message)
		-- local new_error_message = pandoc.pipe(
		-- 	"sed", {"-E",[=[s/\\x1b\[[;0-9]*[a-zA-Z]//g]=]}, error_message)

		if isempty(new_error_message) then
		  new_error_message = " - "
		end

		return pandoc.CodeBlock(
			new_error_message,
			{class='python error'}
		)
	end

end