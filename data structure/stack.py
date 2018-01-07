class stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[len(self.items)-1]
# only (,) in s1, check if it's a right parenthesis, check it s1 is balanced & after all pop, if it's empty
def parChecker(s1):
    st = stack()
    index = 0 
    balance = True
    while index <len(s1) and balance:
        if s1[index] == '(':
            st.push(s1[index])
        else:
            if st.isEmpty() == True:
                balance = False
            else:
                st.pop()
        index = index + 1
    if balance and st.isEmpty():
        return True
    else:
        return False
# （ 【 {
def match(p1, p2):
    l = '[{('
    r = ']})'   
    return l.index(p1) == r.index(p2)

def parChecker2(s2):
    index = 0 
    balance = True
    st2 = stack()
    while index < len(s2) and balance:
        if s2[index] in '([{':
            st2.push(s2[index])
        else:
            if st2.isEmpty():
                balance = False
            else:
                balance = match(st2.pop(), s2[index])
        index = index +1
    if balance and st2.isEmpty():
        return True
    else:
        return False
#using stack convert decimal into binary
def decimalTobinary(num):
    st = stack()
    while num >0:
        st.push(num%2)
        num = num //2
    binary = ''
    while not st.isEmpty():
        binary = binary + str(st.pop())
    return binary
# convert decimal to any base num
def baseConverter(num, base):
    digits = '0123456789ABCDEF'
    st = stack()
    while num >0:
        st.push(num%base)
        num = num //base
    result = ''
    while not st.isEmpty():
        result = result+ digits(st.pop())
    return result

