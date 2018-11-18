# weeeini
[![License](http://img.shields.io/:license-GPL3.0-blue.svg)](http://www.gnu.org/licenses/gpl-3.0.html)
![Version](https://img.shields.io/badge/version-1.0-green.svg)

Python script to add user to json file on owncloud.

## COMMAND SYNTAX

	usage: weeeini.py [-h] -n NAME [NAME ...] -s SURNAME [SURNAME ...] [-S SERIAL]
					  -t TELEGRAMID [-N NICKNAMES [NICKNAMES ...]] [-l LEVEL] [-V]
					  [-v]

	required arguments:
	  -n NAME [NAME ...], --name NAME [NAME ...]
							store the name of the user
	  -s SURNAME [SURNAME ...], --surname SURNAME [SURNAME ...]
							store the surname of the user
	  -t TELEGRAMID, --telegramID TELEGRAMID
							store the telegramID of the user

	optional arguments:
	  -h, --help            show this help message and exit
	  -S SERIAL, --serialID SERIAL
							store the serial ID of the user (by default 000000)
	  -N NICKNAMES [NICKNAMES ...], --nicknames NICKNAMES [NICKNAMES ...]
							store the nicknames of the user
	  -l LEVEL, --level LEVEL
							store the level of the user (type int, default=3)
	  -V, --version         show program's version number and exit
	  -v, --verbose         increase output verbosity, debug mode

## NOTES

- The -n NAME, -s SURNAME and -t TELEGRAMID parameters are required to add the user to the file.