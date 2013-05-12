#!/bin/bash
pathToLive=/usr/share/nginx
pathToRepo=~/repos/webSite

echo Clearing backup and repo copy folder...
sudo rm -rf $pathToLive/htmlBackup/*
sudo rm -rf $pathRoLive/repoCopy/*

echo Copying repo files to ...nginx/repoCopy
sudo cp -rfv $pathToRepo/* $pathToLive/repoCopy/

echo Moving live content to html backup
sudo mv -fv $pathToLive/html/* $pathToLive/htmlBackup/

echo Moving updated files to live content
sudo cp -rfv $pathToLive/repoCopy/* $pathToLive/html/

echo ping kocsen.com
