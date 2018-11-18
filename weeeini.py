#!/usr/bin/env python3

"""
WEEEINI - Python script to add user to json file on owncloud.
Author: Dave
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import argparse
import collections
import os
import owncloud
import json
from requests.exceptions import ConnectionError
import sys

# get environment variables
OC_URL = os.environ.get('OC_URL')  # url of the OwnCloud server
OC_USER = os.environ.get('OC_USER')  # OwnCloud username
OC_PWD = os.environ.get('OC_PWD')  # OwnCloud password
USER_PATH = os.environ.get('USER_PATH') # path of the file with authorized users in OwnCloud (/folder/file.json)

def createUser(name, surname, username, serialID, telegramID, nicknames, level):
    """Used to create the dictionary"""
    user = collections.OrderedDict()
    user["name"] = name
    user["surname"] = surname
    user["username"] = username
    user["serialID"] = serialID
    user["telegramID"] = telegramID
    user["nicknames"] = nicknames
    user["level"] = level
    return user


def main():
    """main function of the weeeini"""
    parser = argparse.ArgumentParser(description='This is a python script to add user to json file on owncloud.\n Create by Dave.')

    # Optional and required parameters defined
    optional = parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')

    required.add_argument('-n', '--name', action="store", nargs='+', dest="name", required=True, help='store the name of the user')
    required.add_argument('-s', '--surname', action="store", nargs='+', dest="surname", required=True, help='store the surname of the user')
    optional.add_argument('-S', '--serialID', action="store", dest="serial", default="000000", help='store the serial ID of the user (by default 000000)')
    required.add_argument('-t', '--telegramID', action="store", dest="telegramID", required=True, help='store the telegramID of the user')
    optional.add_argument('-N', '--nicknames', action="append", nargs='+', dest="nicknames", default=[], help='store the nicknames of the user')
    optional.add_argument('-l', '--level', action="store", dest="level", type=int, default=3, help='store the level of the user (type int, default=3)')

    optional.add_argument('-V', '--version', action='version', version='%(prog)s v1.0')
    optional.add_argument('-v', '--verbose', action="store_true", dest="verbose", help="increase output verbosity, debug mode", )
    parser._action_groups.append(optional) 

    args = parser.parse_args()

    # Check if verbose is enabled
    verboseprint = print if args.verbose else lambda *a, **k: None

    # Create a dictionary of the new users
    name = ' '.join(args.name)
    surname = ' '.join(args.surname)
    username = ''.join(args.name).lower()
    username = username + '.'
    username = username+''.join(args.surname).lower()
    serialID = args.serial
    telegramID = args.telegramID
    nicknames = args.nicknames
    level = args.level
    user = createUser(name, surname, username, serialID, telegramID, nicknames, level)
    print("User to add: \n" +  json.dumps(user, indent=4))
    input("Press Enter to continue...")

    # Connect to Owncloud, download the user file and update it
    verboseprint("Connecting to Owncloud...")
    try:
        oc = owncloud.Client(OC_URL)
        verboseprint("Logging on Owncloud...")
        oc.login(OC_USER, OC_PWD)
        verboseprint("Downloading user file...")
        users = json.loads(oc.get_file_contents(USER_PATH).decode('utf-8'))["users"]
        users.append(user)
        new_users = collections.OrderedDict()
        new_users['users'] = users
        new_users = json.dumps(new_users,indent=4)
        verboseprint(new_users)
        oc.put_file_contents(USER_PATH, new_users.encode('utf-8'))
        print("File Updated.")
    except ConnectionError as e:
        print("Error connecting to Owncloud. No internet connection.")
        verboseprint(e)
    except:
        print("Unexpected error.")
        verboseprint(sys.exc_info()[0])

# call the main() 
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()