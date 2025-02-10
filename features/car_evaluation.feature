Feature: Car valuation test
  Scenario Outline: Valuation comparision test
    Given the browser is open
    And Some personal details
    And An input file 'input.txt'
    When Searching for a reg number with output file name 'output.txt'
    Examples:
    | input_file | output_file |
    | input.txt  | output.txt  |
