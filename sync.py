import shutil

DIR_PATH = '/Users/jcbowden/Documents/Obsidian Vault/publish/docs'

def sync(original_path, pub_path):
	print(f'{original_path} --> {pub_path}')
	title = original_path.split('/')[-1]
	shutil.copy(original_path, f'{DIR_PATH}/{pub_path}/{title}')

if __name__ == "__main__":
	sync('/Users/jcbowden/Documents/Obsidian Vault/__ref/yogas.md', 'misc')
	sync('/Users/jcbowden/Documents/Obsidian Vault/__ref/Engagement Queue.md', 'for_self')
	sync('/Users/jcbowden/Documents/Obsidian Vault/__ref/Engagement List — Hum.md', 'for_self')
