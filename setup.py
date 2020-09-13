import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="funnel_clf",
    version="0.0.1",
    author="Driss Guessous",
    author_email="drisspguessous@gmail.com",
    description="A fastapi server for text classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'scikit-learn==0.23.1',
        'fastapi',
        'uvicorn',
        'gunicorn',
        'pandas',
    ],
    package_data={'funnel_clf': ['data/']}
)