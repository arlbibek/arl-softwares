# the code will open the list of softwares on your default web browser
# import webbrowser
# webbrowser.open(, new=2)
filename = 'softwares.txt'


while True:
    try:
        fh = open(filename, 'rt')
        print("File found: '" + filename + "'")
        break
    except FileNotFoundError:
        print("No such file or directory: '" + filename + "'")
        filename = input("Enter fielname: ")
        continue
    except Exception:
        print("Someting went worong!")
        exit()
input('Press Enter to continue.')

for line in fh:
    line = line.strip()
    if line.startswith('Download Page:'):
        print('Download Page Link:', dpl)
        # webbrowser.open(dpl)

        continue
    elif line.startswith('Direct Download:'):
        ddl = line.split(': ')[1]
        print('Direct Download Link: ', ddl)
        # webbrowser.open(ddl)

        continue
    elif line.startswith('Microsoft Store:'):
        print(line)
        continue
    elif line.startswith('##'):
        if line.startswith('## ANDROID'):
            print('\nWindows apps Compeleted\n')
            break
        continue
    elif line == '':
        continue
    print()
    print('Name: ', line)

print('"""Done"""')
exit()
