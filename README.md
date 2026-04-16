# Machine Translation | Representation and Processing
### Group 2 - Parser Implementation

## About
This repository is a coding application of the **parsing** segment of the topic, which applies a bottom-up approach towards parsing a provided sentence/string.

This implementation follows the different mapping provided by the book, and also adds a few more vocabularies that can be tested. The goal here is to parse the provided string by tokenizing it and mapping it until we arrive to a final result of **'S'**!

## Files
This repository contains three main files:

```
dictionary.py       -> Contains the word categories, mapping, and vocabulary.
helpers.py          -> Contains the different methods such as tokenizers and mappers
main.py             -> Used to run the whole pipeline
```

## Test Cases
The following are test cases that we can use to check how the parser works.

```
1. users should clean the printer
2. the user should clean the printer
3. users clean printers
4. the printer stopped
5. the robot should navigate
6. an algorithm processed the data
```

