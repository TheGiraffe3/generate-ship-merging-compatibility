import os

def run():
	repository = os.environ['PLUGIN_REPOSITORY']
	reposplitted = repository.split('\n')
	if reposplitted[0] == '### Repository':
		print('		SUCCESS: Newly created issue is a compatibility request.')
	print('REPOSITORY TO DOWNLOAD:')
	repofull = reposplitted[2]
	reponamesplit = repofull.split('/')
	repo = reponamesplit[0] + '/' + reponamesplit[1]
	repo = repo.rstrip('\n')
	print(repo)
	with open("repository", 'a') as fh:
		print(f'{repo}', file=fh)
	reponame = reponamesplit[1]
	print(reponame)
	with open("repository_name", 'a') as fh:
		fh.write(reponame)
	datapath = ''
	for i in range(1, len(reponamesplit)):
		datapath += reponamesplit[i] + '/'
	datapath += 'data'
	print(datapath)
	with open("datapath", 'a') as fh:
		fh.write(datapath)

if __name__ == '__main__':
	run()
