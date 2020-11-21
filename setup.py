import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()
    
setuptools.setup(
    name = 'hltv_scraper-devonindustries',
    version = '0.0.2',
    author = 'Joshua Baker',
    author_email = 'jd.baker001@googlemail.com',
    description = 'A web scrper for hltv.org',
    long_description = long_description,
    long_description_context_type = 'text/markdown',
    url = 'https://github.com/devonindustries/hltv_scraper',
    packages = setuptools.find_packages(),
    classifiers =[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent'
        ],
        python_requires = '>=3.7.6')