from setuptools import setup, find_packages

version = '0.0.4'

setup(
    name = 'isotoma.recipe.template',
    version = version,
    description = "Wrapper around Cheetah + JSON to provide simple buildout templating",
    long_description = open("README.rst").read() + "\n" + open("CHANGES.txt").read(),
    classifiers = [
        "Framework :: Buildout",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX",
        "License :: OSI Approved :: Apache Software License",

    ],
    keywords = "buildout template",
    author = "John Carr",
    author_email = "john.carr@isotoma.com",
    license="Apache Software License",
    packages = find_packages(exclude=['ez_setup']),
    package_data = {
        '': ['README.rst', 'CHANGES.txt'],
        'isotoma.recipe.apache': ['apache.cfg', 'apache-ssl.cfg']
    },
    namespace_packages = ['isotoma', 'isotoma.recipe'],
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'setuptools',
        'zc.buildout',
        'Cheetah',
        'simplejson'
    ],
    entry_points = {
        "zc.buildout": [
            "default = isotoma.recipe.template:Template",
        ]
    }
)

