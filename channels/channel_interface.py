from abc import abstractmethod


class Channel:
    name: str

    @abstractmethod
    def output(self, output: str):
        pass

    @abstractmethod
    def get_input(self) -> str:
        pass

    def get_name(self):
        return self.name
