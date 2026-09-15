#!/bin/bash

echo "Passwords in alphabetical order:"
sort passwords.txt


count=0

while read password
do
	echo "$password" > password_$count.txt
	count=$((count + 1))
done < passwords.txt
