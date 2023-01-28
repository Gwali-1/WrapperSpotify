from setuptools import setup, find_packages

setup(
    name="WrapperSpotify",
    version="1.0.3",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    include_package_data=True,
    author="Matthew Gwalisam",
    author_email="gwalisam37@gmail.com",
    description="A lightweight python client for the spotify",
    long_description=open('README.md').read(),
    url='https://github.com/Gwali-1/spotifyclient.git',
    long_description_content_type='text/markdown',
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)