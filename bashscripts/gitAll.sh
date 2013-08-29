#!/bin/bash
# this small bash script will run git pull on all current sub directories


for f in ~/repos/*
do
	cd $f && git pull && git fetch --all && cd ..
done
