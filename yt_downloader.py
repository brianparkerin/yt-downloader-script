import yt_dlp
import sys
import time

def print_progress(d):
    if d['status'] == 'downloading':
        percent = d.get('downloaded_bytes', 0) / d.get('total_bytes', 1) * 100
        sys.stdout.write(f"\rDescargando, espere... {percent:.2f}% completado")
        sys.stdout.flush()

def download_youtube_video(url):
    ydl_opts = {
        'format': 'best[height<=720]/best[height<=480]',  # Descarga el mejor formato con resolución <= 720p, si no, <= 480p
        'outtmpl': '%(title)s.%(ext)s',  # Nombre del archivo de salida
        'progress_hooks': [print_progress],  # Hook para mostrar el progreso de la descarga
    }
    
    try:
        print("Iniciando la descarga...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            print("\n¡Descarga completada!")
            print(f"Descargado: {info_dict['title']}")
    except Exception as e:
        print(f"Error al procesar el video: {e}")

if __name__ == "__main__":
    video_url = input("Ingrese la URL del video de YouTube: ")
    download_youtube_video(video_url)
