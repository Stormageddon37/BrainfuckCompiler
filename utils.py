def read_file(filename: str) -> str:
	with open(file=filename, mode='r') as file:
		return file.read()


def write_to_file(filename: str, content: str) -> None:
	with open(file=f'{filename}', mode='w') as f:
		f.write(content)


def remove_newlines(content: str) -> str:
	return content.replace('\n', '')


def matching_closing_bracket(code, index):
	bracket_count = 1
	for i in range(start=index + 1, stop=len(code), step=1):
		if code[i] == '[':
			bracket_count += 1
		elif code[i] == ']':
			bracket_count -= 1
			if bracket_count == 0:
				return i


def matching_opening_bracket(code, index):
	bracket_count = 1
	for i in range(start=index + 1, stop=0, step=-1):
		if code[i] == ']':
			bracket_count += 1
		elif code[i] == '[':
			bracket_count -= 1
			if bracket_count == 0:
				return i
	"""
			public static int MatchingClosingBracket(int index) {{
			int bracket_count = 1;
			for(int i = index+1; i < code.length; i++) {{
				if (code[i] == '[') {{
					bracket_count++;			
				}}
				else if (code[i] == ']') {{
					bracket_count--;
					if (bracket_count == 0) {{
					return i;
					}}
				}}
			}}
			return index;
		}}
		
		public static int MatchingOpeningBracket(int index) {{
			int bracket_count = 1;
			for(int i = index-1; i < code.length; i--) {{
				if (code[i] == ']') {{
					bracket_count++;			
				}}
				else if (code[i] == '[') {{
					bracket_count--;
					if (bracket_count == 0) {{
					return i;
					}}
				}}
			}}
			return index;
		}}
"""
