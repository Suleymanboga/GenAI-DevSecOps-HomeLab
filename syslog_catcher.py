import socket
import datetime

UDP_IP = "0.0.0.0"
UDP_PORT = 514

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"🚀 SIEM Kaydedici Başlatıldı. Loglar 'firewall_logs.txt' dosyasına yazılıyor...")

try:
    with open("firewall_logs.txt", "a", encoding="utf-8") as f:
        while True:
            data, addr = sock.recvfrom(2048)
            log_mesaji = data.decode('utf-8', errors='ignore')
            
            # Sadece FortiGate loglarını dosyaya ekle
            if "devname" in log_mesaji:
                zaman = datetime.datetime.now().strftime('%H:%M:%S')
                f.write(f"[{zaman}] {log_mesaji}\n")
                f.flush() # Anında dosyaya yaz
                print(f"🎯 Log Kaydedildi: {zaman}")

except KeyboardInterrupt:
    print("\n🛑 Kayıt durduruldu.")
