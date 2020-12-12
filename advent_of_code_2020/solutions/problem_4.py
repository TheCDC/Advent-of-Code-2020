from advent_of_code_2020.problem import ProblemBase


class Problem4(ProblemBase):
    def solve(self, input_string: str):
        lines = input_string.split("\n")
        num_valid_passwords = 0
        for line in lines:
            line_tokens = line.split(":")
            rules_token = line_tokens[0]
            rule_letter = rules_token.split(" ")[1]
            rule_range = [int(t) for t in rules_token.split(" ")[0].split("-")]

            content_token = (line_tokens[1].strip())
            num_position_matches = 0
            if rule_range[1] >= len(content_token):
                pass
                x = 2
            for index_to_check in rule_range:
                try:
                    if content_token[index_to_check-1] == rule_letter:
                        num_position_matches += 1
                except IndexError:
                    pass
            if num_position_matches == 1:
                num_valid_passwords += 1
            elif num_position_matches == 2:
                pass
            elif num_position_matches == 0:
                pass
        return num_valid_passwords
