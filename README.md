![alt Telegram](https://vr6-syncro.de/paperless_telegram.png)

# Paperless-NGX-Telegram German

**Hinweis:** Dies ist ein Post-Consumption-Skript für Paperlexx NGX, das bei erfolgreicher Verarbeitung eines neuen Dokuments eine konfigurierbare Telegram-Nachricht sendet.

## Installation in Docker-Umgebungen

1. Füge in der Docker Compose-Datei ein Host-Mount des Skripts hinzu. Die Einzelheiten dazu findest du in der [offiziellen Dokumentation](https://docs.paperless-ngx.com/advanced_usage/#docker-consume-hooks).

   (Der Pfad im Container ist `PAPERLESS_POST_CONSUME_SCRIPT`.)

2. Logge dich dann auf der Paperless-Webserver-Konsole ein und führe die folgenden Befehle aus. Stelle sicher, dass der Pfad entsprechend deiner Einstellungen angepasst ist.

   ```bash
   sudo chmod 755 /dein/pfad/telegram_de.py
   sudo chmod +x /dein/pfad/telegram_de.py
   ```

3. Konfiguriere das Skript:

   - `base_url` sollte die IP-Adresse deines Servers oder deine Domain sein.

   - `telegram_api_token` ist der Token, den du von BotFather zugewiesen bekommst. Informationen zur Einrichtung eines Telegram-Bots findest du leicht über eine Google-Suche.

   - `telegram_chat_id` sind die IDs, an die die Nachrichten gesendet werden sollen. Dies kann deine eigene ID oder die ID eines Chat-Teilnehmers sein.

   - Die restlichen Konfigurationsoptionen sind entweder auf `True` oder `False` zu setzen, je nachdem, wie du sie verwenden möchtest.
   
   
   

   
   
# Paperless-NGX-Telegram English

**Note:** This is a post-consumption script for Paperlexx NGX that sends a configurable Telegram message upon successful processing of a new document.

## Installation in Docker Environments

1. Add a host mount of the script in the Docker Compose file. For details, refer to the [official documentation](https://docs.paperless-ngx.com/advanced_usage/#docker-consume-hooks).

   (The path in the container is `PAPERLESS_POST_CONSUME_SCRIPT`.)

2. Next, log in to the Paperless web server console and execute the following commands. Make sure to adjust the path according to your settings.

   ```bash
   sudo chmod 755 /your/path/telegram_en.py
   sudo chmod +x /your/path/telegram_en.py
   ```

3. Configure the script:

   - `base_url` should be your server's IP address or domain.

   - `telegram_api_token` is the token assigned to you by BotFather. You can easily find instructions on setting up a Telegram bot through a Google search.

   - `telegram_chat_id` is the ID(s) to which messages should be sent. This can be your own ID or the ID of a chat participant.

   - The remaining configuration options should be set to either `True` or `False`, depending on how you wish to use them.
