import os

try:
    os.mkdir(os.path.join(os.getcwd(),'Uploads'))
except FileExistsError:
    pass