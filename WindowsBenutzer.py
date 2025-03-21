import win32net
import win32netcon
import datetime

def list_users():
    # Abfragen der Benutzerinformationen
    server = None  # Standardmäßig auf dem lokalen Computer
    level = 2  # Gibt erweiterte Benutzerinformationen zurück
    users = []

    try:
        user_info, total, resume = win32net.NetUserEnum(server, level, win32netcon.FILTER_NORMAL_ACCOUNT)
        for user in user_info:
            username = user['name']
            full_name = user['full_name']
            comment = user['comment']
            created = datetime.datetime.fromtimestamp(user['last_logon']).strftime('%Y-%m-%d %H:%M:%S') if user['last_logon'] != 0 else 'Nicht verfügbar'
            print(f"Benutzername: {username}")
            print(f"Vollständiger Name: {full_name}")
            print(f"Kommentar: {comment}")
            print(f"Erstellt am: {created}")
            print("-" * 40)
    except Exception as e:
        print(f"Fehler beim Abrufen der Benutzerinformationen: {e}")

if __name__ == "__main__":
    list_users()