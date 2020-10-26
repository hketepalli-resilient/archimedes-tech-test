# Archimedes tech test

## Context

TODO: explain why it's close to our day-to-day job

## Task

We are giving you a JSON document, containing calls:

```json
{
  "data": [
    {
      "type": "call",
      "id": "2c4fae60-cf43-4f27-869e-a9ed8b0ca25b",
      "attributes": {
        "date": "2020-10-12T07:20:50.52Z",
        "riskScore": 0.431513435443,
        "cli": "+44123456789",
        "greenList": true,
        "redList": false
      }
    },
    {
      "type": "call",
      "id": "8f1b1354-26d2-4e16-9582-9156a0d9a5de",
      "attributes": {
        "date": "2019-10-12T07:20:50.52Z",
        "riskScore": 0.123444,
        "cli": "+44123456789",
        "greenList": false,
        "redList": true
      }
    },
    {
      "type": "call",
      "id": "db48da6c-6cb8-43d5-9637-5906b295fd20",
      "attributes": {
        "date": "2019-11-12T07:20:50.52Z",
        "riskScore": 0.1651346,
        "cli": "+44123456789",
        "greenList": false,
        "redList": true
      }
    }
  ]
}
```

TODO: explain the operators table:

```json
{
  "data": [
    {
      "type": "operator",
      "id": "2c4fae60-cf43-4f27-869e-a9ed8b0ca25b",
      "attributes": {
        "prefix": "0000",
        "operator": "Vodafone"
      }
    },
    {
      "type": "call",
      "id": "8f1b1354-26d2-4e16-9582-9156a0d9a5de",
      "attributes": {
        "prefix": "1000",
        "operator": "EE"
      }
    }
  ]
}
```

TODO: explain the fields for both sources of data

TODO: remove CLI concept - just write a program

We ask you to provide a CLI (command-line interface) to generate the following CSV:
```csv
id,date,cli,operator,riskScore
2c4fae60-cf43-4f27-869e-a9ed8b0ca25b,2020-10-12,+44123,Vodafone,0.0
8f1b1354-26d2-4e16-9582-9156a0d9a5de,2019-10-13,+44654,Unknown,1.0
db48da6c-6cb8-43d5-9637-5906b295fd20,2019-11-12,+99132,EE,0.3
911ea345-c58c-4688-bd9a-725263a1540b,2020-11-12,withheld,Unknown,0.9
```

The rules for the risk score calculation are:
- round up to 1 DP
- if on the green list, the value is 0.0
- if on the red list, the value is 1.0
- being on the green list has precedence on the red list

The target date format for the CSV is: `YYYY-MM-DD`

The optional parameters for the CLI are:
- filter by date range, e.g. only generate a CSV for the calls between the `2020-06-30` (inclusive) and `2020-09-15` (inclusive)
- sorting by date

Optional sortings:
- sorting by risk score
- sorting by operator

The names of the CLI and the CLI parameters are free of choice.

## Internal notes

- only few items
- operator out of range => "Unknown"
- no cli => rule put "Unknown" as operator and "withheld" as cli

## What we expect

TODO
- clean code
- test coverage
- simple README to explain how to run your program
- regular committing to see your thoughts process

## Input and output samples

TODO - links to JSON and CSV files

## Instructions to send the code source

You have one week to build your program, it should not take longer than 2 hours of your time.

Options at your convenience:
- send us the link of your git repo
- send us a zip git repo
- fork this repo as a private fork and give us the access
