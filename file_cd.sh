#!/bin/bash

# Create 3 folders
mkdir A1 Bb2 Ccc3

# Enter A1
cd A1

# Create 3 subfolders inside A1
mkdir subA1 subA2 subA3

# Remove 2 folders from the parent directory
cd ..
rmdir Bb2 Ccc3
