import shutil

DIR_PATH = '/Users/jcbowden/Documents/Obsidian Vault/publish/'

def sync(original_path, pub_path):
	print(f'{original_path} --> {pub_path}')
	shutil.copy(original_path, DIR_PATH+pub_path)

if __name__ == "__main__":
	sync('/Users/jcbowden/Documents/Obsidian Vault/yogas.md', 'docs/misc/yogas.md')
