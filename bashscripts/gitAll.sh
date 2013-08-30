#!/bin/bash
# this small bash script will run git pull on all current sub directories


for f in ~/repos/*
do
	cd $f && git pull --all && git fetch --all -p && cd ..
done
