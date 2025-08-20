from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="AgentForge",
    version="0.1",
    author="Ridham Puri",
    packages=find_packages(),
    install_requires = requirements,
)