#!/usr/bin/env python
import os
import requests

# Output configuration
enable_document_id = True
enable_document_file_name = True
enable_document_created = False
enable_document_source_path = False
enable_document_thumbnail_path = False
enable_document_original_filename = True
enable_document_correspondent = True
enable_document_tags = True
enable_document_added = False
enable_document_modified = False
enable_document_download_url = False
enable_document_passphrase = False

# Generate Thumbnail
enable_thumbnail = True

# Paperless URL
base_url = "YourIP/Domain"
enable_document_url = True
enable_download_url = True

# Telegram Bot Configuration
telegram_api_token = "YourTelegramBotToken"
telegram_chat_id = "YourChatID"

# Execute Telegram functions
def send_telegram_message_with_thumbnail(text, image_path):
    telegram_url = f"https://api.telegram.org/bot{telegram_api_token}/sendPhoto"
    params = {
        "chat_id": telegram_chat_id,
        "caption": text,
        "parse_mode": "HTML"
    }

    try:
        with open(image_path, 'rb') as image_file:
            response = requests.post(telegram_url, params=params, files={'photo': image_file})

        response raise_for_status()
        print("Telegram notification sent with thumbnail.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending Telegram notification with thumbnail: {e}")

def send_telegram_message(text):
    telegram_url = f"https://api.telegram.org/bot{telegram_api_token}/sendMessage"
    params = {
        "chat_id": telegram_chat_id,
        "text": text,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(telegram_url, params=params)
        response.raise_for_status()
        print("Telegram notification sent without thumbnail.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending Telegram notification without thumbnail: {e}")

# Environment variables from Paperless
document_id = os.getenv("DOCUMENT_ID")
document_file_name = os.getenv("DOCUMENT_FILE_NAME")
document_created = os.getenv("DOCUMENT_CREATED")
document_source_path = os.getenv("DOCUMENT_SOURCE_PATH")
document_thumbnail_path = os.getenv("DOCUMENT_THUMBNAIL_PATH")
document_original_filename = os.getenv("DOCUMENT_ORIGINAL_FILENAME")
document_correspondent = os.getenv("DOCUMENT_CORRESPONDENT")
document_tags = os.getenv("DOCUMENT_TAGS")
document_added = os.getenv("DOCUMENT_ADDED")
document_modified = os.getenv("DOCUMENT_MODIFIED")
document_download_url = os.getenv("DOCUMENT_DOWNLOAD_URL")
document_passphrase = os.getenv("PASSPHRASE")

# The message is created as is
message = "ℹ 📄 <b>New document has been processed:</b> \n\n"

# Checking enable flags to determine which function to call
if enable_document_id:
    message += f"Document ID: {document_id}\n\n"

if enable_document_url:
    document_url = f"{base_url}/documents/{document_id}/details"
    message += f"<a href=\"{document_url}\">Edit Document</a>\n\n"

if enable_download_url:
    download_url = f"{base_url}/api/documents/{document_id}/download/"
    message += f"<a href=\"{download_url}\">Download Document</a>\n\n"

if enable_document_original_filename:
    message += f"Original Filename: {document_original_filename}\n\n"

if enable_document_created:
    message += f"Created: {document_created}\n\n"

if enable_document_added:
    message += f"Added: {document_added}\n\n"

if enable_document_modified:
    message += f"Modified: {document_modified}\n\n"

if enable_document_correspondent:
    message += f"Correspondent: {document_correspondent}\n\n"

if enable_document_tags:
    message += f"Tags: {document_tags}\n\n"

if enable_document_passphrase:
    message += f"Processed with Passphrase: {document_passphrase}\n\n"

if enable_document_file_name:
    message += f"Generated File Name: {document_file_name}\n\n"

if enable_document_source_path:
    message += f"Source Path: `{document_source_path}`\n\n"

if enable_document_thumbnail_path:
    message += f"Thumbnail Path: `{document_thumbnail_path}`\n\n"

if enable_document_download_url:
    message += f"Download URL: `{document_download_url}`\n\n"

# Calling the correct function based on the enable_thumbnail flag
if enable_thumbnail:
    send_telegram_message_with_thumbnail(message, document_thumbnail_path)
else:
    send_telegram_message(message)
