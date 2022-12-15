# memento method - behavioral design pattern
#   provides the ability to restore an object to its previous state without
#   revealing the details of concrete implementations


# create memento class
# - Encourages Encapsulation: memento method can help in producing state of the
#   object without breaking the encapsulation of code
# - Simplifies Code: take advantage of caretaker who can help in simplifying
#   code by maintaining the history of the originator’s code
# - Generic Memento’s Implementation: better to use Serialization to achieve
#   memento pattern implementation that is more generic rather than Memento
#   pattern where every object needs to have it’s own Memento class implementation
class Memento(object):
    def __init__(self, state):
        self._state = state

    def get_saved_state(self):
        return self._state


# create originator class
class Originator(object):
    _state = ""

    def set(self, state):
        self._state = state
        print("Originator: Setting state to", self._state)

    def save_to_memento(self):
        print("Originator: Saving to Memento.")
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_saved_state()
        print("Originator: State after restoring from Memento:", self._state)


# run method
if __name__ == '__main__':
    saved_states = []
    originator = Originator()
    originator.set("State-1")
    originator.set("State-2")
    saved_states.append(originator.save_to_memento())

    originator.set("State-3")
    saved_states.append(originator.save_to_memento())

    originator.set("State-4")

    originator.restore_from_memento(saved_states[0])