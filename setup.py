import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "1.0.0"

REPO_NAME = "titanic-automate"
AUTHOR_USER_NAME = "utkarsh-iitbhu"
SRC_REPO = "titanic"
AUTHOR_EMAIL = "utkarsh.bhuiit@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Titanic classifier in modular coding",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages=setuptools.find_packages(),  # Automatically find all packages
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
)
