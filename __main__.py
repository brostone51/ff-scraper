import sys

from ff_scraper.input import parser
from ff_scraper.output import output
from ff_scraper.scraper import scraper


def main(argv): 
    input_file = argv[0] if argv else './inputs.txt'
    print('Loading inputs from ' + input_file)
    inputs = parser.parse_inputs(input_file)

    for input in inputs:
        name, url, table_id = input
        headers, rows = scraper.scrape(url, table_id)
        output.write_output(name, [headers, *rows])

    print('Output files have been written to the current directory.')

if __name__ == '__main__':
    main(sys.argv[1:])
