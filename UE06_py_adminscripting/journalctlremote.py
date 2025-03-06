# Fragen

# Welche Dateien werden erzeugt – wie lautet deren absoluter Pfad?
# C:\Users\Luka Pacar\.ssh\id_rsa (private key) und C:\Users\Luka Pacar\.ssh\id_rsa.pub (public key)

# Welche zusätzlichen Informationen werden angezeigt?
# → Pfad der gespeicherten Schlüsseldateien
# → Fingerprint des Schlüssels
# → grafische Darstellung des Schlüssels

# ssh-copy-id
# Welche Daten werden kopiert (Quelle – Ziel)?
# Der öffentliche Schlüssel wird in die Datei ~/.ssh/authorized_keys auf dem Zielrechner kopiert.
# Warum darf der private-key die eigene Maschine NIEMALS verlassen?
# Weil sonst der Zugriff nicht mehr sicher ist (jemand anderes kann den Schlüssel verwenden)

# Was passiert jetzt beim Verbinden mit ssh user@IP-Adresse? Wird nach einem Passwort gefragt?
# Nein, es wird nicht nach einem Passwort gefragt, da der private Schlüssel auf dem lokalen Rechner vorhanden ist.

# Warum gilt die Authentifizierung mittels Schlüsselpaar als sicherer6 als ein Login mittels herkömmlicher Passwörter?
# Weil es schwerer ist die Keys zu knacken als das Passwort, und man könnte zuschauen wenn jemand das Passwort eingibt.

__author__ = "Luka Pacar"

from getpass import getpass

import paramiko

# Kopiert von der Angabe
def key_based_connect(username: str, key_path: str, host: str, passphrase :str=None):
    """
    Connect to a remote host using keys.

    :param username: Username to connect with
    :param key_path: Path to the private key
    :param host: Host to connect to
    :param passphrase: Passphrase for the key
    :return: paramiko.SSHClient Connection
    """
    if not passphrase:
        passphrase = getpass(f"Enter passphrase for key: {key_path}")
    pkey = paramiko.RSAKey.from_private_key_file(key_path, password=passphrase)
    client = paramiko.SSHClient()
    policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(policy)
    client.connect(host, username=username, pkey=pkey, )
    return client

def get_journal_logs(username: str, host: str, key_path: str, minutes: int):
    """
    Get the journal logs from a remote machine.

    :param username: Username to connect with
    :param host: Host to connect to
    :param key_path: Path to the private key
    :param minutes: Minutes to go back in the logs
    :return: str of the logs
    """
    client = key_based_connect(username, key_path, host)

    # journalctl auf der remote-maschine ausführen
    stdin, stdout, stderr = client.exec_command('journalctl --since "{} minutes ago"'.format(minutes))

    return stdout.read().decode()


if __name__ == "__main__":
    print("Reading Logs")
    print(get_journal_logs("junioradmin", "192.168.140.130", r"C:\Users\Luka Pacar\.ssh\id_rsa", 10))
    print("Finished Reading Logs")