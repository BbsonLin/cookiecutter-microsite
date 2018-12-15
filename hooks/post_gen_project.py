import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.init_with_vue_cli }}' == 'y':
        subprocess.check_call('vue create .', shell=True)

    if '{{ cookiecutter.init_with_pipenv }}' == 'y':
        subprocess.check_output(['pipenv', 'install', '--dev', '--ignore-pipfile'])
