import os

REFERENSI = '{{ referensi() }}'

for path, subdirs, files in os.walk('docs'):
    for name in files:
        with open(os.path.join(os. getcwd(),path, name), 'r') as file:
            if REFERENSI in file.read():
                file.close()
            else:
                file.close()
                with open(os.path.join(os. getcwd(),path, name), 'a') as append:
                    append.write('\n\n' + REFERENSI)
                    append.close