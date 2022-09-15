from commander import initialize_program
from compiler import compile_file, execute_file
from interperter import determine
from utils import write_to_file, read_file, delete_file


def main():
	brainfuck_code = read_file('input.bf')
	java_bf = ''
	for i, char in enumerate(brainfuck_code):
		java_bf += 3 * '\t' + determine(code=brainfuck_code, index=i) + '\n'

	write_to_file('Main.java', initialize_program(bf_code=''.join(brainfuck_code)) + java_bf + '\t}\n}')
	compile_file('Main.java')
	execute_file('Main')
	delete_file('Main.class')


if __name__ == '__main__':
	main()
