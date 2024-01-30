import os
import shutil
import tkinter as tk


def del_content(folder: str):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def clean():
    root.withdraw()

    print('cleaning')
    try:
        print('clear user temp')
        del_content(f'{os.environ["tmp"]}')
        print('completed')
    except Exception:
        print('pass')
    try:
        print('clear system temp')
        del_content(f'{os.environ["SystemRoot"]}\\temp')
        print('completed')
    except Exception:
        print('pass')

    try:
        print('clear internet cache')
        del_content(f'{os.environ["LOCALAPPDATA"]}\\Microsoft\\Windows\\INetCache\\IE')
        print('completed')
    except Exception:
        print('pass')
    try:
        print('clear recycle bin')
        del_content(f'{os.environ["SystemDrive"]}\\$Recycle.Bin')
        print('completed')
    except Exception:
        print('pass')

    try:
        print('cleanmgr')
        os.system('start /wait cleanmgr /verylowdisk')
        print('completed')
    except Exception:
        print('pass')

    try:
        print('ccleaner')
        os.system('start /wait CCleaner.exe /AUTO')
        print('completed')
    except Exception:
        print('pass')

    print('cleaning completed')
    root.deiconify()


root = tk.Tk()
text = tk.Label(root, text='Clean master 1.0')
button = tk.Button(root, text='Clean', command=clean)

text.pack(anchor='n')
button.pack(anchor='w', side='right')

root.mainloop()
