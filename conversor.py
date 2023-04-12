import ffmpeg

input_file = "input.mkv"
output_file = "output.mp4"

# Define o objeto de entrada do ffmpeg
input_stream = ffmpeg.input(input_file)

# Define o objeto de saída do ffmpeg com o codec h264 e o formato mp4
output_stream = ffmpeg.output(input_stream, output_file, vcodec='h264', format='mp4')

# Executa a conversão de vídeo
ffmpeg.run(output_stream)
