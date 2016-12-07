import json, sys, os, random, re

BOTDIR = sys.path[0]
winwords = open('%s/corpus/winwords.txt' % BOTDIR, 'rb').read().split('\n')
i_affirmations = open('%s/corpus/i_affirmations.txt' % BOTDIR, 'rb').read().split('\n')
i_replacements = open('%s/corpus/i_replacements.txt' % BOTDIR, 'rb').read().split('\n')
i_am_replacements = open('%s/corpus/i_am_replacements.txt' % BOTDIR, 'rb').read().split('\n')


def get_original_msgs(BOTDIR):
	"""
	Return list of original messages from Windows 95 installer as
	dictionary.

	Each dictionary key is the name of the installer screen, and contains
	a list of messages in that screen.
	"""
	with open('%s/original_msgs.json' % BOTDIR) as data_file:
		original_msgs = json.loads(data_file.read())
	return original_msgs

def new_benefit():

	ww = random.choice(winwords)
	affirmation = random.choice(i_affirmations)

	if re.search('^I am', affirmation):
		affirmation = affirmation.replace('I am ', '', 1)
		helper_word = random.choice(i_am_replacements)
	
	elif re.search('^I ', affirmation):
		affirmation = affirmation.replace('I ', '', 1)
		helper_word = random.choice(i_replacements)

	else:
		return None

	benefit = '%s %s %s' % (ww, helper_word, affirmation)
	return benefit

def genernate_messages(BOTDIR=os.getcwd()):

	original_msgs = get_original_msgs(BOTDIR)
	install_screen = random.choice(original_msgs.keys()).lower()
	msgs = original_msgs[install_screen]

	# Remove random item from list
	random.shuffle(msgs)
	msgs.pop()
	
	# Add new benefit and shuffle again
	benefit = new_benefit()
	msgs.append(benefit)
	random.shuffle(msgs)
	
	return msgs, install_screen


