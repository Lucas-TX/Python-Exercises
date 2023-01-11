print('Exercício 18: Calcula o tempo de download de um arquivo')
tamanhoArquivo = input('Escreva o tamanho do arquivo para download(MB):\n')
velocidadeInternet = input('Escreva a velocidade média da internet(Mbps):\n')
tempoDownload_segundos = float(tamanhoArquivo) / float(velocidadeInternet)
tempoDownload_minutos = tempoDownload_segundos/60
