import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO,  # Minimum level of messages to log
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log message format
                        filename='dab_api.log',  # Log file path
                        filemode='a')  # Append mode

    # Example to also log to console
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
