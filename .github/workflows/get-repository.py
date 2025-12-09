import os

def run():
	repository = os.environ['PLUGIN_REPOSITORY']
	reposplitted = repository.split('\n')
	if reposplitted[0] == '### Repository':
		print('		SUCCESS: Newly created issue is a compatibility request.')
	print('REPOSITORY TO DOWNLOAD:')
	repo = reposplitted[2]
	print(repo)
	with open("repository", 'a') as fh:
		print(f'{repo}', file=fh)
	reponamesplit = repo.split('/')
	reponame = reponamesplit[1]
	print(reponame)
	with open("repository_name", 'a') as fh:
		fh.write(reponame)
	datapath = ''
	for i in range(1, len(reponamesplit)):
		datapath += reponamesplit[i]
	print(datapath)
	with open("datapath", 'a') as fh:
		fh.write(datapath)

if __name__ == '__main__':
	run()
