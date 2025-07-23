#!/usr/bin/env python3
"""
Grimoire Madness - Launcher Principale
Seleziona modalità di gioco
"""

import sys
import os
from src.core.utils import Colors, clear_screen, print_header, get_player_input

def show_main_menu():
    """Mostra il menu principale di selezione modalità"""
    clear_screen()
    print_header("🧙‍♂️ GRIMOIRE MADNESS 🧙‍♀️")
    
    print(f"{Colors.CYAN}Seleziona modalità di gioco:{Colors.END}")
    print()
    print(f"1. {Colors.GREEN}🎮 Gioco Locale{Colors.END} - Due giocatori sullo stesso PC")
    print(f"2. {Colors.BLUE}🖥️ Avvia Server Locale{Colors.END} - Server per questo PC")
    print(f"3. {Colors.CYAN}🌐 Avvia Server Remoto{Colors.END} - Server per connessioni remote")
    print(f"4. {Colors.MAGENTA}📱 Connetti a Server{Colors.END} - Client multiplayer")
    print(f"5. {Colors.YELLOW}📚 Documentazione{Colors.END} - Guide e tutorial")
    print(f"6. {Colors.RED}🚪 Esci{Colors.END}")
    print()
    
    choice = get_player_input("Scegli opzione (1-6): ", ["1", "2", "3", "4", "5", "6"])
    
    if choice == "1":
        launch_local_game()
    elif choice == "2":
        launch_server_local()
    elif choice == "3":
        launch_server_remote()
    elif choice == "4":
        launch_client()
    elif choice == "5":
        show_documentation()
    elif choice == "6":
        print(f"{Colors.YELLOW}👋 Arrivederci!{Colors.END}")
        sys.exit(0)

def launch_local_game():
    """Avvia il gioco locale"""
    print(f"{Colors.GREEN}🎮 Avvio gioco locale...{Colors.END}")
    try:
        from main import main
        main()
    except Exception as e:
        print(f"{Colors.RED}❌ Errore: {e}{Colors.END}")
        input("Premi INVIO per tornare al menu...")
        show_main_menu()

def launch_server():
    """Avvia il server"""
    print(f"{Colors.BLUE}🖥️ Avvio server...{Colors.END}")
    try:
        from src.network.server_control import main
        main()
    except Exception as e:
        print(f"{Colors.RED}❌ Errore: {e}{Colors.END}")
        input("Premi INVIO per tornare al menu...")
        show_main_menu()

def launch_server_local():
    """Avvia il server per connessioni locali"""
    print(f"{Colors.BLUE}🖥️ Avvio server locale...{Colors.END}")
    print(f"{Colors.YELLOW}Server accessibile solo da questo PC (localhost){Colors.END}")
    try:
        from src.network.server_control import main
        main()
    except Exception as e:
        print(f"{Colors.RED}❌ Errore: {e}{Colors.END}")
        input("Premi INVIO per tornare al menu...")
        show_main_menu()

def launch_server_remote():
    """Avvia il server per connessioni remote"""
    print(f"{Colors.CYAN}🌐 Avvio server remoto...{Colors.END}")
    print(f"{Colors.YELLOW}Server accessibile da altri PC sulla rete{Colors.END}")
    print(f"{Colors.CYAN}Assicurati di aver aperto la porta 12345 nel firewall!{Colors.END}")
    
    # Mostra IP locale
    try:
        import socket
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f"{Colors.GREEN}🌐 Il tuo IP locale è: {local_ip}{Colors.END}")
        print(f"{Colors.CYAN}Altri PC si connettono con: {local_ip}:12345{Colors.END}")
    except:
        print(f"{Colors.YELLOW}⚠️ Impossibile rilevare IP locale{Colors.END}")
    
    print()
    try:
        # Avvia server con host 0.0.0.0 per accettare connessioni remote
        import sys
        sys.argv = ["server_control.py", "--host", "0.0.0.0", "--port", "12345"]
        from src.network.server_control import main
        main()
    except Exception as e:
        print(f"{Colors.RED}❌ Errore: {e}{Colors.END}")
        input("Premi INVIO per tornare al menu...")
        show_main_menu()

def launch_client():
    """Avvia il client"""
    print(f"{Colors.MAGENTA}📱 Avvio client...{Colors.END}")
    try:
        from src.network.client import main
        main()
    except Exception as e:
        print(f"{Colors.RED}❌ Errore: {e}{Colors.END}")
        input("Premi INVIO per tornare al menu...")
        show_main_menu()

def show_documentation():
    """Mostra la documentazione disponibile"""
    clear_screen()
    print_header("📚 DOCUMENTAZIONE")
    
    print(f"{Colors.CYAN}Guide disponibili:{Colors.END}")
    print()
    print(f"1. {Colors.GREEN}README.md{Colors.END} - Guida principale")
    print(f"2. {Colors.BLUE}GUIDA_CONNESSIONE_REMOTA.md{Colors.END} - Setup multiplayer")
    print(f"3. {Colors.MAGENTA}SERVER_CONTROL_README.md{Colors.END} - Controllo server")
    print()
    print(f"{Colors.YELLOW}📁 Posizione file: ./docs/{Colors.END}")
    print()
    print(f"{Colors.CYAN}🚀 Comandi rapidi:{Colors.END}")
    print(f"  • Gioco locale:    python grimoire_local.py")
    print(f"  • Server:          python grimoire_server.py")
    print(f"  • Client:          python grimoire_client.py")
    print()
    print(f"{Colors.CYAN}📂 Struttura cartelle:{Colors.END}")
    print(f"  • src/core/        - Logica di gioco")
    print(f"  • src/network/     - Networking")
    print(f"  • scripts/         - Script .bat")
    print(f"  • data/            - Salvataggi")
    print(f"  • docs/            - Documentazione")
    print(f"  • tests/           - Test e demo")
    print()
    
    input("Premi INVIO per tornare al menu...")
    show_main_menu()

if __name__ == "__main__":
    try:
        show_main_menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}👋 Arrivederci!{Colors.END}")
        sys.exit(0)
