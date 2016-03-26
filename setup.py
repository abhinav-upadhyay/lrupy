from distutils.core import setup

setup(
    name = "lrupy",
    version = "0.1",
    py_modules=['lrupy'],
    description = "A simpley (LRU) cache implementation",
    author = "Abhinav Upadhyay",
    author_email = "er.+abhinav.+updadhyay@gmail.com",
    url = "https://github.com/abhinav-upadhyay/lrupy",
    classifiers = [
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: BSD",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description=open('README.md').read())

