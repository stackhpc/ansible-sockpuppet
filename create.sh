#!/bin/bash

# To create a new role using this skeleton fill variables and run this script. Remove this file after role creation.

# This variable ideally should contain the name of an application which will be deployed with ansible role.
# Do not use whitespaces.
APPLICATION="sockpuppet"

# Port on which your application is listening
PORT="30000"

# Your name. Preferably your full name.
AUTHOR="Will Szumski"

rm -rf .git
rm README.md
mv ROLE_README.md README.md
mv "templates/application.service.j2" "templates/${APPLICATION}.service.j2"

find ./ -type f -exec sed -i "s/Will Szumski/$AUTHOR/g" {} \;
find ./ -type f -exec sed -i "s/sockpuppet/$APPLICATION/g" {} \;
find ./ -type f -exec sed -i "s/30000/$PORT/g" {} \;
