from setuptools import setup, find_packages

setup(
    name='abstract_test_package',
    version='0.0.1',
    author='putkoff',
    author_email='partners@abstractendeavors.com',
    description='abstract_test_package is a Python package that facilitates testing with abstract scenarios. Utilizing PyTest, it offers extra utilities to streamline the creation and execution of abstract tests.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/abstract_endeavors/abstract_test_package',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        # Add your project's requirements here, e.g.,
        # 'numpy>=1.22.0',
        # 'pandas>=1.3.0',
    ],
    entry_points={
        'console_scripts': [
            'abstract_test_package=abstract_test_package.main:main',
        ],
    },
)
