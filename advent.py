import argparse
import json
from importlib import import_module


def Main():
	parser = argparse.ArgumentParser()
	verboseGroup = parser.add_mutually_exclusive_group()

	# Add all the needed Arguments for the Program to run
	parser.add_argument("day", help="The number of the day you want to run the code for.", type=int)
	parser.add_argument("-o", "--output", help="Output result to a file.", action="store_true")

	# Prepares some -- maybe -- needed options in case I need to debug stuff
	verboseGroup.add_argument("-v", "--verbose", help="Will output some information in the console", action="store_true")
	verboseGroup.add_argument("-vv", "--veryverbose", help="Will output more information in the console", action="store_true")
	verboseGroup.add_argument("-vvv", "--veryveryverbose", help="Will output all the information in the console", action="store_true")

	args = parser.parse_args()

	verbosity = 0
	if args.verbose:
		verbosity = 1
	elif args.veryverbose:
		verbosity = 2
	elif args.veryveryverbose:
		verbosity = 3

	if verbosity == 3:
		print("===============================\n")
		print("Running the programm with following arguments: " + "\n")
		for arg in vars(args):
			print(arg, getattr(args, arg))
		print("\n===============================\n\n")

	if verbosity > 0:
		print("Loading Challenge day" +str(args.day) + " ....")

	challenge = import_module('challenge.day' + str(args.day))
	challenge.Run(args)

if __name__ == '__main__':
	Main()