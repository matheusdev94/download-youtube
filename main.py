from pytube import YouTube
from tqdm import tqdm

# URL do vídeo do YouTube
urls = [
    'https://www.youtube.com/watch?v=GNsuF4xB80E&list=PL0Zuz27SZ-6NamGNr7dEqzNFEcZ_FAUVX&index=7'
]

for url in urls:
    # Criar um objeto YouTube
    yt = YouTube(url)
    # Baixar o vídeo na melhor qualidade disponível
    video = yt.streams.get_highest_resolution()

    # Iniciar o download
    print(f'Baixando: {video.title}')
    with tqdm(total=video.filesize, unit='B', unit_scale=True, desc=video.title, ascii=True) as progress_bar:
        video.download(output_path='.', filename=video.title, filename_prefix='')
        progress_bar.update(video.filesize)

    print("Download concluído!")