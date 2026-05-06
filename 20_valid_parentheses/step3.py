class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {"(": ")", "{": "}", "[": "]"}
        open_bracket = list()

        for bracket in s:
            if bracket in bracket_dict.keys():
                open_bracket.append(bracket)
            else:
                if not open_bracket or bracket_dict[open_bracket.pop()] != bracket:
                    return False
        return len(open_bracket) == 0
