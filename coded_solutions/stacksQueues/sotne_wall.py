def solution(H) -> int:
    stack = []
    blocks = 0
    for h in H:
        while stack and stack[-1] > h:
            stack.pop()
        if not stack or stack[-1] < h:
            stack.append(h)
            blocks += 1
    return blocks