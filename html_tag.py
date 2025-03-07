class HtmlTag:
    # _indent - глобальная переменная, хранящая отступ
    _indent = -1
    
    def __init__(self, tag, inline=False):
        """
        tag - имя тега
        inline - если True - тег выводится в одну строку.
        По умолчанию - False
        """
        self.tag = tag
        self.inline = inline
        
    def print(self, text):
        if not self.inline:
            print(f'{self._indent * "  "}  {text}')
        else:
            print(text, end="")
    
    def __enter__(self):
        self.increment_indent()
        end = "" if self.inline else "\n"
        print(f"{self._indent * '  '}<{self.tag}>", end=end)
        return self
    
    def __exit__(self, *args, **kwargs):
        if not self.inline:
            print(f"{self._indent * '  '}</{self.tag}>")
        else:
            print(f"</{self.tag}>")
        self.decrement_indent()
    
    @classmethod
    def increment_indent(cls):
        cls._indent += 1
        
    @classmethod
    def decrement_indent(cls):
        cls._indent -= 1
    
# TEST_1:
with HtmlTag('body') as _:
    with HtmlTag('h1') as header:
        header.print('Поколение Python')
    with HtmlTag('p') as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')

# TEST_2:
with HtmlTag('body') as _:
    with HtmlTag('h1', True) as header:
        header.print('Поколение Python')
    with HtmlTag('p', True) as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')