#!/bin/bash
#this script read an argument and create a python file 
#using the argument
fileName="$1"

touch $fileName && chmod +x $fileName
echo "#!/usr/bin/python3" >> $fileName
echo '"""' >> $fileName
echo "Designed by R. Chiu for the embeded system lecture." >> $fileName
echo "(r)2023  Universidad de Guadalajara MX" >> $fileName
echo "All the code comments where gerenerated automatically by chatGPT 3.5" >> $fileName
echo '"""' >> $fileName

