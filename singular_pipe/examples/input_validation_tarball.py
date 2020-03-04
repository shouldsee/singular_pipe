'''
Showing how Prefix differs from File
'''
from singular_pipe.types import File,Prefix,Path
from singular_pipe.runner import cache_run_verbose, cache_run

from singular_pipe.shell import LoggedShellCommand
from singular_pipe.runner import cache_check_changed,cache_run_verbose,force_run,cache_run
import singular_pipe

def gen_files(self, prefix, 
	_seq = 'AGCTTCGTC',
	 _output=[
	 	File('out_txt')]):
	with open(self.output.out_txt,'w') as f:
		f.write( _seq * 10 )
	return self

def tarball_dangerous_cache(self,prefix, 
	input_prefix = File,
	_output=[
	File('tar_gz'),
	File('cmd')]):
	with input_prefix.dirname(): 
		stdout = LoggedShellCommand([
			'tar', '-cvzf', self.output.tar_gz, input_prefix.basename()+'*',
			], 
			self.output.cmd)
	return self	

def tarball_prefix_cache(self,prefix, 
	input_prefix = Prefix,
	_output=[
		File('tar_gz'),
		File('cmd')]):
	
	with input_prefix.dirname(): 
		stdout = LoggedShellCommand([
			'tar', '-cvzf', self.output.tar_gz, input_prefix.basename()+'*',
			], 
			self.output.cmd)
	return self

def main():
	# singular_pipe.rcParams['dir_layout'] = dir_layout

	prefix = Path('/tmp/singular_pipe.test_run/root')
	prefix.dirname().rmtree_p()


	print('\n---------------------Run1---\n## got') if __name__ == '__main__' else None
	res1 = force_run(gen_files, prefix)
	tups = (tarball_dangerous_cache, prefix, res1.prefix_named)
	force_run(*tups)
	
	res1 = force_run(gen_files, prefix)
	cache_run_verbose(*tups)

	s = '''
## expect 
[cache_run] {"job_name"="tarball_dangerous_cache"_"input_ident_changed"=1_"output_ident_chanegd"=0}

	* This change to input is ignored because tarball_dangerous_cache(input_prefix=File) would not expand to match the files during input validation The type specified in def line will be used for detecting a timestamp/filesize change	
	
	'''.strip()
	print(s) if __name__ == '__main__' else None


	print('---------------------Run2---\n## got') if __name__ == '__main__' else None
	res1 = force_run(gen_files, prefix)
	tups = (tarball_prefix_cache, prefix, res1.prefix_named)
	force_run(*tups)
	
	res1 = force_run(gen_files, prefix)
	cache_run_verbose(*tups)
	s = '''
## expect 
[cache_run] {"job_name"="tarball_prefix_cache"_"input_ident_changed"=1_"output_ident_chanegd"=0}

	* Because tarball_prefix_cache(input_prefix=Prefix) is expanded into the appropriate files during input validation.
	* Note that the Prefix only expands into a shallow match and does not recurse into sub-directory during input validation
	'''.strip()
	print(s) if __name__ == '__main__' else None
	print('------Output Directory. (dir_layout={singular_pipe.rcParams.dir_layout})--------\n'.format(singular_pipe=singular_pipe),
		LoggedShellCommand(['echo [ls]',prefix,'&&','ls','-lhtr',prefix.dirname(),],'/dev/null'))

if __name__ == '__main__':
	main()
