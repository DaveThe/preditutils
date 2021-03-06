import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='preditutils',
    version='0.1',
    author="Davide Tresoldi",
    author_email="davide.tresoldi@predit.it",
    description="GCP Predit utility package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
