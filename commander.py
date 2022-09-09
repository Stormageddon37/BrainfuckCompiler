import config


def initialize_program(bf_code):
	return f"""
	public class Main {{
		private static byte[] memory = new byte[{config.MEMORY_SIZE}];
		private static char[] code = "{bf_code}".toCharArray();
		
		private static int instruction_pointer = 0;
		private static int memory_pointer = 0;
		
		public static boolean validate_code(char[] code) {{
			int opener = 0;
			int closer = 0;
			for (int i = 0; i < code.length; i++) {{
				switch (code[i]) {{
					case '[':
						opener++;
						break;
					case ']':
						closer++;
						break;
					default:
						break;
				}}
			}}
			return opener == closer;
		}}		
		
		public static int MatchingClosingBracket(int index) {{
			int bracket_count = 1;
			for(int i = index+1; i < code.length; i++) {{
				if (code[i] == '[') {{
					bracket_count++;			
				}}
				else if (code[i] == ']') {{
					bracket_count--;
					if (bracket_count == 0) {{
					return i;
					}}
				}}
			}}
			return index;
		}}
		
		public static int MatchingOpeningBracket(int index) {{
			int bracket_count = 1;
			for(int i = index-1; i < code.length; i--) {{
				if (code[i] == ']') {{
					bracket_count++;			
				}}
				else if (code[i] == '[') {{
					bracket_count--;
					if (bracket_count == 0) {{
					return i;
					}}
				}}
			}}
			return index;
		}}
		
		public static void main(String[] args) {{
			System.out.println("hello");
			System.out.println(code);
			if (!validate_code(code)) {{
				throw new Exception("Invalid Brainfuck");
			}}
		}}
	}}
	"""
