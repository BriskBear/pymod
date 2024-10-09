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

EC = {
    'is_error': lambda msg: True if str(msg.__class__.__mro__[-2]).split("'")[1] == 'BaseException' else False,
    'get': lambda err: str(err.__class__).split("'")[1],
    'FileNotFoundError': lambda err: f"{err.args[1]}: {err.filename}",
    'KeyError': lambda err: f"\'{err.args[0]}\' is not defined",
    'NameError': lambda err: err.args[0].replace('name ', ''),
    'ValueError': lambda err: err.args[0]
}

# Write message to screen and log, with message-level-colors on screen
def reply(message, type='info', leaf='reply.log'):
    out_message = str(message).rstrip()
    with open(leaf, "a") as log_file:
        if type in ['error', 'err', 'e']:
            if EC['is_error'](message):
                print('%sERROR: %s %s' % (COL['err'], get_error(message), COL['none']))
            else:
                print('%sERROR: %s %s' % (COL['err'], out_message, COL['none']))
            log_file.write(f'ERROR: {message}\n')
        elif type in ['warning', 'warn', 'w']:
            print('%sWARNING: %s%s' % (COL['warn'], out_message, COL['none']))
            log_file.write(f'WARNING: {message}\n')
        else:
            print('%s%s%s' % (COL['info'], out_message, COL['none']))
            log_file.write(f'INFO: {out_message}\n')

def get_error(err):  # Get a descriptive error-message
    klass = EC['get'](err)

    try:
        return klass + ': ' + EC[klass](err)
    except KeyError as k:
        reply(EC['KeyError'](k), 'e', 'reply-errors.log')
