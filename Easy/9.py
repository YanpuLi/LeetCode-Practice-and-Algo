class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rawNum = s.split()
        state = {'e/E':[], '.':[]}
        hasNum = False
        if len(rawNum) != 1:
            return False
        if rawNum[0].isdigit():
            return True
        
        if rawNum[0][0] == '+' or rawNum[0][0] == '-':
                rawNum[0] = rawNum[0][1:]
                
        for i in range(len(rawNum[0])):
            if rawNum[0][i] == 'e' or rawNum[0][i] == 'E':
                state['e/E'].append(i)
            elif rawNum[0][i] == '.':
                state['.'].append(i)
            elif rawNum[0][i] == '+' or rawNum[0][i] == '-':
                    return False
            elif rawNum[0][i] in '0123456789':
                hasNum = True
                continue
            else:
                return False
        # no digits in string
        if hasNum == False:
                return False
        if len(state['.']) >1 or len(state['e/E'])>1:
            return False
        if len(state['e/E'])==1:
            if state['e/E'][0]==0 or  state['e/E'][0]== len(rawNum[0]) -1:
                return False
        if len(state['.']) ==1:
            if state['.'][0]==0:
                if not(rawNum[0][1].isdigit()):
                    return False
            elif state['.'][0] == len(rawNum[0])-1:
                if not(rawNum[0][len(rawNum[0])-2].isdigit()):
                    return False
            else:
                if not(rawNum[0][state['.'][0]-1].isdigit() or rawNum[0][state['.'][0]+1].isdigit()):
                    return False
        if len(state['e/E'])==1 and len(state['.']) ==1:
            if state['e/E'][0] <state['.'][0]:
                return False
            
        return True     

obj = Solution()
obj.isNumber(" 005047e+6")

# Time:  O(n)
# Space: O(1)
#
# Validate if a given string is numeric.
# 
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# Note: It is intended for the problem statement to be ambiguous.
# You should gather all requirements up front before implementing one.
#

class InputType:
    INVALID    = 0
    SPACE      = 1
    SIGN       = 2
    DIGIT      = 3
    DOT        = 4
    EXPONENT   = 5


# regular expression: "^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$"
# automata: http://images.cnitblog.com/i/627993/201405/012016243309923.png
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        transition_table = [[-1,  0,  3,  1,  2, -1],     # next states for state 0
                            [-1,  8, -1,  1,  4,  5],     # next states for state 1
                            [-1, -1, -1,  4, -1, -1],     # next states for state 2
                            [-1, -1, -1,  1,  2, -1],     # next states for state 3
                            [-1,  8, -1,  4, -1,  5],     # next states for state 4
                            [-1, -1,  6,  7, -1, -1],     # next states for state 5
                            [-1, -1, -1,  7, -1, -1],     # next states for state 6
                            [-1,  8, -1,  7, -1, -1],     # next states for state 7
                            [-1,  8, -1, -1, -1, -1]]     # next states for state 8
        
        state = 0
        for char in s:
            inputType = InputType.INVALID
            if char.isspace():
                inputType = InputType.SPACE;
            elif char == '+' or char == '-':
                inputType = InputType.SIGN
            elif char.isdigit():
                inputType = InputType.DIGIT
            elif char == '.':
                inputType = InputType.DOT
            elif char == 'e' or char == 'E':
                inputType = InputType.EXPONENT;
                
            state = transition_table[state][inputType];
            
            if state == -1:
                return False;
        
        return state == 1 or state == 4 or state == 7 or state == 8


class Solution2(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        return bool(re.match("^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$", s))


if __name__ == "__main__":
    print Solution().isNumber(" 0e+6 ")
    print Solution().isNumber("abc")
    print Solution().isNumber("1 a")
    print Solution().isNumber("2e10")