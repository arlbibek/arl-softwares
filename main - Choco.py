'''Download file using GetRequest using powershell and bat file'''

# input('Press RETURN to continue..')

# This code will extracts different links from file 'README.md'

links = {}

dd_links = {}
odp_links = {}
msv_links = {}
choco_cmd = {}
num_apps = 0
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
                # print()
                app = line.split('# ')[1].split("\n")[0]
                num_apps += 1
                # print(app)
            if line.startswith('Go to'):
                # Extracting offical download page(odp) link from line
                try:
                    odp = line.split("page](")[1].split(' "')[0]
                except IndexError:
                    odp = None
                # print('Offical download link:', odp)
                odp_links[app] = odp
                # Extracting direct download link(ddl) from line
                try:
                    ddl = line.split("[here](")[1].split(' "')[0]
                except IndexError:
                    ddl = None
                dd_links[app] = ddl
                # print('App Name: ', app)
                # print('Direct download link: ', ddl)
            if line.startswith('Get it from'):
                try:
                    msv = line.split("store](")[1].split(' "')[0]
                except IndexError:
                    msv = None
                msv_links[app] = msv
                # print('Microsoft Store: ', msv)
            if line.startswith('    choco'):
                try:
                    choco = line.split("    ")[1].split("\n")[0]
                except IndexError:
                    choco = None
                choco_cmd[app] = choco
                # print("Chocolatey CMD: ", choco)

            links[app] = [odp, ddl, msv, choco]

print('The total number of apps is: ', num_apps)
i = 1

for app, cmd in choco_cmd.items():
    print(str(i) + ': ' + app)
    print('CMD: ' + cmd)
    i += 1
