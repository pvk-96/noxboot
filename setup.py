from setuptools import setup, find_packages

setup(
    name="noxboot",
    version="0.1.0",
    author="PVK",
    author_email="",
    description="A smart, minimal startup manager for Linux",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/noxboot",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer>=0.9.0",
        "rich>=13.0.0",
        "psutil>=5.9.0",
        "pyyaml>=6.0.0"
    ],
    entry_points={
        "console_scripts": [
            "noxboot=noxboot.cli:app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: MIT License",
        "Topic :: System :: Operating System :: Linux",
    ],
    python_requires=">=3.8",
)

