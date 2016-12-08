import json, sys, os, random, re

def random_from_list(term_list, logfile, minimum_freshness=1, max_retry=500 ):
    """
    Get a random term from supplied list, but lookup term against
    a log file file and reject random choice if term is within
    last N lines of log file.

    Keep trying until get a valid result.
    """
        
    log = open('%s/%s' % (PROJDIR, logfile), 'rb').read().split('\n')    
    log.reverse() # Newest entries at top
    log = log[0:minimum_freshness]

    ctr = 0
    while ctr < max_retry:
        word = random.choice(term_list)
        if not word in log:
            return word

        ctr += 1


def get_original_msgs():
    """
    Return list of original messages from Windows 95 installer as
    dictionary.

    Each dictionary key is the name of the installer screen, and contains
    a list of messages in that screen.
    """
    with open('%s/original_msgs.json' % PROJDIR) as data_file:
        original_msgs = json.loads(data_file.read())
    return original_msgs

def new_benefit():

    # Open Term Lists
    winwords = open('%s/corpus/winwords.txt' % PROJDIR, 'rb').read().split('\n')
    i_affirmations = open('%s/corpus/i_affirmations.txt' % PROJDIR, 'rb').read().split('\n')
    i_replacements = open('%s/corpus/i_replacements.txt' % PROJDIR, 'rb').read().split('\n')
    i_am_replacements = open('%s/corpus/i_am_replacements.txt' % PROJDIR, 'rb').read().split('\n')

    # Do the work of generating the benefit:
    # Windows Word + Helper Word + Snipped Affirmation = Benefit    
    ww = random_from_list(winwords, 'winword.log', 8)
    affirmation = random_from_list(i_affirmations, 'affirmation.log', 75)

    if re.search('^I am', affirmation):
        trunc_affirmation = affirmation.replace('I am ', '', 1)
        helper_word = random.choice(i_am_replacements)
    
    elif re.search('^I ', affirmation):
        trunc_affirmation = affirmation.replace('I ', '', 1)
        helper_word = random.choice(i_replacements)

    else:
        return None

    benefit = '%s %s %s' % (ww, helper_word, trunc_affirmation)

    # Log words used to log to prevent repeats
    with open("%s/winword.log" % PROJDIR, "a") as ww_log:
        ww_log.write(ww + '\n')

    with open("%s/affirmation.log" % PROJDIR, "a") as af_log:
        af_log.write(affirmation + '\n')

    return benefit

def genernate_messages(BOTDIR=os.getcwd()):

    global PROJDIR
    PROJDIR = BOTDIR

    original_msgs = get_original_msgs()
    install_screen = random.choice(original_msgs.keys()).lower()
    msgs = original_msgs[install_screen]

    # Remove random item from list
    random.shuffle(msgs)
    msgs.pop()
    
    # Add new benefit and shuffle again
    benefit = new_benefit()
    msgs.append(benefit)
    random.shuffle(msgs)

    # Finally, log screen image to prevent repeats
    with open("%s/screen.log" % PROJDIR, "a") as screen_log:
        screen_log.write(install_screen + '\n')
    
    return msgs, install_screen


