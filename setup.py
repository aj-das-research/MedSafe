from setuptools import setup, find_packages

setup(
    name="MedSafe",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'GitPython',
    ],
    entry_points={
        'console_scripts': [
            'medsafe=src.analyzer:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for analyzing AI codebase compliance in healthcare",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aj-das-research/MedSafe",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)