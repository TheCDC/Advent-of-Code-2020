from advent_of_code_2020.problem import ProblemBase


class Day4Part1(ProblemBase):
    def solve(self, input_string: str):
        """
        First try!
        """
        required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
        num_valid_passports = 0
        passport_blocks = [' '.join(b.split())
                           for b in input_string.split("\n\n")]
        for block in passport_blocks:
            field_kv_tokens = block.split(" ")
            token_names_set = set(t.split(":")[0]
                                  for t in field_kv_tokens)
            if token_names_set >= required_fields:
                num_valid_passports += 1
        return num_valid_passports
