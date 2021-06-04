# Description

A simple CLI tool for calculating the total and split costs of a bill.

# Usage

## Get help

```text

> python ./main.py -h
usage: BillCalculation [-h] [-n N] [-a ADD [ADD ...]] [-d DELIMITER]

Calculator for the total and split costs of a bill

optional arguments:
  -h, --help            show this help message and exit
  -n N                  Number of parties to split the bill (default: 1)
  -a ADD [ADD ...], --add ADD [ADD ...]
                        Add costs to the bill as [label] [cost] ...
  -d DELIMITER, --delimiter DELIMITER
                        Symbol used to indicate multi-word labels (default: "-")
```

## Calculate

```text
> python ./main.py -n 3 -a apples 12.99 pens 8.99 apple-pens 13.99
Apples       12.99    (4.33)
Pens         8.99     (3.00)
Apple pens   13.99    (4.66)
-----------------------------
Total        35.97    (11.99)
```
