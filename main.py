import csv


def get_softwares_info(fname):
    """Returns (csv header, rows) of a fname."""
    while True:
        try:
            with open(fname, 'rt', newline='') as sl:
                soft_list = csv.reader(sl)
                header = next(soft_list)
                if len(header) < 3:
                    print(f'Less than 3 columns in {fname}')
                    print('Try another file')
                    continue
                return header, [row for row in soft_list]
        except FileNotFoundError:
            while True:
                try:
                    fname = input(
                        f"Couldn't locate {fname}\nEnter name of the file containing list of softwares\n:")
                except KeyboardInterrupt: exit('Abort!')


def get_app_disc(a_name, d_file):
    '''Returns discription of the name if found,other wise returns None'''
    try:
        with open(d_file, 'rt') as disc:
            app_disc = csv.reader(disc)
            next(app_disc)
            try:
                disc_dict = {disc[0]: disc[1] for disc in app_disc}
                try:
                    return disc_dict[a_name]
                except KeyError:
                    return None
            except IndexError:
                print(
                    f'The file containing apps discriptions has less then 2 colums.\nI looked on {d_file}')
                return None
    except FileNotFoundError:
        print(
            "Couldn't locate file containing apps discriptions.\nI looked for {d_file} file")
        return None


# Location files on local folder
file_softwares = 'main_applications.csv'
file_disc = 'discriptions_applications.csv'
file_markdown = 'README.md'

data = get_softwares_info(file_softwares)
# ['Application', ' Download Page Link', ' Direct Download Link']
header = data[0]
# contents = [['Firefox', 'https://www.mozilla.org/en-US/firefox/new/', 'https://download.mozilla.org/?product=firefox-stub&os=win&lang=en-US'],...]
contents = data[1]

'''Creating MARKDOWN file with collected information'''
defalut_lines = """
# List of Softwares and Tools that I use on a daily basis.
![](images/desktop.png "Softwares Icon Montage")
\n> This README is generated dynamically by main.py\n
"""
other_apps = list()
android_apps = list()
with open(file_markdown, 'wt') as md:
    md.write(defalut_lines)
    for info in contents:
        app_name = info[0]  # app_name is name of the application
        dpl = info[1]       # dpl is Download Page link
        ddl = info[2]       # ddl is Direct Download link

        # Seperating few apps
        if app_name.startswith('+ ') and app_name not in other_apps:
            other_apps.append(app_name)
            continue
        # Seprating android apps
        if app_name.startswith('- ') and app_name not in android_apps:
            android_apps.append(app_name)
            continue

        # Writing app name as H1
        md.write(f'# {app_name}\n')

        # Writing discriptions
        app_disc = get_app_disc(app_name, file_disc)
        if not app_disc is None:
            md.write(f'{app_disc}\n\n')

        # Writting download links info
        if ' OR ' in ddl:
            multi_ddl = ddl.split(' OR ')
            ddl = multi_ddl[0]
            ddl2 = multi_ddl[1]
        # print(ddl)
        wr_dpl = f'Go to [official download page]({dpl})'
        wr_ddl = f'Directly download for windows from [here]({ddl})'

        # When both Download Page link and Direct Download link is available
        if len(dpl) > 1 and len(ddl) > 1:
            md.write(f'- {wr_dpl} or {wr_ddl.lower()}.\n')
        else:
            if len(dpl) > 1:  # When only Direct Download link is available
                md.write(f'- {wr_dpl}.\n')
            if len(ddl) > 1:   # When only Download page link is available
                md.write(f'- {wr_ddl}.\n')
        if 'ddl2' in locals():
            if ddl2.startswith('https://www.microsoft') or ddl2.startswith('http://www.microsoft'):
                md.write(
                    f'\n- Install Microsoft store version from [here]({ddl2}).\n')
            del ddl2

    # Writing others apps
    if len(other_apps) > 1:
        md.write('## And few others\n')
        for app in other_apps:
            md.write(f'{app}\n')
    md.write('<hr>\n\n')

    # Writing android apps
    if len(android_apps) > 1:
        md.write('# Android Apps\n\n')
        for app in android_apps:
            md.write(f'{app}\n')
    md.write('<hr>\n')
