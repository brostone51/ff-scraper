def write_output(file_name: str, outputs: list) -> None:
    """ Writes each row in :outputs to :file_name.csv as its own line

    Will write the CSV of each row of outputs to the provided file name.

    Args
        file_name (str): The name you want the csv file to have
        outputs (list): A list of lists to be written as comma separated values
            per line to file_name
    
    Returns
        None
    """
    with open(file_name + '.csv', 'w') as file:
        for output in outputs:
            if output:
                file.write(','.join(output) + '\n')
