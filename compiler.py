import os


def compile_file(filename: str):
	os.system(f'javac {filename}')


def execute_file(filename: str):
	os.system(f'java {filename}')


def compile_and_execute_file(filename: str):
	compile_file(filename)
	execute_file(filename)
