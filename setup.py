from setuptools import setup, find_packages

setup(
    name="hue_shift",
    version="1.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            # If you want to create any executable scripts
        ],
    },
    author="EchterAlsFake | Johannes Habel",
    author_email="EchterAlsFake@proton.me",
    description="A simple script for generating ~16 million colors without dependencies",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license="LGPLv3",
    url="https://github.com/EchterAlsFake/hue_shift",
    classifiers=[
        # Classifiers help users find your project on PyPI
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python",
    ],
)
