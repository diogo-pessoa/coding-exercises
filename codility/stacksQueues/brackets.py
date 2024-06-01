def solution(S: str) -> int:
    """
    Conditions for nested brackets:
    S is Empty
    S has the form (U) or [U] or {U} where U is a properly nested string
    S has the form VW where V and W are properly nested strings
    The String "{[()()]}" os properly nested but "([)()]" is not
    :param S:
    :return: binary 1 if S is properly nested, 0 otherwise
    """
    # stack
    stack = []
    # dictionary for matching brackets
    brackets = {')': '(', '}': '{', ']': '['}
    for s in S:
        if s in brackets.values():
            stack.append(s)
        else:
            if not stack:
                return 0
            if stack[-1] == brackets[s]:
                stack.pop()
            else:
                return 0
    return 1 if not stack else 0
