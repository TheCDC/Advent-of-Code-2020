from advent_of_code_2020.problem import ProblemBase


class Problem3(ProblemBase):
    def solve(self, input_string: str):
        lines = input_string.split("\n")
        num_valid_passwords = 0
        for line in lines:
            line_tokens = line.split(":")
            rules_token = line_tokens[0]
            rule_letter = rules_token.split(" ")[1]
            rule_range = [int(t) for t in rules_token.split(" ")[0].split("-")]

            content_token = line_tokens[1]
            pw_letter_count = content_token.count(rule_letter)
            if rule_range[0] <= pw_letter_count and pw_letter_count <= rule_range[1]:
                num_valid_passwords += 1
        return num_valid_passwords
