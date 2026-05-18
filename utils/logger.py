# # import logging


# # def get_logger(name):

# #     logger = logging.getLogger(name)

# #     if not logger.handlers:

# #         logger.setLevel(logging.INFO)

# #         formatter = logging.Formatter(
# #             "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
# #         )

# #         console_handler = logging.StreamHandler()
# #         console_handler.setFormatter(formatter)

# #         logger.addHandler(console_handler)

# #     return logger

# import logging
# import os


# def get_logger(name):

#     os.makedirs("logs", exist_ok=True)

#     logger = logging.getLogger(name)

#     if not logger.handlers:

#         logger.setLevel(logging.INFO)

#         formatter = logging.Formatter(
#             "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
#         )

#         file_handler = logging.FileHandler("logs/test.log")

#         console_handler = logging.StreamHandler()

#         file_handler.setFormatter(formatter)
#         console_handler.setFormatter(formatter)

#         logger.addHandler(file_handler)
#         logger.addHandler(console_handler)

#     return logger


import logging
import os

from config.config import Config


def get_logger(name):

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(name)

    if not logger.handlers:

        log_level = getattr(
            logging,
            Config.LOG_LEVEL.upper(),
            logging.INFO
        )

        logger.setLevel(log_level)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        log_file = "logs/test.log"

        file_handler = logging.FileHandler(log_file)

        console_handler = logging.StreamHandler()

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger