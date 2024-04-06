# Problem Statement: 1249. Minimum Remove to Make Valid Parentheses

stack = []
        to_remove = set()
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if not stack:
                    to_remove.add(i)
                else:
                    stack.pop()
    
        to_remove.update(stack)

        result = ''
        for i, char in enumerate(s):
            if i not in to_remove:
                result += char
    
        return result
