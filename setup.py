from setuptools import setup, find_packages

setup(
    name='plotly_assets',
    version='0.1.0',
    description='Assets for GridWatch Grafana',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'plotly_assets': ['plotly_style.yml'],
    },
)