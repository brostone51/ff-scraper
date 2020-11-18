def write_output(file_name: str, outputs: list) -> None:
    with open(file_name + '.csv', 'w') as file:
        for output in outputs:
            if output:
                file.write(','.join(output) + '\n')
