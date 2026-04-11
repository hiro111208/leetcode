class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {"(": ")", "{": "}", "[": "]"}
        open_stack = list()

        for bracket in s:
            if bracket in bracket_dict.keys():
                open_stack.append(bracket)
            else:
                if not open_stack or bracket_dict[open_stack.pop()] != bracket:
                    return False
        return len(open_stack) == 0
