import time
import os

def digital_aarti():
    aarti_lines = [
        "🌺 जय हनुमान ज्ञान गुन सागर 🌺",
        "🌺 जय कपीस तिहुं लोक उजागर 🌺",
        "🌺 राम दूत अतुलित बल धामा 🌺",
        "🌺 अंजनि पुत्र पवनसुत नामा 🌺",
        "",
        "🪔 आरती कीजै हनुमान लला की 🪔",
        "🪔 दुष्ट दलन रघुनाथ कला की 🪔"
    ]
    
    for line in aarti_lines:
        print(line)
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen between lines

digital_aarti()