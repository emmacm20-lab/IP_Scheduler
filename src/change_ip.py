# 📂 src/change_ip.py - Script para modificar la IP en Windows
import os

def change_ip(ip_address, subnet_mask, gateway, interface="Ethernet"):
    """Modifica la dirección IP en Windows utilizando comandos de PowerShell."""
    command = f"netsh interface ip set address name=\"{interface}\" static {ip_address} {subnet_mask} {gateway}"
    os.system(command)
    print(f"IP cambiada a {ip_address}")

if __name__ == "__main__":
    change_ip("192.168.1.100", "255.255.255.0", "192.168.1.1")
