#!/bin/bash

read -p "Download paper template as well?" download
if [[ "$download" =~ ^[Yy]$ ]]
then
  cookiecutter https://github.com/johnnygreco/cookiecutter-aasdraft
fi
