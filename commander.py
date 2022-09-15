import config


def initialize_program(bf_code):
	return f"""import java.util.Scanner;

public class Main {{
	private static char[] code = "{''.join(bf_code)}".toCharArray();
	private static byte[] memory = new byte[{config.MEMORY_SIZE}];
	private static Scanner input = new Scanner(System.in);
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
	
	public static void main(String[] args) {{
		if (!validate_code(code)) System.exit(0);
"""
