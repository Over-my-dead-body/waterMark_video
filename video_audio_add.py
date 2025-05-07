import subprocess

def video_audio_add(input_video,input_audio,output_video):
    '''
    本函数可以给视频添加音频
    :param input_video: 没有音频的视频
    :param input_audio: 视频音频
    :param output_video: 添加完音频的视频
    :return:
    '''
    cmd = [
        r'D:\\ffmpeg\\ffmpeg-2025-05-05-git-f4e72eb5a3-full_build\\bin\\ffmpeg.exe',
        '-i', input_video,
        '-i', input_audio,
        '-c', 'copy',
        '-map', '0:v:0',
        '-map', '1:a:0',
        output_video
    ]

    try:
        result = subprocess.run(
            cmd,
            check=True,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as e:
        print("FFmpeg 错误信息：", e.stderr.decode())
