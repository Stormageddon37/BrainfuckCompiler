import config


def initialize_program():
	return f"""
	public class Main {{
		public static void main(String[] args) {{
		int pointer = 0;
		byte[] arr = new byte[{config.MEMORY_SIZE}];
		}}
	}}
	"""
