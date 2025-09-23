 
import prepare_mail_content.index
# from send_email.index import * not recommended
from send_email.index import send_email

prepare_mail_content.index.prepare_content("Order packed")

send_email("Order Complete", "test@example.com")

import email_utils

from email_utils.format_message import format_message

email_utils.format_message("test message")

format_message("test message again")