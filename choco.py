def main2():
    windows = False
    links = {}
    with open('README.md', 'rt') as rm:
        for line in rm:
            if line.startswith('# Windows'):
                windows = True
            if line.startswith('### Others'):
                break
            if windows is True:
                # app_name = None
                if line.startswith('## '):
                    app_name = line.split('# ')[1].split("\n")[0]
                if line.startswith('Go to'):
                    # Extracting offical download page(odp) link from line
                    try:
                        odp = line.split("page](")[1].split(' "')[0]
                    except IndexError:
                        odp = None
                    # Extracting direct download link(ddl) from line
                    try:
                        ddl = line.split("[here](")[1].split(' "')[0]
                    except IndexError:
                        ddl = None
                    links[app_name] = [odp, ddl]
                if line.startswith('Get it from'):
                    try:
                        msv = line.split("store](")[1].split(' "')[0]
                    except IndexError:
                        msv = None
                else:
                    msv = None
                links[app_name].append(msv)
                if line.startswith('## Tor'):
                    break
    for k, link_list in links.items():
        print(k, ': ')
        for link in link_list:
            print(link)


def main():
    windows = False
    links = {}
    with open('README.md', 'rt') as rm:
        app_name = None
        got_app = False
        for line in rm:
            if line.startswith('# Windows'):
                windows = True
            if line.startswith('### Others'):
                break
            if windows is True:
                if line.startswith('## '):
                    app_name = line.split('# ')[1].split("\n")[0]
                    got_app = True
                if got_app is True:
                    try:
                        odp = line.split("page](")[1].split(' "')[0]
                    except IndexError:
                        odp = None
                    # Extracting direct download link(ddl) from line
                    try:
                        ddl = line.split("[here](")[1].split(' "')[0]
                    except IndexError:
                        ddl = None
                    links[app_name] = [odp, ddl]
                    try:
                        msv = line.split("store](")[1].split(' "')[0]
                    except IndexError:
                        msv = None
                    links[app_name].append(msv)
                    # print('Microsoft Store: ', msv)

        for k, link_list in links.items():
            print(k, ': ')
            for link in link_list:
                print(link)


main()
