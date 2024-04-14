import os
import json
import logging
from sib_api_v3_sdk import ApiClient, Configuration, TransactionalEmailsApi, SendSmtpEmail
from sib_api_v3_sdk.rest import ApiException

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def notification(message):
    try:
        # Parse the incoming JSON message
        message_dict = json.loads(message)
        mp3_fid = message_dict['mp3_fid']
        receiver_address = message_dict["username"]
        sender_address = os.environ.get("SIB_FROM_EMAIL")

        # Load the email content template
        email_content = f"<html><body><p>mp3 file_id: {mp3_fid} is ready!</p></body></html>"

        # Configure API key authorization: api-key
        configuration = Configuration()
        configuration.api_key['api-key'] = os.environ.get("SIB_API_KEY")

        # Create an instance of the API class
        api_instance = TransactionalEmailsApi(ApiClient(configuration))
        send_smtp_email = SendSmtpEmail(
            to=[{"email": receiver_address}],
            sender={"email": sender_address, "name": "M3DIO"},
            subject=f"MP3 Download",
            html_content=email_content
        )

        # Send the email
        api_response = api_instance.send_transac_email(send_smtp_email)
        logging.info(f"Mail sent successfully: {api_response}")

    except ApiException as e:
        logging.error(f"Failed to send email: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
