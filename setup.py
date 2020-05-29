import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="local_reload",
    version="1.0.0",
    author="Alex Fischer",
    author_email="alex@quadrant.net",
    description="Django app for automatically identifying and reloading stale web pages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quadrant-newmedia/local_reload",
    packages=['local_reload'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["Django>=2.2,<3.1"],
    include_package_data=True,
)