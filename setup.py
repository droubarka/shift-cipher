from setuptools import setup, find_packages

setup(
	name='shiftcipher',
	version='1.0.1',
	packages=find_packages(),
	author='Mohamed A. Oubarka',
	author_email='droubarka@gmail.com',
	url='https://github.com/droubarka/shift-cipher.git',
	description='Shift-Cipher is a traditional encryption method used to encrypt texts.',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
	],
	keywords=(
		'cryptography substitution shift caesar cipher'
		'algorithm security cybersecurity'
		'code encryption decryption key'),
	license='MIT License',
	install_requires=[],
	zip_safe=False
)
