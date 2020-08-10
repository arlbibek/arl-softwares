'''Download file using GetRequest using powershell and bat file'''

# input('Press RETURN to continue..')

# This code will extracts different links from file 'README.md'
dd_links = {}
odp_links = {}
msv_links = {}
choco_cmd = {}
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
                # print(app)
            elif line.startswith('Go to'):
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
            elif line.startswith('Get it from'):
                try:
                    msv = line.split("store](")[1].split(' "')[0]
                except IndexError:
                    msv = None
                msv_links[app] = msv
                # print('Microsoft Store: ', msv)
            elif line.startswith('    choco'):
                try:
                    choco = line.split("    ")[1].split("\n")[0]
                except IndexError:
                    choco = None
                choco_cmd[app] = choco
                # print("Chocolatey CMD: ", choco)


# for di in [dd_links, odp_links, msv_links, choco_cmd]:
#     for app, link in di.items():
#         print(str(app) + ': ' + str(link))
#     print()
for app, links in dd_links.items():
    if links is None:
        print('ODP :', odp_links[app])
        continue
    print(links)
