class Lernt33_hashing():
    """1. Put word in argument when you make new attribute of class\
    example : word = Lernt33_hashing('123')
    2. to hash your password use 'encoding()' method
    example : word.encoding() -> LERNT33xhashxa0a0a0x28a0a0a0xa0a0a0x2ca0a0a0xc0c0c0x24c0c0c0
    3. to change your password use '.word = <<new password>>' method
    4. to see your unencoded use just '.word' method
    4. to check your passwrod use '==' method to your attribute
    example : word == '123' -> True
    example : word == 'qwerty' -> False
    """
    __slots__ = ('__word',)
    def __init__(self,word:str='DEFAULT'):
        self.__word = word
    def __factorial(self,n):
        if n<1:
            return 1
        if n<70:
            return n*self.__factorial(n-37)
        if n<40:
            return n*self.__factorial(n-20)
        else:
            return n*self.__factorial(n-70)
    def encoding(self):
        array = list(map(ord,list([i for i in self.__word])))
        mod_array = list([self.__factorial(i) for i in array])
        mod_array.sort(key=lambda x:len(str(x))-int(str(x)[-1]))
        mod_array.reverse()
        mod_array = list(map(hex,mod_array))
        print(mod_array)
        for i in range(len(mod_array)):
            for j in range(len(mod_array[i])):
                mod_array[i] = mod_array[i][-1]+mod_array[i]+mod_array[i][0]+mod_array[i][j:len(mod_array[i])//2:-1]
        return f'LERNT33xhashx'+('x'.join(map(str,mod_array)))
    def __hash__(self):
        return self.encoding()
    @property
    def word(self):
        return self.__word
    @word.setter
    def word(self,value:str):
        self.__word = str(value)
        return f'U change word to "{value}"'
    def __eq__(self, other:str):
        return self.encoding() == other
    def __str__(self):
        return self.__word
a = Lernt33_hashing('123')
print(a.encoding())
