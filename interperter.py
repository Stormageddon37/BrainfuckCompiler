def determine(code, index) -> str:
	big_dict = {
		'>': 'memory_pointer++;',
		'<': 'memory_pointer--;',
		'+': 'memory[memory_pointer]++;',
		'-': 'memory[memory_pointer]--;',
		'.': 'System.out.print((char) memory[memory_pointer]);',
		',': 'System.out.println();\nmemory[memory_pointer] = input.nextByte();',
		'[': 'while(memory[memory_pointer] != 0) {',
		']': '}'
	}

	return big_dict[code[index]]
