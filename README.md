# 🧙‍♂️ Grimoire Madness - Gioco Multiplayer di Combattimento Magico

Un gioco multiplayer da riga di comando dove i giocatori creano maghi personalizzati e combattono in epiche battaglie magiche turn-based!

## ✨ Caratteristiche

- 🎭 **Personalizzazione completa**: 6 razze e 6 specializzazioni magiche
- ⚔️ **Sistema di combattimento turn-based** con meccaniche di probabilità
- 🌍 **9 scenari di combattimento** che influenzano le statistiche
- 🌐 **Multiplayer locale e remoto** con server dedicato
- 💾 **Salvataggio automatico** di utenti e personaggi
- 🎮 **Controllo server avanzato** con panel di amministrazione

## 🚀 Avvio Rapido

### Launcher Unificato
```bash
python grimoire.py
```

#### Menu Principale:
```
🧙‍♂️ Grimoire Madness - Menu Principale
1. Gioco Locale        → Modalità single-player
2. Server Locale       → Server per connessioni locali (stesso PC)
3. Server Remoto       → Server per connessioni remote (altri PC)
4. Client              → Connessione a server esistente
5. Documentazione      → Guide e manuali
6. Esci
```

### ⚡ Modalità di Gioco

#### 🏠 Gioco Locale
- Modalità single-player classica
- Non richiede configurazione di rete
- Perfetto per test e pratica

#### 🌐 Server Locale
- Per multiplayer sullo stesso PC
- Indirizzo: `localhost:12345`
- Ideale per test locali

#### 🌍 Server Remoto  
- Per multiplayer da PC diversi
- Rileva automaticamente l'IP locale
- Configura automaticamente il firewall
- Mostra l'indirizzo per la connessione

#### 📱 Client
- Connessione a server esistenti
- Supporta connessioni locali e remote
- Configurazione guidata dell'indirizzo

### 🛠️ Script di Configurazione
- `setup_firewall.bat` - Configura firewall Windows
- `close_firewall.bat` - Rimuove regole firewall

## 📚 Guide Dettagliate

- **[Risoluzione Connessioni](docs/Risoluzione_Connessioni.md)** - Troubleshooting completo
- **[Guida Connessione Remota](docs/GUIDA_CONNESSIONE_REMOTA.md)** - Setup multiplayer
- **[Documentazione Completa](docs/)** - Tutte le guide disponibili

## 🎲 Meccaniche di Gioco

### Razze Disponibili
- 👤 **Umano**: Equilibrato, +1 a tutte le statistiche
- 🧝 **Elfo**: Maestro della magia, +3 Mana, +2 Intelligenza  
- 🏔️ **Nano**: Resistente, +4 Vita, +2 Costituzione
- 🌿 **Mezzelfo**: Versatile, +2 Mana, +1 Vita, +1 Intelligenza
- 👹 **Orco**: Brutale, +3 Vita, +3 Forza, -1 Intelligenza
- 🐲 **Draconico**: Potente, +2 Vita, +2 Mana, +1 Forza

### Specializzazioni Magiche
- 🔥 **Pyromante**: Maestro del fuoco (+2 danni fuoco)
- ❄️ **Criomante**: Controllo del ghiaccio (+2 danni ghiaccio)  
- ⚡ **Fulguramante**: Signore dei fulmini (+2 danni fulmine)
- 🌿 **Naturalista**: Guaritore naturale (+2 guarigione)
- 🌙 **Ombramante**: Mago oscuro (+2 danni oscurità)
- ✨ **Arcanista**: Esperto arcano (+1 a tutti i danni)

### Scenari di Combattimento
1. 🏟️ **Arena Magica** - Ambiente neutro
2. 🌋 **Vulcano Attivo** - Potenzia magie di fuoco
3. 🧊 **Caverna Ghiacciata** - Potenzia magie di ghiaccio
4. ⛈️ **Picco della Tempesta** - Potenzia magie di fulmine
5. 🌲 **Bosco Incantato** - Potenzia magie naturali
6. 🌑 **Santuario Oscuro** - Potenzia magie oscure
7. 📚 **Biblioteca Arcana** - Potenzia magie arcane
8. 🏜️ **Deserto Mistico** - Riduce mana ma aumenta danni
9. 🌊 **Isola Fluttuante** - Bonus casuali variabili

## 🎮 Controlli Server

Nel control panel del server (`server_control.py`):
- `status` - Stato del server e statistiche
- `players` - Lista giocatori connessi
- `combats` - Combattimenti attivi
- `network` - Informazioni di connessione
- `save` - Forza salvataggio dati
- `shutdown` - Spegnimento sicuro
- `quit` - Terminazione immediata

## 🔧 Requisiti Tecnici

- **Python 3.7+** (solo librerie standard)
- **Porte di rete**: 12345 (default, configurabile)
- **Sistema**: Windows, Linux, macOS

## 📁 Struttura del Progetto

```
Grimoire Madness/
├── main.py              # Gioco locale
├── server.py            # Server multiplayer  
├── server_control.py    # Control panel server
├── client.py            # Client multiplayer
├── game_engine.py       # Engine principale
├── wizard.py            # Classi maghi
├── spells.py            # Sistema magie
├── combat.py            # Sistema combattimento
├── scenarios.py         # Scenari di combattimento
├── player.py            # Gestione giocatori
├── utils.py             # Utility e colori
├── config.py            # Configurazioni
├── connect_local.bat    # Connessione locale rapida
├── connect_remote.bat   # Connessione remota rapida
└── GUIDA_CONNESSIONE_REMOTA.md
```

## 🎯 Esempi di Utilizzo

### Partita Locale
```bash
# Avvia il gioco per 2 giocatori sullo stesso PC
python main.py
```

### Server Privato per Amici
```bash
# Host: Avvia server
python server_control.py --host 0.0.0.0 --port 12345

# Amici: Si connettono
python client.py --host [IP_DELL_HOST] --port 12345
```

### Test di Connessione
```bash
# Terminale 1: Server
python server_control.py

# Terminale 2: Client
python client.py --host localhost --port 12345
```

## 🛡️ Sicurezza e Rete

- **Firewall**: Apri la porta configurata (default 12345)
- **IP privati**: Usa per LAN locale (192.168.x.x)
- **Port forwarding**: Necessario per connessioni Internet
- **Salvataggio**: Dati salvati automaticamente in JSON

## 🐛 Risoluzione Problemi

### Errori di Connessione
- Verifica IP e porta del server
- Controlla firewall e antivirus
- Assicurati che il server sia avviato

### Errori di Gioco
- Controlla i log nel terminal del server
- Usa `status` nel control panel
- Riavvia server e client se necessario

## 🎮 Come Giocare

1. **Crea il tuo mago**: Scegli razza e specializzazione
2. **Entra in combattimento**: Attendi un avversario
3. **Lancia magie**: Scegli dalla tua collezione di incantesimi
4. **Vinci battaglie**: Usa strategia e un po' di fortuna!

## 🏆 Caratteristiche Avanzate

- **Sistema DC**: Ogni magia ha una Difficulty Class
- **Probabilità dinamiche**: Successo basato su statistiche
- **Effetti ambientali**: Gli scenari influenzano il combattimento
- **Persistenza dati**: Utenti e maghi salvati tra sessioni
- **Thread sicuri**: Server robusto per più connessioni

---

🎮 **Buon divertimento con Grimoire Madness!** 🧙‍♂️✨

*Per supporto tecnico o problemi, consulta la documentazione o i log del server.*
