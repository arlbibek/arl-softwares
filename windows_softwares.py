# the code will open the list of softwares on your default web browser
# import webbrowser
# webbrowser.open('', new=1)
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

for line in fh:
    line = line.strip()
    if line.startswith('Page'):
        print(line)
        continue
    elif line.startswith('Download'):
        print(line)
        continue
    elif line.startswith('MS Version'):
        print(line)
        continue
    if line.startswith('ANDROID'):
        print('Done: Windows apps')
        break
    print(line)


print('"""Done"""')
exit()
