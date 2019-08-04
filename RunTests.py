from unittest import TestCase
from Exceptions import EmptyInputFileException, WrongFormatInputFileException, MowerInitException
from Mower import Mower
from Execute import parse_and_execute_inputs


class Tests(TestCase):
    def test_working_example(self):
        file_path = 'tests/working_example_test.txt'
        expected_final_mower1 = Mower(1, 3, "N")
        expected_final_mower2 = Mower(5, 1, "E")
        result = parse_and_execute_inputs(file_path)
        self.assertEqual(result.mowers[0], expected_final_mower1)
        self.assertEqual(result.mowers[1], expected_final_mower2)

    def test_empty_file(self):
        file_path = 'tests/empty_file_test.txt'
        self.assertRaises(EmptyInputFileException, parse_and_execute_inputs, file_path)

    def test_out_of_bound(self):
        file_path = 'tests/out_of_bound_test.txt'
        expected_final_mower1 = Mower(0, 2, "W")
        result = parse_and_execute_inputs(file_path)
        self.assertEqual(result.mowers[0], expected_final_mower1)

    def test_missing_mower(self):
        file_path = 'tests/missing_mower_test.txt'
        self.assertRaises(WrongFormatInputFileException, parse_and_execute_inputs, file_path)

    def test_wrong_instructions(self):
        file_path = 'tests/wrong_instructions_test.txt'
        self.assertRaises(WrongFormatInputFileException, parse_and_execute_inputs, file_path)

    def test_wrong_mower_format_test(self):
        file_path = 'tests/wrong_mower_format_test.txt'
        self.assertRaises(ValueError, parse_and_execute_inputs, file_path)

    def test_mower_starting_out_of_bound(self):
        file_path = 'tests/mower_starting_out_of_bound_test.txt'
        self.assertRaises(MowerInitException, parse_and_execute_inputs, file_path)

    def test_wrong_orientation(self):
        file_path = 'tests/wrong_orientation_test.txt'
        self.assertRaises(WrongFormatInputFileException, parse_and_execute_inputs, file_path)
