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
            if c in open_to_closed: # opening bracket?
                stack.append(c) # stack=[]
            elif c in open_to_closed.values(): # closing bracket?
                if stack: # check for closing bracket using map with stack
                    # check what the expected character is that we need
                    # map the last value in the stack to an expected closing bracket
                    stack_to_close=open_to_closed.get(stack[-1], "X") # stc="]"
                    if stack_to_close==c:
                        stack.pop()
                    else:
                        # its a closing bracket, but its not closing in the LIFO order
                        # so an invalid bracket
                        return False
                else:
                    # if its a closing bracket and theres no stack, its invalid
                    # covering our bases since we'll already get false if we just have an opening bracket
                    # since it'll always add to the stack but nevr be popped
                    # but if its a closing brcket it'll never be added to the stack, and so its already in the wrong order
                    return False
        return stack==[]
        # 
                