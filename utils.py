def read_file(filename: str) -> str:
	with open(file=filename, mode='r') as file:
		return file.read()


def write_to_file(filename: str, content: str) -> None:
	with open(file=f'{filename}', mode='w') as f:
		f.write(content)
