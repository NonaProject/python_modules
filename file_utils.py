# File Utils Module

def create_file(filename): # Creates An empty file at dir
    try:
        with open(filename, 'w') as f:
            f.write('')
    except Exception as e:
        print(f'Error Raised {e}')

def overwrite_file_content(filename, content): # Over-Writes the content of a given file
    try:
        with open(filename, 'w') as f:
            f.write(content)
    except Exception as e:
        print(f'Error Raised {e}')
