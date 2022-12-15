# observer method - behavioral design pattern
#   allows to define or create a subscription mechanism to send notification to
#   multiple objects about any new event that happens to the object that is
#   being observed


# create base class
class Subject:
    # represents what is being observed
    def __init__(self):
        # create an empty observer list
        self._observers = []

    def notify(self, modifier = None):
        # alert the observers
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
    # if observer is not in the list, append it into the list
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
    # remove the observer from the observer list
        try:
            self._observers.remove(observer)
        except ValueError:
            pass


# create data class
class Data(Subject):
    # monitor the object
    def __init__(self, name =''):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


# create viewer classes
# - Open/Closed Principle: introducing subscriber classes is easier in Observer
#   method as compared to others without making changes in the code
# - Establishes Relationships: easy to establishes relationships at runtime
#   between the objects
# - Description: carefully describes about coupling present between objects and
#   observer - hence, no need to modify Subject to add or remove observers
class HexViewer:
    # updates the Hexviewer
    def update(self, subject):
        print('HexViewer: Subject {} has data 0x{:x}'.format(subject.name, subject.data))


class OctalViewer:
    # updates the Octal viewer
    def update(self, subject):
        print('OctalViewer: Subject' + str(subject.name) + 'has data '+str(oct(subject.data)))


class DecimalViewer:
    # updates the Decimal viewer
    def update(self, subject):
        print('DecimalViewer: Subject % s has data % d' % (subject.name, subject.data))


# run method
if __name__ == '__main__':
    obj1 = Data('Data 1')
    obj2 = Data('Data 2')

    view1 = DecimalViewer()
    view2 = HexViewer()
    view3 = OctalViewer()

    obj1.attach(view1)
    obj1.attach(view2)
    obj1.attach(view3)

    obj2.attach(view1)
    obj2.attach(view2)
    obj2.attach(view3)

    obj1.data = 10
    obj2.data = 15