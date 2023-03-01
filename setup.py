import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pylynkz',
    version='0.0.1',
    author='Alexandre Desgagné',
    author_email='alexd@lynkz.ca',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mike-huls/toolbox',
    license='MIT',
    packages=['pylynkz'],
    install_requires=['requests', 'termcolor', 'colorama'],
)
