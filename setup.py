from setuptools import(
    setup,
    find_packages,
)


PACKAGE_REQUIRES=[
    'fastapi',
    'uvicorn',
    'uvloop',
    'SQLAlchemy',
    'sentry-sdk',
    'alembic',
    'Cython',
    'sphinx',
    'Click',
]


with open('README.md', 'r', encoding='utf-8') as f_readme:
    readme = f_readme.read()


setup(
    name='app',
    version='0.0.1',
    packages=find_packages(".", exclude=['tests',]),
    install_requires=PACKAGE_REQUIRES,
    author='Nguyen Khac Thanh',
    author_email='nguyenkhacthanh244@gmail.com',
    url="https://github.com/magiskboy/fastapi-webservice",
    description='',
    long_description=readme,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6.8',
    entry_points='''
        [console_scripts]
        appcli=app.cli:cli
    ''',
)
