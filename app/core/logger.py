import logging

from app.core.request_context import request_id_ctx

class RequestFormatter(logging.Formatter):

    def format(self, record):
        record.request_id = request_id_ctx.get()
        return super().format(record)

def get_logger(name: str):

    logger = logging.getLogger(name)

    if not logger.handlers:

        handler = logging.StreamHandler()

        formatter = RequestFormatter(
            "%(asctime)s | %(levelname)s | %(request_id)s | %(name)s | %(filename)s:%(lineno)d | %(message)s"
        )

        handler.setFormatter(formatter)

        logger.addHandler(handler)

        logger.setLevel(logging.INFO)

        logger.propagate = False

    return logger