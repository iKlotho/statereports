from statereport import StateReport
import sys
"""
Usage:
    python3 fetch_and_save.py -y 2016
"""
import argparse
parser = argparse.ArgumentParser(description='Fetch state reports')
parser._action_groups.pop()
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')
required.add_argument('-y', '--year', default='2017', type=str, help='Year of the report')
optional.add_argument('-s', '--sheeted', type=str, choices=('t','f'), help='Putting states in seperate sheets')
optional.add_argument('-t', '--to', type=str, choices=('xlsx', 'csv'), help='xlsx or csv')
args = parser.parse_args()
args.sheeted = False if args.sheeted == 'f' else True
args.to= '' if args.to == None else args.to


sp = StateReport(year=args.year)
sp.run()
sp.extract(sheeted=args.sheeted, to=args.to)
