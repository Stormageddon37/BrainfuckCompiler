import os


def compile_file(filename: str) -> int:
	return os.system(f'javac {filename}')


def execute_file(filename: str) -> int:
	return os.system(f'java {filename}')
