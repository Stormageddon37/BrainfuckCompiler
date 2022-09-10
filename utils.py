def read_file(filename: str) -> list[str]:
	with open(file=filename, mode='r') as file:
		return [x for x in remove_newlines(file.read())]


def write_to_file(filename: str, content: str) -> None:
	with open(file=f'{filename}', mode='w') as f:
		f.write(content)


def remove_newlines(content: str) -> str:
	return content.replace('\n', '')
