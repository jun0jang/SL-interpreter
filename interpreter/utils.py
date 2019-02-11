import os


def fileopen(filename):
    if not filename.endswith('.sl'):
        raise Exception('파일 확장자가 올바르지 않습니다.')
    if not os.path.isfile(filename):
        raise Exception('해당 파일을 찾을 수 없습니다.')

    with open(filename, encoding='utf_8') as f:
        return f.read().splitlines()
