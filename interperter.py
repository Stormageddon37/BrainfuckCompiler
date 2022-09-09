from utils import matching_closing_bracket, matching_opening_bracket


def loop_start(code, index) -> str:
	closing_index = matching_closing_bracket(code, index)

	return """
	if(memory[memory_pointer] == 0) {
		instruction_pointer = MatchingClosingBracket(instruction_pointer)+1;
	}
	else {
		instruction_pointer++;
	}
	"""


def loop_end(code, index) -> str:
	opening_index = matching_opening_bracket(code, index)

	return """
	if(memory[memory_pointer] != 0){
		instruction_pointer = MatchingOpeningBracket(instruction_pointer)+1;
	}
	else {
		instruction_pointer++;
	}
	"""


def determine(code, index):
	big_dict = {
		'>': 'forwards();',
		'<': 'backwards();',
		'+': 'increment();',
		'-': 'decrement();',
		'.': 'output_from();',
		',': 'input_to();',
	}

	if code[index] == '[':
		return loop_start(code, index)
	elif code[index] == ']':
		return loop_end(code, index)
	else:
		return big_dict[code[index]]
