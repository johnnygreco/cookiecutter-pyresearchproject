# cookiecutter-pyresearchproject

Boilerplate for [cookiecutter](https://github.com/audreyr/cookiecutter)
for a python-centered research project

Do `cookiecutter https://github.com/smoh/cookiecutter-pyresearchproject`,
and you are prompted to give project name, etc.

Creates the following files and directories:

```sh
$ tree \{\{cookiecutter.project_name\}\}
{{cookiecutter.project_name}}
├── README.md
├── docs
│   └── README.md
├── environment.yml
├── scripts
│   └── README.md
├── setup.py
└── {{cookiecutter.project_name}}
    └── __init__.py
```
