from abc import ABCMeta, abstractmethod



class ModuleInterface(object, metaclass=ABCMeta):
    def __init__(self, subscribers, publishers):

        assert isinstance(publishers, list)
        assert isinstance(subscribers, list)

        self.publishers = publishers
        self.subscribers = subscribers


    @abstractmethod
    def start(self):
        raise NotImplementedError()
