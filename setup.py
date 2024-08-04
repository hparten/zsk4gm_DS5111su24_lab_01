from setuptools import setup, find_packages

# Read the contents of requirements.txt
def parse_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines() if line.strip() and not line.startswith('#')]

# Parse the requirements
install_requires = parse_requirements('requirements.txt')

setup(
    name="zsk4gm",
    version="0.1.0", 
    description="A small example package.",
    author="Hallie Parten",
    author_email="zsk4gm@virginia.edu",  
    url="https://github.com/hparten/zsk4gm_DS5111su24_lab_01",  
    packages=find_packages(where='src'),
    package_dir={'': 'src'}, 
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'my-script=src/zsk4gm.process_text:clean_text',  
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8', 
)
