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
    author_email="zsk4gm@virgnia.edu",  
    url="https://github.com/hparten/zsk4gm_DS5111su24_lab_01"  
    packages=find_packages(), 
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'my-script=zsk4gm:process_text',  # Replace with your module and function
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT',
        'Operating System :: Darwin',
    ],
    python_requires='>=3.8',  # Adjust based on your project's Python version requirements
)
