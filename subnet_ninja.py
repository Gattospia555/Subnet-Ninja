import ipaddress
import argparse
from rich.console import Console
from rich.table import Table


def calcola_subnet(ip_input):
    """
    Calcola i parametri di rete a partire da un IP/CIDR.

    Args:
        ip_input (str): Indirizzo IP con subnet mask in formato CIDR (es. "192.168.1.0/24")

    Returns:
        tuple: (indirizzo_rete, netmask, broadcast, range_host, totale_host) o None se errore
    """
    try:
        # Creiamo l'oggetto rete IPv4
        rete = ipaddress.IPv4Network(ip_input, strict=False)

        # Estraiamo i parametri principali
        ind_rete = str(rete.network_address)
        broadcast = str(rete.broadcast_address)
        netmask = str(rete.netmask)

        # Calcoliamo gli host utilizzabili
        hosts = list(rete.hosts())
        if hosts:
            range_host = f"{hosts[0]} - {hosts[-1]}"
            totale_host = str(len(hosts))
        else:
            range_host = "N/A"
            totale_host = "0"

        return ind_rete, netmask, broadcast, range_host, totale_host

    except ValueError:
        # Ritorniamo None in caso di input non valido
        return None


def mostra_tabella(ip_input, dati_rete):
    """
    Crea e stampa una tabella formattata con Rich.

    Args:
        ip_input (str): L'input originale dell'utente
        dati_rete (tuple): I dati calcolati dalla funzione calcola_subnet
    """
    ind_rete, netmask, broadcast, range_host, totale_host = dati_rete
    console = Console()

    # Creiamo la tabella con titolo e stili
    tabella = Table(
        title=f"🥷 Subnet-Ninja Report: [bold yellow]{ip_input}[/bold yellow]",
        show_header=True,
        header_style="bold cyan"
    )

    # Aggiungiamo le colonne
    tabella.add_column("Parametro", style="dim", width=25)
    tabella.add_column("Valore", style="bold green")

    # Popoliamo la tabella con i dati
    tabella.add_row("Indirizzo di Rete", ind_rete)
    tabella.add_row("Subnet Mask", netmask)
    tabella.add_row("Indirizzo Broadcast", broadcast)
    tabella.add_row("Range Host Utili", range_host)
    tabella.add_row("Totale Host", totale_host)

    # Stampiamo la tabella
    console.print(tabella)


def main():
    """
    Funzione principale che gestisce gli argomenti CLI e coordina il calcolo.
    """
    # Configurazione del parser degli argomenti
    parser = argparse.ArgumentParser(
        description="🥷 Subnet-Ninja: Calcolatore di Subnet per riga di comando.",
        epilog="Esempio d'uso: python subnet_ninja.py 192.168.1.0/24"
    )

    # Aggiungiamo l'argomento obbligatorio per la subnet
    parser.add_argument(
        "subnet",
        help="L'indirizzo IP e la subnet mask in formato CIDR (es. 10.0.0.0/8)"
    )

    # Parsiamo gli argomenti dalla linea di comando
    args = parser.parse_args()

    # Eseguiamo il calcolo della subnet
    dati = calcola_subnet(args.subnet)

    if dati:
        # Se il calcolo è riuscito, mostriamo la tabella
        mostra_tabella(args.subnet, dati)
    else:
        # Se c'è un errore, mostriamo un messaggio di errore
        Console().print(
            f"[bold red]Errore:[/bold red] '{args.subnet}' non è un indirizzo IPv4 "
            "o una subnet valida."
        )


if __name__ == "__main__":
    main()