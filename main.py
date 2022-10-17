from commander import initialize_program
from compiler import compile_file, execute_file
from interpreter import determine
from utils import write_to_file, read_file, delete_file


def main():
	original_bf_code = read_file('input.bf')
	java_bf_code = ''
	for i, char in enumerate(original_bf_code):
		java_bf_code += 3 * '\t'
		java_bf_code += determine(code=original_bf_code, index=i)
		java_bf_code += '\n'

	content = initialize_program(original_bf_code)
	content += java_bf_code + '\t}\n}'
	write_to_file('Main.java', content)
	compile_file('Main.java')
	execute_file('Main')
	delete_file('Main.class')


if __name__ == '__main__':
	main()
