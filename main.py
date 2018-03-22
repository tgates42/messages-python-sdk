import message_media_messages.message_media_messages_client
import getpass
client = message_media_messages.message_media_messages_client.MessageMediaMessagesClient(
     auth_user_name=getpass.getpass('API Key'),
     auth_password=getpass.getpass('API Pass'),
)
client.messages.create_send_messages(
        {
            "messages": [
                {
                    "content": "I want a Nintendo Switch!",
                     "destination_number": getpass.getpass('Phone'),
                }
            ]
        }
) 
