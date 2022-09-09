import os


def compile_file(filename: str):
	os.system(f'javac {filename}')


def execute_file(filename: str):
	os.system(f'java {filename}')
