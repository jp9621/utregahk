import os
import sys

def ahk(filename, code):
  scripts_folder_path = "scripts"
  filepath = os.path.join(scripts_folder_path, filename + ".ahk")
  with open(filepath, 'w') as f:
    f.write(code)


def write():
    unique_num = input("un: ")
    nick = input("nick: ")
    key = input("key: ")

    filename = f"{nick};{key}"

    code = f"""; {nick}
    {key}::Send, {unique_num}
    """
    
    ahk(filename, code)
    print(f"{filename}.ahk made")

    

print("hello annie :)")

while True:
    write()
    next = input("next [y/n]: ").lower()
    if (next == "y"):
        pass
    elif (next == "n"):
       sys.exit(0)
    else:
       break
    
