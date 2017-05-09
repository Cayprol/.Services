import fnmatch
import os
import subprocess
import re
#ffmpeg -i input.mp4 -i input.ass -c:v copy -c:a copy -c:s copy -map 0:0 -map 0:1 -map 1:0 -y out.mkv

def schar(char):
    if char==' ':
        return '\\ '
    elif char=='(':
        return '\\('
    elif char==')':
        return '\\)'
    elif char=='[':
        return '\\['
    elif char==']':
        return '\\]'
    else:
        return char

command=''  # The output actually being typed in terminal by subprocess
ASSsubtitle=[ASS[:-4] for ASS in os.listdir(os.getcwd()) if re.search(r'.+\.ass$', ASS, re.I)]
SSAsubtitle=[SSA[:-4] for SSA in os.listdir(os.getcwd()) if re.search(r'.+\.ssa$', SSA, re.I)]
SRTsubtitle=[SRT[:-4] for SRT in os.listdir(os.getcwd()) if re.search(r'.+\.srt$', SRT, re.I)]
MKVvideoFile=[MKV[:-4] for MKV in os.listdir(os.getcwd()) if re.search(r'.+\.mkv$', MKV, re.I)]
MP4videoFile=[MP4[:-4] for MP4 in os.listdir(os.getcwd()) if re.search(r'.+\.mp4$', MP4, re.I)]



for name in MKVvideoFile:
    cmdname=''
    for char in name:
        cmdname+=schar(char)
    tup=(cmdname+'.mkv', cmdname, cmdname+'Sub.mkv')
    if name in SRTsubtitle and name not in ASSsubtitle and name not in SSAsubtitle:
        command='/usr/local/bin/ffmpeg -i {} -i {}.srt -c:v copy -c:a copy -c:s copy -map 0:0 -map 0:1 -map 1:0 -y {}'.format(*tup)
        print (command)
        subprocess.call(command, shell=True)

    elif name in SSAsubtitle and name not in ASSsubtitle:
        command='/usr/local/bin/ffmpeg -i {} -i {}.ssa -c:v copy -c:a copy -c:s copy -map 0:0 -map 0:1 -map 1:0 -y {}'.format(*tup)
        print (command)
        subprocess.call(command, shell=True)

    elif name in ASSsubtitle:
        command='/usr/local/bin/ffmpeg -i {} -i {}.ass -c:v copy -c:a copy -c:s copy -map 0:0 -map 0:1 -map 1:0 -y {}'.format(*tup)
        subprocess.call(command, shell=True)



for name in MP4videoFile:
    cmdname=''
    for char in name:
        cmdname+=schar(char)
    tup=(cmdname+'.mp4', cmdname, cmdname+'Sub.mkv')
    if name in SRTsubtitle and name not in ASSsubtitle and name not in SSAsubtitle:
	    command='/usr/local/bin/ffmpeg -i {} -i {}.srt -c:v copy -c:a copy -c:s copy -map 0:0 -map 0:1 -map 1:0 -y {}'.format(*tup)
	    print (command)
	    subprocess.call(command, shell=True)

    elif name in SSAsubtitle and name not in ASSsubtitle:
        command='/usr/local/bin/ffmpeg -i {} -i {}.ssa -c:v copy -c:a copy -c:s copy -map 0:0 -map 0:1 -map 1:0 -y {}'.format(*tup)
        print (command)
        subprocess.call(command, shell=True)

    elif name in ASSsubtitle:
        command='/usr/local/bin/ffmpeg -i {} -i {}.ass -c:v copy -c:a copy -c:s copy -map 0:0 -map 0:1 -map 1:0 -y {}'.format(*tup)
        subprocess.call(command, shell=True)


