import argparse

import bills


def parse():
	"""Returns the command line arguments as an argparse.Namespace object."""
	parser = argparse.ArgumentParser(
		'BillCalculation',
		description=(
			'Simple tool for calculating the total and split costs of a bill.'
		))
	parser.add_argument(
		'-n',
		default=1,
		type=int,
		help='Number of parties to split the bill (default: 1)')
	parser.add_argument(
		'-a',
		'--add',
		nargs='+',
		action='extend',
		help='Add costs to the bill as [label] [cost] ...')
	parser.add_argument(
		'-d',
		'--delimiter',
		default='-',
		required=False,
		help='Symbol used to indicate multi-word labels (default: "-")')
	return parser.parse_args()


def main():
	"""Takes input from the command line and prints the bill."""
	args = parse()
	bill = bills.Bill(args.n, delimiter=args.delimiter)
	for i in range(0, len(args.add) - 1, 2):
		bill.add_cost(label=args.add[i], cost=float(args.add[i + 1]))
	bill.summarize()


if __name__ == '__main__':
	main()
