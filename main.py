# main.py
from data import sname, reponame

def main(sname):
    print(f'Hello, {sname}!')


if __name__ == '__main__':
    main(sname)
    print(f'{sname}: {reponame}')
