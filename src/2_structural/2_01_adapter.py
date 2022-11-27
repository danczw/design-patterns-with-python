# adapter method - structural design pattern
#   helps to make two incompatible interfaces work together by creating a bridge
#   between them -> allows to use existing classes with new interfaces

from abc import ABC, abstractmethod


# create existing base class
class PngInterface(ABC):
    @abstractmethod
    def draw(self):
        pass

class PngImage(PngInterface):
    def __init__(self, png):
        self.png = png
        self.format = 'raster'
        
    def draw(self):
        print('drawing ' + self.get_image())
            
    def get_image(self):
        return 'png'

# create new class
class SvgImage:
    def __init__(self, svg):
        self.svg = svg
        self.format = 'vector'
        
    def get_image(self):
        return 'svg'

# create object adapter
# - helps in achieving flexibility and reusability of existing classes
# - allows to introduce new adapter classes into the code without violating the
#   open/closed principle (wikipedia.org/wiki/Open–closed_principle)
class SvgAdapter(PngInterface):
    def __init__(self, svg):
        self.svg = svg
        
    def rasterize(self):
        return 'rasterized ' + self.svg.get_image()
    
    def draw(self):
        img = self.rasterize()
        print('drawing ' + img)

# create class adapter
# - only be implemented in languages that support multiple inheritance
#   -> inheriting all of their functionalities
# - instance of the adapter can replace either our class or the external class,
#   under a uniform interface
class ConvertingNonVector(Exception):
    # exception used to check whether image can be rasterized
    pass

class ClassAdapter(PngImage, SvgImage):
    def __init__(self, image):
        self.image = image
        
    def rasterize(self):
        if(self.image.format == "vector"):
            return "rasterized " + self.image.get_image()
        else:
            raise ConvertingNonVector
        
    def draw(self):
        try:
            img = self.rasterize()
            print("drawing " + img)
        except ConvertingNonVector as e:
            print("drawing " + self.image.get_image())


# run method
if __name__ == '__main__':
    regular_png = PngImage('some data')
    regular_png.draw()

    example_svg = SvgImage('some more data')
    example_adapter = SvgAdapter(example_svg)
    example_adapter.draw()
    
    example_adapter = ClassAdapter(example_svg)
    example_adapter.draw()