from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()
requirements = [
    "black",
    "folium",
    "pytz",
    "requests",
]
setup(
    name="atob_siddharth_assignment",
    version="1.0",
    description="Tracking fleets over time and routing to hub",
    long_description=readme,
    author="Siddharth Gupta",
    author_email="sid2harthgupta@gmail.com",
    url="",
    install_requires=requirements,
    license="MIT Licence 2021",
    zip_safe=False,
    keywords="samsara fleet location",
)
