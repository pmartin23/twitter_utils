import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="twitter_utils",
    version="0.0.1",
    author="Paige Martin",
    author_email="paige.newman@mq.edu.au",
    description="Tools for retrieving data from Twitter",
    long_description=long_description,
    url="https://github.com/pmartin23/twitter_utils",
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
          'tweepy',
      ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
    ],
)
