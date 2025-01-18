from setuptools import setup, find_packages

setup(
    name="pola-lang",
    version="1.0.0",
    author="Syed Abdul-Rehman",
    author_email="abdulrehman1255211@gmail.com",
    description="A custom programming language interpreter for .pola files.",
    packages=find_packages(),
    py_modules=["pola", "interpreter", "custom_functions", "keyword_map"],
    entry_points={
        "console_scripts": [
            "pola=pola:main",  # Maps the `pola` command to the `main` function in `pola.py`
        ]
    },
    install_requires=[],  # Add any Python dependencies here, if needed
    python_requires=">=3.8",
)
