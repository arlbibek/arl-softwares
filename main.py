'''Download file using GetRequest using powershell and bat file'''
# This program will extrcts download links from README.md

with open('README.md', 'rt') as rm:
    windows = False
    for line in rm:
        # print(line)
        if line.startswith('# Windows'):
            windows = True
        if line.startswith('### Others'):
            break
        if windows is True:
            if line.startswith('## '):
                print()
                app_name = line.split('# ')[1].split("\n")[0]
                print(app_name)
            elif line.startswith('Go to'):
                # Extracting offical download page(odp) link from line
                try:
                    odp = line.split("page](")[1].split(' "')[0]
                except IndexError:
                    odp = "None"
                print('Offical download link:', odp)
                # Extracting direct download link(ddl) from line
                try:
                    ddl = line.split("[here](")[1].split(' "')[0]
                except IndexError:
                    ddl = "None"
                print('Direct download link: ', ddl)
            elif line.startswith('Get it from'):
                try:
                    msv = line.split("store](")[1].split(' "')[0]
                except IndexError:
                    msv = "None"
                print('Microsoft Store: ', msv)
            elif line.startswith('    choco'):
                try:
                    choco_cmd = line.split("    ")[1].split("\n")[0]
                except IndexError:
                    choco_cmd = "None"
                print("Chocolatey CMD: ", choco_cmd)
