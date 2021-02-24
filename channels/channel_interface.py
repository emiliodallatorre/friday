class Channel:
    name: str

    def output(self, output: str):
        pass

    def get_input(self) -> str:
        pass

    def get_name(self):
        return self.name
