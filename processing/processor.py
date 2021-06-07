import logging

from rivescript import RiveScript


class Processor:
    rivescript: RiveScript = RiveScript()

    def __init__(self):
        self.rivescript.load_directory("./processing/replies")
        self.rivescript.sort_replies()

        # TODO: Passare al logger.
        logging.debug("Inizializzato correttamente RiveScript.")

    def process(self, input_request: str) -> str:
        # TODO: Gestire l'utente.

        result: str = self.rivescript.reply("emiliodallatorre", input_request)
        if not result.startswith("[ERR"):
            return result
        else:
            logging.exception("Nessuna risposta per: " + input_request)
            return "Non ho ancora una risposta per questo, mi dispiace signore."
