from Execute import parse_and_execute_inputs


# Main function - Parsing the instructions file and printing the final positions of the mowers
def main():
    # File path for the input instructions
    file_path = 'input.txt'
    print(parse_and_execute_inputs(file_path))


main()