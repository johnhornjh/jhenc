import base64
import gzip
import os
import random
import binascii
from rich.console import Console
from rich.prompt import Prompt
with open("b", "r") as file:
    banner = file.read()
    
console = Console()

# Banner
def tampilkan_banner():
    console.print(banner, style="bold blue")

# Fungsi encoding
def encode_base64(data):
    return base64.b64encode(data.encode()).decode()

def encode_gzip(data):
    return base64.b64encode(gzip.compress(data.encode())).decode()

def encode_hex(data):
    return binascii.hexlify(data.encode()).decode()

# Fungsi decoding di dalam script Bash
def generate_decoder(var_name, encoded_data, method):
    if method == "base64":
        return f'#ENC BY JH DV\n#GAGAGUGU\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n#Hai\n{var_name}="{encoded_data}"; eval "$(echo ${{{var_name}}} | base64 -d)"'
    elif method == "gzip":
        return f'#ENC BY JH DV\n#GAGAGUGU\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n#Hai\n{var_name}="{encoded_data}"; eval "$(echo ${{{var_name}}} | base64 -d | gunzip)"'
    elif method == "base":
        return f'#ENC BY JH DV\n#GAGAGUGU\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n#Hai\n{var_name}="{encoded_data}"; eval "$(echo ${{{var_name}}} | base64 -d)"'

# Fungsi obfuscasi file Bash
def obfuscate_bash(file_path, jumlah_enc):
    with open(file_path, "r") as f:
        original_content = f.read()

    methods = {
        "john": (encode_base64, "base64"),
        "horn": (encode_gzip, "gzip"),
        "dika": (encode_hex, "base"),
    }

    content = original_content

    console.print(f"🔄 [green]Memproses obfuscasi {jumlah_enc} kali...[/green]")

    for i in range(jumlah_enc):
        method_name, (encode_fn, method) = random.choice(list(methods.items()))

        content = encode_fn(content)
        content = generate_decoder(method_name, content, method)

    final_file_path = f"{file_path}_e.sh"
    with open(final_file_path, "w") as f:
        f.write(content)

    console.print(f"✅ [yellow]Enkripsi selesai! File tersimpan sebagai:[/yellow] [bold]{final_file_path}[/bold]")

# Fungsi input dengan validasi
def dapatkan_input():
    file_path = Prompt.ask("📂 Masukkan nama atau lokasi file :")
    
    if not os.path.exists(file_path):
        console.print("⛔ [red]File tidak ditemukan![/red]")
        return None, None

    try:
        jumlah_enc = int(Prompt.ask("🔢 Masukkan jumlah ENC"))
        if jumlah_enc < 1:
            raise ValueError
    except ValueError:
        console.print("⛔ [red]Masukkan angka yang valid![/red]")
        return None, None

    return file_path, jumlah_enc

# Main program
if __name__ == "__main__":
    tampilkan_banner()
    file_path, jumlah_enc = dapatkan_input()
    if file_path:
        obfuscate_bash(file_path, jumlah_enc)