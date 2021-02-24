from channels.channel_interface import Channel
from channels.terminal import Terminal
from processing.processor import Processor


def main():
    brain: Processor = Processor()

    current_channel = Terminal()

    while True:
        input_request: str = current_channel.get_input()

        if input_request == "/shutdown":
            break

        output: str = brain.process(input_request)

        current_channel.output(output)


main()
