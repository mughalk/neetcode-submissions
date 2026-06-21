class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        # adding to stack
        # ex. ([{}])
        # add the character to the stack, and check if the current value matches the presently opened value in the stack. if it doesnt, ever
        # its INVALID, so return and fail quick
        # stack.append("[")
        # while stack is open and not empty and last letter in stack
        # well we also have to match the brackets somehow; map it ig?
        open_to_closed={"(":")","{":"}","[":"]"}
        # and obv u wanna map an OPENED bracket to a CLOSED one
        # since thats the correct order
        # []
        # ]
        # or ]]]
        # (])
        for c in s:
            if c in open_to_closed: # no
                stack.append(c) # stack=[]
            elif c in open_to_closed.values(): # no
                if stack:
                    stack_to_close=open_to_closed.get(stack[-1], "X") # stc="]"
                    if stack_to_close==c:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return stack==[]
                