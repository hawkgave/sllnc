class PrefixConverter:
    def __init__(self):
        self.stackList = ['?']
        self.size = 0

    def push(self,data):
        self.stackList.append(data)

    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"

    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
        return data
    
    
    
    def cekValidExpression(self,expression):
        pass

class konversi:
    
    def prioritas(self, text) :
        if (text == "+" or text == "-") :
            return 1
            
        elif (text == "*" or text == "/") :
            return 2

        elif (text == "^") :
            return 3

    def operator(self,text):
        if(self.prioritas(text) != -1):
            return True
        return False

    def infixToPrefix(self,expression):
        size = len(expression)
        s = PrefixConverter()
        op = PrefixConverter()
        bantu = ""
        op1 = ""
        op2 = ""
        isValid = True
        i = 0
        while (i < size and isValid) :
            if (expression[i] == '(') :
                op.push("(")

            elif (self.operator(str(expression[i])) == True) :
                while (s.size > 1 and self.prioritas(
                       str(expression[i])) <= self.prioritas(op.peek())) :
                    op1 = s.pop()
                    op2 = s.pop()
                    bantu = op.pop() + op2 + op1
                    s.push(bantu)
				
                bantu = str(expression[i])
                op.push(bantu)

            elif (expression[i] == ')') :
                if (s.size > 1) :
                    while (s.size > 1 and not op.peek() == "(") :
                        op1 = s.pop()
                        op2 = s.pop()
                        bantu = op.pop() + op2 + op1
                        s.push(bantu)
					
                    op.pop()

                else :
                    isValid = False
				
            elif ((expression[i] >= '0'
					and expression[i] <= '9') or(expression[i] >= 'a'
					and expression[i] <= 'z') or(expression[i] >= 'A'
					and expression[i] <= 'Z')) :
                bantu = str(expression[i])
                s.push(bantu)

            else :
                isValid = False
			
            i += 1
		
        if (isValid == False) :
            print("Expresi INfix yang ada masukkan tidak Valid ")
        else :
            print(" Expresi Prefix-nya adalah  : ", s.pop())


expresi1 = PrefixConverter()
print(expresi1.in("1+2+3*4/2-1"))
print(expresi1.infixToPrefix("A * (B + C) / D"))
print(expresi1.infixToPrefix("(1+2)*3"))
print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))

