# Import External Dependencies
from os import name

match name:
    case 'nt':
        COL = {
            'err': '[48;5;1m[38;5;255m',
            'info': '[38;5;36m',
            'warn': '[38;5;208m',
            'none': '[0m'
        }
    case 'posix':
        COL = {
            'err': '\u001b[48;5;1m\u001b[38;5;255m',
            'info': '\u001b[38;5;36m',
            'warn': '\u001b[38;5;208m',
            'none': '\u001b[0m'
        }

def reply(message, type, leaf='reply.log'):
    with open(leaf, "a") as log_file:
        match type:
            case 'error' | 'err' | 'e':
                print('%sERROR: %s%s' % (COL['err'], str(message), COL['none']))
                log_file.write(f'ERROR: {message}\n')
            case 'warning' | 'warn' | 'w':
                print('%sWARNING: %s%s' % (COL['warn'], str(message), COL['none']))
                log_file.write(f'WARNING: {message}\n')
            case _:
                print('%s%s%s' % (COL['info'], str(message), COL['none']))
                log_file.write(f'INFO: {message}\n')
