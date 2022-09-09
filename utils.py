def read_file(filename: str) -> str:
	with open(filename, 'r') as file:
		return file.read()


def write_to_file(filename: str, content: str):
	with open(file=f'{filename}', mode='w') as f:
		f.write(content)
