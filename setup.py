import io
import re

from setuptools import setup


with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

with io.open('interpreter/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search('__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='SL-Interpreter',
    version=version,
    description='A small and light interpreter',
    long_description=readme,
    url='https://github.com/jun0jang/SL-interpreter',
    author='jun young Jang',
    author_email='wnsdud3256@gmail.com',
    packages=['interpreter'],
    zip_safe=False,
)
