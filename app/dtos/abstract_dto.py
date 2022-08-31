from abc import ABC, abstractmethod


class AbstractDTO(ABC):

    @staticmethod
    @abstractmethod
    def build_from_entity(entity):
        pass

    @staticmethod
    @abstractmethod
    def get_json_parsable(self):
        pass