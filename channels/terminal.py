from channels.channel_interface import Channel


class Terminal:
    name: str = "Terminale"

    def get_input(self) -> str:
        return input()

    def output(self, output: str):
        print(output)
