import config


def initialize_program():
	return f"""
	public class Main {{
		public static void main(String[] args) {{
		{initialize_array()}
		}}
	}}
	"""


def initialize_array():
	return f'byte[] arr = new byte[{config.MEMORY_SIZE}];'
