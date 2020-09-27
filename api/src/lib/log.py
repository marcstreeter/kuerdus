import logging
import sys


def setup():
    logging.basicConfig(
        level=logging.INFO,
        handlers=[ColorStdErr()]
    )


class ColorStdErr(logging.StreamHandler):
    def __init__(self):
        class AddColor(logging.Formatter):
            def format(self, record):
                msg = super().format(record)
                color = '\033[1;' + ('32m', '36m', '33m', '31m', '41m')[
                    min(4, int(4*record.levelno / logging.FATAL))]
                return color + record.levelname + '\033[1;0m: ' + msg
        super().__init__(sys.stderr)
        self.setFormatter(AddColor())
