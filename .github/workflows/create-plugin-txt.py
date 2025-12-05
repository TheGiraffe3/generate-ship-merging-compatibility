import os

def run():
	plugin = os.environ['PLUGIN']
	plugin = plugin[0].upper() + plugin[1:]
	plugintxt = '' + \
		'name "' + plugin + ' Ship Merging Compatibility"\n' +\
		'about "This plugin provides compatibility between ' + plugin + ' and ship.merging."\n' +\
		'about "Thanks to zuckung for creating the icon and the script to generate this."\n' +\
		'authors\n' +\
		'	Loymdayddaud\n' +\
		'	zuckung\n' +\
		'dependencies\n' +\
		'	requires\n' +\
		'		ship.merging\n' +\
		'		' + plugin + '\n'
	with open("plugin.txt", 'a') as fh:
		fh.write(plugintxt)

if __name__ == '__main__':
	run()
