# import spiper
import sys
if __name__ == '__main__':
	debug = 0
	jump = 0
	for line in sys.stdin:
		# print(repr(line))
		if line.startswith('+'):
			if jump:
				sys.stdout.write('\n')
			sp = line[2:].split()

			for i,token in enumerate(sp):
				if debug:
					sys.stderr.write(repr(token)+'\n')
					sys.stderr.flush()
				if i+1 != len(sp):
					sys.stdout.write(token+'\\\n  ')
				else:
					sys.stdout.write(token+'\n')
		else:
			# line = line+'\n' if not line.endswith('\n') else line
			sys.stdout.write('### '+line)
			jump = 1


# class flags:
# 	empty   = 0
# 	comment = 1
# 	command = 2
# def parse_bash(gen):
# 	buf = []
# 	while True:
# 		line = next(gen, None)
# 		if line is None:
# 			break
# 		line = line.lstrip()
# 		if not line:
# 			yield (flags.empty, [line])
# 		if line.startswith('#'):
# 			yield (flags.comment, [line])
# 		if line.endswith('\\\n'):
# 			buf.append(line)
# 		else:
# 			yield (flags.command, buf)

# import sys
# from pprint import pprint
# if __name__ == '__main__':
# 	it = parse_bash(open(sys.argv[1],'r'))
# 	# sys.stdout
# 	fh = sys.stdout
# 	for flag, lines in it:
# 		if flag == flags.command:
# 			fh.write(''.join(lines))
# 			stdout = LoggedShellCommand(lines)
# 			fh.write(''.join(['#%s\n'%x for x in stdout.splitlines()]))

# 	[pprint(x) for x in it]
		# if buf.strip()

	# for line in gen:


# for line in stdin:


