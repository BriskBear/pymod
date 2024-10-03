# Import External Dependencies
from os import name

if name == 'nt':
    COL = {
        'err': '[48;5;1m[38;5;255m',
        'info': '[38;5;36m',
        'warn': '[38;5;208m',
        'none': '[0m'
    }
elif name == 'posix':
    COL = {
        'err': '\u001b[48;5;1m\u001b[38;5;255m',
        'info': '\u001b[38;5;36m',
        'warn': '\u001b[38;5;208m',
        'none': '\u001b[0m'
    }
else:
    raise ValueError(f'{name} not yet supported.')

# Write message to screen and log, with message-level-colors on screen
def reply(message, type='info', leaf='reply.log'):
    message = str(message).rstrip()

    with open(leaf, "a") as log_file:
        if type in ['error', 'err', 'e']:
            print('%sERROR: %s %s' % (COL['err'], message, COL['none']))
            log_file.write(f'ERROR: {message}\n')
        elif type in ['warning', 'warn', 'w']:
            print('%sWARNING: %s%s' % (COL['warn'], message, COL['none']))
            log_file.write(f'WARNING: {message}\n')
        else:
            print('%s%s%s' % (COL['info'], message, COL['none']))
            log_file.write(f'INFO: {message}\n')
