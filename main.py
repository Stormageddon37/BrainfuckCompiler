from commander import initialize_program
from compiler import compile_and_execute_file
from utils import write_to_file, read_file


def main():
	write_to_file('Main.java', initialize_program(read_file('input.bf')))
	compile_and_execute_file('Main')


if __name__ == '__main__':
	main()
