from setuptools import setup

setup(
	name='stochastis',
	version='1.0.1',
	license="MIT",
	description='Convert Python code into music to hear algorithms',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	author='http://github.com/Pebaz',
	url='http://github.com/Pebaz/stochastis',
	py_modules=['main'],
    install_requires=['midiutil', 'pygame'],
    entry_points={
		'console_scripts' : [
			'stochastis=main:main'
		]
	}
)
