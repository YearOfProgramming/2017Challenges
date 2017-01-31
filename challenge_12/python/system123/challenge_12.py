import re

def compress(input_str):
	COMPRESS_LVL = 3

	seq_cnt = 0
	cur_char = ""
	output = ""

	for i, c in enumerate(input_str):

		if cur_char == c:
			seq_cnt += 1
		if cur_char != c or i == (len(input_str)-1):
			if seq_cnt > COMPRESS_LVL:
				output += "{}#{}".format(cur_char, seq_cnt)
			else:
				output += cur_char*seq_cnt

			cur_char = c
			seq_cnt = 1	

	return(output)

def decompress(input_str):
	output = input_str
	matches = re.findall( r'(.#\d+)' , input_str)

	for m in matches:
		info = re.match(r'(.)#(\d+)', m)
		output = output.replace( m, info.group(1)*int(info.group(2)) )

	return(output)


if __name__ == "__main__":
	t_str = "aaabbbbcdeeeeeeeefffffhh"
	print(t_str)
	print(compress(t_str))
	print(decompress(compress(t_str)))
