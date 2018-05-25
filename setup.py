from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    author='Anne Pietsch, Philip Schildkamp',
    author_email='a.pietsch@uni-koeln.de, philip.schildkamp@uni-koeln.de',
    description='CLI/GUI tools to measure agreement between annotations',
    license=license,
    long_description=readme,
    name='annogree',
    packages=find_packages(exclude=('tests', 'docs')),
    url='https://github.com/schlusslicht/annogree',
    version='0.0.1'
)
