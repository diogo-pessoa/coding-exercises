def solution(S: str) -> int:
    stack = []
    for s in S:
        if s == '(':
            stack.append(s)
        else:
            if not stack:
                return 0
            stack.pop()
    return 1 if not stack else 0