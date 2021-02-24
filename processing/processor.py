from rivescript import RiveScript


class Processor():
    rivescript: RiveScript = RiveScript()

    def __init__(self):
        self.rivescript.load_directory("./processing/replies")
        self.rivescript.sort_replies()

        # TODO: Passare al logger.
        print("Inizializzato correttamente RiveScript.")

    def process(self, input_request: str) -> str:
        # TODO: Gestire l'utente.
        return self.rivescript.reply("emiliodallatorre", input_request)
