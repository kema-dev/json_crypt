<div id="top"></div>
<!-- PROJECT LOGO -->
<p align=center>
  <img alt="Project's status" src="https://img.shields.io/badge/Status-Finished-brightgreen">
  <img alt="Project's primary language" src="https://img.shields.io/badge/Language-Python-blue">
  <img alt="Project's focus" src="https://img.shields.io/badge/Focus-Data%20encryption-blue">
</p>

<br />
<div align="center">
    <img src="assets/logo_json_crypt.png" alt="Docker logo" style="height:30vh">
</div>

<!-- ABOUT THE PROJECT -->
## About The Project
<!-- TODO Put images / gifs from the project here -->

**json_crypt** is a simple tool to encrypt and decrypt the values of JSON files, thus keeping the ability to search for specific key in the file and decrypt its value on-the-fly. It uses AES-256 in CBC mode to encrypt the data, with a given password as the key.

### Built With

* <a href="https://www.python.org/" target="_blank" title="Python's website">Python</a>
* <a href="https://pypi.org/project/pycryptodome/" target="_blank" title="pycryptodome's page">pycryptodome</a>
* <a href="https://regex101.com/r/SodelR/1" target="_blank" title="regex demo">regex</a>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* [Python 3](https://www.python.org/downloads/)
* [pycryptodome](https://pypi.org/project/pycryptodome/)

### Installation

1. Clone the repo

```sh
git clone https://github.com/kema-dev/json_crypt.git
```

2. Go to repository's folder

```sh
cd json_crypt
```

<!-- USAGE EXAMPLES -->
## Usage

1. Simply execute the script

```sh
python src/json_encrypt.py
```

<!-- ROADMAP -->
## Roadmap

Just found [Mozilla's work](https://github.com/mozilla/sops) that does pretty much the same job, thus I don't plan to work on this project anymore.

Initial roadmap is available [here](roadmap.md).

<!-- CONTACT -->
## Contact

kema-dev - [GitHub](https://github.com/kema-dev)

## Acknowledgments

* [Img Shields](https://shields.io)
* [README.MD-Template](https://github.com/othneildrew/Best-README-Template)
