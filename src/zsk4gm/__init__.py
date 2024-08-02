from zsk4gm.process_text import clean_text
from zsk4gm.process_text import tokenize
from zsk4gm.process_text import count_words

import os
import logging

log_file_path = os.path.join(os.path.dirname(__file__), 'logs', 'logfile.log')
log_dir = os.path.dirname(log_file_path)

# Ensure directory exists
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s', filename=log_file_path)
