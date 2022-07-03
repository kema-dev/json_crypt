import os
import sys
import tkinter as tk
from tkinter.filedialog import askopenfilename
from aes import AESCipher as aes
import getpass as gp
import re
from pathlib import Path

def get_infile_path():
    """
    Get the file path of the input json file.
    """
    if debug == True:
        print('Getting input file path...')
    pop = tk.Tk()
    pop.withdraw()
    print('Choose the json file you want to encrypt / decrypt')
    try:
        fn = tk.filedialog.askopenfilename()
    except:
        print('No file chosen')
        exit()
    if not os.path.isfile(fn):
        print('File not found')
        exit()
    if debug == True:
        print('File path loaded (' + fn + ')')
    return fn


def get_outfile_path(infile, mode):
    """
    Get the file path of the output json file.
    """
    if debug == True:
        print('Getting output file path...')
    pop = tk.Tk()
    pop.withdraw()
    print('Choose your destination folder')
    try:
        dn = tk.filedialog.askdirectory()
    except:
        print('No directory chosen')
        exit()
    if not os.path.isdir(dn):
        print('Directory not found')
        exit()
    fn = dn + '/' + re.search('[\w]+?(?=\.)',
                              infile).group() + '_' + mode + '.json'
    if debug == True:
        print('Output file path loaded (' + fn + ')')
    return fn


def get_key():
    """
    Get the key.
    """
    if debug == True:
        print('Getting key...')
    key = ''
    while not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])(?=^[a-zA-Z0-9!@#$%^&*]*$).{16,32}$', key):
        key = gp.getpass(
            """Time to choose you key, it must:
- be between 16 and 32 characters long
- contain at least one number
- contain at least one lowercase letter
- contain at least one uppercase letter
- contain at least one special character
- contain only letters, numbers, and special characters
Allowed characters: [a-z] [A-Z] [0-9] [!@#$%^&*]
The key will be used to encrypt the data, so make sure you remember it!
Enter your key: """
        )
        if not re.search(r'^.{16,32}$', key):
            print('Fail! Key must be between 16 and 32 characters long')
            continue
        if not re.search(r'[0-9]', key):
            print('Fail! Key must contain at least one number')
            continue
        if not re.search(r'[a-z]', key):
            print('Fail! Key must contain at least one lowercase letter')
            continue
        if not re.search(r'[A-Z]', key):
            print('Fail! Key must contain at least one uppercase letter')
            continue
        if not re.search(r'[!@#$%^&*]', key):
            print('Fail! Key must contain at least one special character')
            continue
        if not re.search(r'^[a-zA-Z0-9!@#$%^&*]*$', key):
            print('Fail! Key contains an invalid character.')
            continue
    pad_key = key.ljust(32, '0')
    if debug == True:
        print('Key loaded')
    return pad_key


def export_to_file(data, file):
    """
    Export the json data to a file.
    """
    if debug == True:
        print('Exporting data to file...')
    try:
        with open(file, 'wb') as outfile:
            outfile.write(data.encode('utf-8'))
    except Exception as e:
        print(e)
        exit()
    if debug == True:
        print('Data exported to ' + file)


def encrypt():
    """
    Encrypt the data.
    """
    if short != '':
        in_name = SHORT_E_INFILE
        outfile = SHORT_E_OUTFILE
        key = SHORT_E_KEY
    else:
        in_name = get_infile_path()
        outfile = get_outfile_path(in_name, 'encrypted')
        key = get_key()
    data = get_data(in_name)
    data = encrypt_json(data, key)
    if not Path(outfile).parent.is_dir():
        os.mkdir(Path(outfile).parent)
    export_to_file(data, outfile)


def encrypt_string(string, cipher_proc):
    """
    Encrypt a string.
    """
    if debug == True:
        print('Encrypting string...')
    if string is None or string == '':
        if debug == True:
            print('String is None, skipping')
        return ''
    try:
        encrypted = cipher_proc.encrypt(string)
    except Exception as e:
        if debug == True:
            print(e)
        print('Fail! Unknow error. Enable debug mode and try again to see the error message')
        exit()
    if debug == True:
        print('String encrypted')
    return encrypted.decode('utf-8')


def decrypt():
    """
    Decrypt the data.
    """
    if short != '':
        in_name = SHORT_D_INFILE
        outfile = SHORT_D_OUTFILE
        key = SHORT_D_KEY
    else:
        in_name = get_infile_path()
        outfile = get_outfile_path(in_name, 'decrypted')
        key = get_key()
    data = get_data(in_name)
    data = decrypt_json(data, key)
    export_to_file(data, outfile)


def decrypt_string(string, cipher_proc):
    """
    Decrypt a string.
    """
    if debug == True:
        print('Decrypting string...')
    if string is None or string == '':
        if debug == True:
            print('String is None, skipping')
        return ''
    try:
        decrypted = cipher_proc.decrypt(string)
    except Exception as e:
        if debug == True:
            print(e)
        print('Fail! This is most likely to be caused by a wrong key. Enable debug mode and try again to see the error message')
        exit()
    if debug == True:
        print('String decrypted')
    return decrypted


def main():
    """
    Main function.
    """
    global short
    global debug
    short = ''
    debug = ''
    for i in range(len(sys.argv)):
        if sys.argv[i] == '--debug':
            debug = True
            print('Debug mode enabled')
        elif sys.argv[i] == '-e':
            short = 'e'
            print('Short mode enabled (encryption)')
        elif sys.argv[i] == '-d':
            short = 'd'
            print('Short mode enabled (decryption)')
        elif sys.argv[i] == '-t':
            short = 't'
            print('Short mode enabled (encryption + decryption)')
    if short != '':
        choice = short
    else:
        choice = input('Do you want to encrypt or decrypt? (e/d) ')
    if choice == 'e':
        encrypt()
    elif choice == 'd':
        decrypt()
    elif choice == 't':
        encrypt()
        decrypt()
    else:
        print('Invalid choice')
        exit()


def get_data(in_name):
    """
    Get the data from the file.
    """
    if debug == True:
        print('Getting data from file...')
    try:
        with open(in_name, 'rb') as infile:
            data = infile.read()
    except Exception as e:
        print(e)
        exit()
    if debug == True:
        print('Data loaded')
    return data


def encrypt_json(data, key):
    """
    Encrypt the json data.
    """
    if debug == True:
        print('Encrypting json data...')
    cipher_proc = aes(key)
    pattern = r'(:(\s?)*)(\".*?\"|.*?(?=[,\[\]{}\s]))'
    data = data.decode('utf-8')
    data = re.sub(pattern, lambda m: m.group(1) + encrypt_string(m.group(3), cipher_proc), data)
    if debug == True:
        print('Json data encrypted')
    return data

def decrypt_json(data, key):
    """
    Decrypt the json data.
    """
    if debug == True:
        print('Decrypting json data...')
    cipher_proc = aes(key)
    pattern = r'(:(\s?)*)(\".*?\"|.*?(?=[,\[\]{}\s]))'
    data = data.decode('utf-8')
    data = re.sub(pattern, lambda m: m.group(1) + decrypt_string(m.group(3), cipher_proc), data)
    if debug == True:
        print('Json data decrypted')
    return data


if __name__ == '__main__':
    PARENT_FOLDER = str(Path(__file__).parent.parent.absolute())
    SAMPLE_FOLDER = PARENT_FOLDER + '/sample/'
    SAMPLE_FILE = 'bitwarden_export_20220702203804.json'
    SAMPLE_NAME = ''.join(SAMPLE_FILE.split('.')[:-1])
    SAMPLE_EXT = '.' + SAMPLE_FILE.split('.')[-1]
    SHORT_E_INFILE = SAMPLE_FOLDER + SAMPLE_FILE
    SHORT_E_OUTFILE = PARENT_FOLDER + '/out/' + SAMPLE_NAME + '_encrypted' + SAMPLE_EXT
    SHORT_E_KEY = '#Password123%123456'.ljust(32)
    SHORT_D_INFILE = SHORT_E_OUTFILE
    SHORT_D_OUTFILE = SHORT_D_INFILE.replace(SAMPLE_EXT, '') + '_decrypted' + SAMPLE_EXT
    SHORT_D_KEY = '#Password123%123456'.ljust(32)
    main()
    print('Done')
    exit()
