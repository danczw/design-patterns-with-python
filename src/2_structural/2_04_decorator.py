# decorator method - structural design pattern
#   allows to dynamically attach new behaviors to objects without changing their
#   implementation by placing these objects inside the wrapper objects that
#   contains the behaviors

class WrittenText:
    def __init__(self, text: str):
        self._text = text

    def render(self) -> str:
        return self._text

class UnderlineWrapper(WrittenText):
    def __init__(self, wrapped):
        self._wrapped = wrapped
    
    def render(self) -> str:
        return f'<u>{self._wrapped.render()}</u>'


# create wrapper
# - easy to divide a monolithic class which implements many possible variants
#   of behavior into several classes using the Decorator method
# - add or remove the responsibilities from an object at runtime
class ItalicWrapper(WrittenText):
    def __init__(self, wrapped: str):
        self._wrapped = wrapped

    def render(self):
        return f'<i>{self._wrapped.render()}</i>'

class BoldWrapper(WrittenText):
    def __init__(self, wrapped: str):
        self._wrapped = wrapped

    def render(self) -> str:
        return f'<b>{self._wrapped.render()}</b>'


# run method
if __name__ == '__main__':
    before_gfg = WrittenText('hello world!')
    after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))

    print(f'before : {before_gfg.render()}')
    print(f'after : {after_gfg.render()}' )