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


def validate_height(s: str):
    units = ['in', 'cm']
    if not any(u in s for u in units):
        return False
    if 'cm' in s:
        num = int(s.split('cm')[0])
        return 150 <= num <= 193
    elif 'in' in s:
        num = int(s.split('in')[0])
        return 59 <= num <= 76
    return False


def validate_haircolor(s: str):
    legal_chars = set('0123456789abcdef')
    if len(s) != 7:
        return False
    if s[0] != '#':
        return False
    return set(s.split('#')[1]) <= legal_chars


validations = {
    'byr': lambda s: len(s) == 4 and (1920 <= int(s) <= 2002),
    'iyr': lambda s: len(s) == 4 and (2010 <= int(s) <= 2020),
    'eyr': lambda s: len(s) == 4 and (2020 <= int(s) <= 2030),
    'hgt': validate_height,
    'hcl': validate_haircolor,
    'ecl': lambda s: s in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
    'pid': lambda s: len(s) == 9 and s.isdigit()
}


class Day4Part2(ProblemBase):
    def solve(self, input_string: str):
        """
        First try!
        """
        required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
        num_valid_passports = 0
        passport_blocks = [' '.join(b.split())
                           for b in input_string.split("\n\n")]
        n = 0
        for block in passport_blocks:
            n += 1
            field_kv_tokens = block.split(" ")
            ks = set([kv.split(':')[0] for kv in field_kv_tokens])
            if not(ks >= required_fields):
                continue
            for kv in field_kv_tokens:
                k, v = kv.split(':')
                try:
                    if not validations[k](v):
                        break
                except KeyError:
                    pass
            else:
                num_valid_passports += 1

        return num_valid_passports
