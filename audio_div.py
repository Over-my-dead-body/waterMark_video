import subprocess

def audio_div(input_video,output_audio):
    '''
    本函数用于将音频从视频文件中分离出来
    :param input_video: 视频位置必须MP4
    :param output_audio: 音频输出位置必须MP3
    :return:
    '''
    cmd = [
        r'D:\\ffmpeg\\ffmpeg-2025-05-05-git-f4e72eb5a3-full_build\\bin\\ffmpeg.exe',
        '-i', input_video,
        '-vn',  # 禁用视频流
        '-c:a', 'libmp3lame',  # 直接复制音频流
        output_audio
    ]
    try:
        result = subprocess.run(
            cmd,
            check=True,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as e:
        print("FFmpeg 错误信息：", e.stderr.decode())