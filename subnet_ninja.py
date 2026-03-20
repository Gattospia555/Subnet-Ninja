import ipaddress
from rich.console import Console
from rich.table import Table
import sys

def calcola_subnet(ip_input):
    """Calcola i parametri di rete a partire da un IP/CIDR."""
    try:
        # strict=False permette di passare un IP host (es. 192.168.1.5/24) 
        # e calcolare in automatico la sua rete di appartenenza.
        rete = ipaddress.IPv4Network(ip_input, strict=False)
        
        # Estrazione dei dati
        ind_rete = str(rete.network_address)
        broadcast = str(rete.broadcast_address)
        netmask = str(rete.netmask)
        
        # Calcolo degli host utilizzabili
        hosts = list(rete.hosts())
        if hosts:
            range_host = f"{hosts[0]} - {hosts[-1]}"
            totale_host = str(len(hosts))
        else:
            # Gestione delle subnet /32 o /31 dove non ci sono host utili standard
            range_host = "N/A"
            totale_host = "0"
            
        return ind_rete, netmask, broadcast, range_host, totale_host
        
    except ValueError:
        return None

def mostra_tabella(ip_input, dati_rete):
    """Crea e stampa una tabella formattata con Rich."""
    ind_rete, netmask, broadcast, range_host, totale_host = dati_rete
    
    console = Console()
    
    # Inizializzazione della tabella
    tabella = Table(title=f"🥷 Subnet-Ninja Report: [bold yellow]{ip_input}[/bold yellow]", 
                    show_header=True, 
                    header_style="bold cyan")
    
    # Definizione delle colonne
    tabella.add_column("Parametro", style="dim", width=25)
    tabella.add_column("Valore", style="bold green")
    
    # Aggiunta delle righe con i risultati
    tabella.add_row("Indirizzo di Rete", ind_rete)
    tabella.add_row("Subnet Mask", netmask)
    tabella.add_row("Indirizzo Broadcast", broadcast)
    tabella.add_row("Range Host Utili", range_host)
    tabella.add_row("Totale Host", totale_host)
    
    console.print(tabella)

if __name__ == "__main__":
    # Richiesta input semplice
    ip_target = input("Inserisci l'IP e la subnet (es. 192.168.1.0/24): ")
    
    dati = calcola_subnet(ip_target)
    
    if dati:
        mostra_tabella(ip_target, dati)
    else:
        # Messaggio di errore colorato
        Console().print(f"[bold red]Errore:[/bold red] '{ip_target}' non è un indirizzo IPv4 o una subnet valida.")