
#!/usr/bin/python3


# my_Clip.py - A multi-clipboard program.
import sys, pyperclip


TEXT = {'agree': '''Yes, I agree. That sounds fine to me.''',
        'busy': '''Sorry can we do this later this week or next week?''',
        'upsell': '''Will you consider making this a monthly donation?'''}


if len(sys.argv) < 2:
    print('Usage: py myClip.py [keyphrace] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]  #first command line argument is set to the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for {} is copied to clipboard'.format(keyphrase))
else:
    print('This {} is not a keyphrase'.format(keyphrase))

