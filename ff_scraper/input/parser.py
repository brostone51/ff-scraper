def parse_inputs(input_file: str) -> list:
    """ Parses inputs from an input text file. Returns a list of the inputs.

    For an example of a well formatted inputs file, see inputs.sample.txt in the
    root of this repository. An input line should be three comma separated 
    values: (name,url,table_id). This can easily be used as input to the scaper
    and the output function to write your data to file for later processing.

    Args:
        input_file (str): The location of the input file relative to the caller

    Returns:
        list: A list of the input lines from the file. Each line should have:
        [name,url,table_id].
    """
    inputs = []
    with open(input_file) as file:
        for line in file:
            inputs.append(line.strip().split(','))
    return inputs
