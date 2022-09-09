import config


def initialize_program(bf_code):
	return f"""
	public class Main {{
		private static byte[] memory = new byte[{config.MEMORY_SIZE}];
		private static char[] code = "{bf_code}".toCharArray();
		
		private static int instruction_pointer = 0;
		private static int memory_pointer = 0;		
		
		public static int nextClosingBracket(int index) {{ 
			for(int i = index; i < code.length; i++) {{
				if (code[i] == ']') {{
					return i+1;
				}}
			}}
			return index;
		}}
		
		public static void main(String[] args) {{
			System.out.println("hello");
			System.out.println(code);
		}}
	}}
	"""
