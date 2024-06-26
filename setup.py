from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME= 'GUNJAN SARMA'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS= ['Streamlit']

setup
(
    name=SRC_REPO,
    version="0.0.1",
    author='Gunjan Sarma',
    author_email= 'gunjansarma2001@gmail.com'
    description="A small package for Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[SRC_REPO],
    python_requires=">=3.11",
    install_requires=LIST_OF_REQUIREMENTS,
)
