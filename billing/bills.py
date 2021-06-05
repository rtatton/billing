import decimal
from typing import Optional

_SPACE = '   '


class Bill:
	"""A collection of costs to split.

	Attributes:
		n: Number of ways to split the bill.
		labels: List of labels for each cost.
		costs: List of each cost.
		per: List of cost for each split of the bill.
		delimiter: A string to split multi-word labels.
	"""
	__slots__ = ('n', 'labels', 'costs', 'per', 'delimiter')

	def __init__(self, n: int, delimiter: Optional[str] = None):
		self.n = n
		self.labels = []
		self.costs = []
		self.per = []
		self.delimiter = delimiter

	def add_cost(self, label: str, cost: float):
		"""Adds a cost to the bill."""
		if self.delimiter is not None:
			label = ' '.join(label.split(self.delimiter))
		self.labels.append(label)
		self.costs.append(cost := decimal.Decimal(str(cost)))
		self.per.append(cost / self.n)

	def summarize(self):
		"""Calculates the bill and prints all item and total costs."""
		self.add_cost('total', sum(self.costs))
		longest_label = self._longest_string(*self.labels)
		longest_cost = self._longest_string(*map(str, self.costs))
		lines = [
			self._format_item(label, cost, per, longest_label, longest_cost)
			for label, cost, per in zip(self.labels, self.costs, self.per)]
		for line in lines[:-1]:
			print(line)
		print('-' * self._longest_string(*lines))
		print(lines[-1])

	def _format_item(
			self,
			label: str,
			cost: decimal.Decimal,
			per: decimal.Decimal,
			longest_label: int,
			longest_cost: int):
		label = label.lower().capitalize()
		cost, per = self._money_format(cost), self._money_format(per)
		from_label = ' ' * (longest_label - len(label))
		from_cost = ' ' * (longest_cost - len(str(cost)) + 1)
		return f"{label}{from_label}{_SPACE}{cost}{from_cost}{_SPACE}({per})"

	@staticmethod
	def _money_format(
			value: decimal.Decimal,
			places: int = 2,
			curr: str = '',
			sep: str = ',',
			dp: str = '.',
			pos: str = '',
			neg: str = '-',
			trail_neg: str = ''):
		"""Convert Decimal to a money formatted string.

		References:
			https://docs.python.org/3/library/decimal.html#recipes

		Args:
			value: Decimal to format as a monetary amount.
			places: Number of places after the decimal point.
			curr: Currency symbol before the sign (may be blank).
			sep: Grouping separator (comma, period, space, or blank).
			dp: Decimal point indicator (comma or period). Only specify as
				blank when places is zero.
			pos: Sign for positive numbers: '+', space or blank.
			neg: Sign for negative numbers: '-', '(', space or blank.
			trail_neg: Trailing minus indicator:  '-', ')', space or blank.
		"""
		q = decimal.Decimal(10) ** -places  # 2 places --> '0.01'
		sign, digits, exp = value.quantize(q).as_tuple()
		result = []
		digits = list(map(str, digits))
		build, next_ = result.append, digits.pop
		if sign:
			build(trail_neg)
		for _ in range(places):
			build(next_() if digits else '0')
		if places:
			build(dp)
		if not digits:
			build('0')
		i = 0
		while digits:
			build(next_())
			i += 1
			if i == 3 and digits:
				i = 0
				build(sep)
		build(curr)
		build(neg if sign else pos)
		return ''.join(reversed(result))

	@staticmethod
	def _longest_string(*strings: str) -> int:
		return max(map(len, strings))
