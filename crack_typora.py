import fnmatch
import os
import sys
import winreg
import re


def crack():
    root_path = find_install_path_win("Typora")
    if not root_path:
        print("Install path not found.")
        sys.exit(1)

    print(f"Find path {root_path}")

    path = os.path.join(root_path, r"resources\page-dist\static\js")
    file_paths = find_files_with_pattern(path, r"LicenseIndex.*.*.chunk.js")
    for path in file_paths:
        replace_in_file(path, False, r'e.hasActivated="true"==e.hasActivated', r'e.hasActivated="true"=="true"')

    path = os.path.join(root_path, r"resources\page-dist")
    file_paths = find_files_with_pattern(path, r"license.html")
    for path in file_paths:
        replace_in_file(path, False,
                        r'</body></html>',
                        r'</body><script>window.onload=function(){setTimeout(()=>{window.close();},5);}</script></html>')

    path = os.path.join(root_path, r"resources\locales")
    file_paths = find_files_with_pattern(path, r"Panel.json")
    for path in file_paths:
        replace_in_file(path, True, u'"UNREGISTERED":"[^"]*?"', u'')

    print("OK")
    input()


def find_install_path_win(software_name):
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
    i = 0
    while True:
        try:
            subkey_name = winreg.EnumKey(key, i)
            subkey = winreg.OpenKey(key, subkey_name)
            try:
                display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                if software_name.lower() in display_name.lower():
                    try:
                        install_location = winreg.QueryValueEx(subkey, "InstallLocation")[0]
                        return install_location
                    except FileNotFoundError:
                        print(f"Found {display_name}, but InstallLocation is not set.")
            except FileNotFoundError:
                pass
            winreg.CloseKey(subkey)
            i += 1
        except OSError:
            break
    return None


def find_files_with_pattern(start_dir, pattern):
    file_paths = []
    for root, dirs, files in os.walk(start_dir):
        for file_name in files:
            if fnmatch.fnmatch(file_name, pattern):
                file_paths.append(os.path.join(root, file_name))
    return file_paths


def replace_in_file(file_path, use_regex, search_string, replace_string):
    with open(file_path, 'r+', encoding='utf-8') as file:
        content = file.read()
        if not use_regex:
            new_content = content.replace(search_string, replace_string)
        else:
            new_content = re.sub(search_string, replace_string, content)
        file.seek(0)
        file.write(new_content)
        file.truncate()
    print(f"Patch file {file_path}")


if __name__ == '__main__':
    crack()
