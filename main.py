from commander import initialize_program
from compiler import compile_file, execute_file
from interperter import determine
from utils import write_to_file, read_file, remove_newlines


def main():
	input_code = read_file('input.bf')
	input_code = remove_newlines(input_code)
	input_code = [x for x in input_code]
	java_bf = ''
	for i, char in enumerate(input_code):
		java_bf += determine(input_code, i) + '\n'
	footer = '//code ends here\n}}'

	write_to_file('Main.java', initialize_program(input_code) + java_bf + footer)
	compile_file('Main.java')
	execute_file('Main')


if __name__ == '__main__':
	main()
