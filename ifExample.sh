#!/bin/bash

# IF: check if new_folder exists
if [ -d "new_folder" ]; then
    mkdir if_folder
fi

# IF-ELSE: check if if_folder exists
if [ -d "if_folder" ]; then
    mkdir hyperionDev
else
    mkdir new-projects
fi
