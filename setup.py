import setuptools
import os

from setuptools.command.install import install

from AutoROM import main

here = os.path.dirname(os.path.abspath(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

class InstallCommand(install):
    user_options = install.user_options + [
        ('accept-license', None, 'I accept the license')
    ]

    def initialize_options(self):
        install.initialize_options(self)
        self.accept_license = None

    def finalize_options(self):
        install.finalize_options(self)
        assert self.accept_license is None or self.accept_license == 1

    def run(self):
        install_dir = os.path.join(here, "AutoROM", "roms")
        if self.accept_license == 1:
            main(self.accept_license, install_dir, True)

        install.run(self)

setuptools.setup(
    name="AutoROM",
    version="0.3.0",
    author="PettingZoo Team",
    author_email="justinkterry@gmail.com",
    description="Automated installation of Atari ROMs for Gym/ALE-Py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PettingZoo-Team/AutoROM",
    keywords=["Reinforcement Learning", "game", "RL", "AI", "gym"],
    packages=setuptools.find_packages(),
    install_requires=[
        "click",
        "requests",
        "tqdm",
        'importlib-resources; python_version < "3.9"',
    ],
    entry_points={
        "console_scripts": ["AutoROM=AutoROM:cli"],
        "ale_py.roms": ["AutoROM=AutoROM.roms:export"]
    },
    zip_safe=False,
    cmdclass={"install": InstallCommand},
    package_data={
        "AutoROM.roms": ["*.bin"]
    },
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
