from setuptools import setup, find_packages

setup(
    name="calculadora",
    version="1.0.0",
    description="Calculadora simples em Python com interface Tkinter",
    author="Desenvolvedor",
    author_email="dev@example.com",
    url="https://github.com/seu-repo/calculadora",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "pytest>=7.4.3",
        "pytest-cov>=4.1.0",
    ],
    entry_points={
        "console_scripts": [
            "calculadora=src.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
