import fnmatch
import os
import subprocess
#ffmpeg -i input.mp4 -i input.ass -c:v copy -c:a copy -c:s copy -map 0:0 -map 0:1 -map 1:0 -y out.mkv
ASSsubtitle=[]
SSAsubtitle=[]
SRTsubtitle=[]
MP4videoFile=[]
MKVvideoFile=[]

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
cmdname=''  # The file name without extension translated to type in terminal to avoid error caused by special characters.
for ASS in os.listdir('.'):
    if fnmatch.fnmatch(ASS, '*.ass'):
        ASSsubtitle.append(ASS[:-4])

for SSA in os.listdir('.'):
    if fnmatch.fnmatch(SSA, '*.ssa'):
        SSAsubtitle.append(SSA[:-4])

for MP4 in os.listdir('.'):
    if fnmatch.fnmatch(MP4, '*.mp4'):
        MP4videoFile.append(MP4[:-4])

for SRT in os.listdir('.'):
    if fnmatch.fnmatch(SRT, '*.srt'):
        SRTsubtitle.append(SRT[:-4])
for MKV in os.listdir('.'):
	if fnmatch.fnmatch(MKV, '*.mkv'):
		MKVvideoFile.append(MKV[:-4])

for name in MKVvideoFile:
    if name in SRTsubtitle and name not in ASSsubtitle and name not in SSAsubtitle:
        for char in name:
            cmdname=cmdname+schar(char)
        command='/usr/local/bin/ffmpeg -i '+cmdname+'.mkv -i '+cmdname+'.srt -c:v copy -c:a copy -c:s copy -map 0:0 -map 0:1 -map 1:0 -y '+cmdname+'Sub'+'.mkv'
        print (command)
        subprocess.call(command, shell=True)
        cmdname=''

    elif name in SSAsubtitle and name not in ASSsubtitle:
        for char in name:
            cmdname=cmdname+schar(char)
        command='/usr/local/bin/ffmpeg -i '+cmdname+'.mkv -i '+cmdname+'.ssa -c:v copy -c:a copy -c:s copy -map 0:0 -map 0:1 -map 1:0 -y '+cmdname+'Sub'+'.mkv'
        print (command)
        subprocess.call(command, shell=True)
        cmdname=''

    elif name in ASSsubtitle:
        for char in name:
            cmdname=cmdname+schar(char)
        command='/usr/local/bin/ffmpeg -i '+cmdname+'.mkv -i '+cmdname+'.ass -c:v copy -c:a copy -c:s copy -map 0:0 -map 0:1 -map 1:0 -y '+cmdname+'Sub'+'.mkv'
        subprocess.call(command, shell=True)
        cmdname=''

for name in MP4videoFile:
    if name in SRTsubtitle and name not in ASSsubtitle and name not in SSAsubtitle:
	    for char in name:
	        cmdname=cmdname+schar(char)
	    command='/usr/local/bin/ffmpeg -i '+cmdname+'.mp4 -i '+cmdname+'.srt -c:v copy -c:a copy -c:s copy -map 0:0 -map 0:1 -map 1:0 -y '+cmdname+'.mkv'
	    print (command)
	    subprocess.call(command, shell=True)
	    cmdname=''

    elif name in SSAsubtitle and name not in ASSsubtitle:
        for char in name:
            cmdname=cmdname+schar(char)
        command='/usr/local/bin/ffmpeg -i '+cmdname+'.mp4 -i '+cmdname+'.ssa -c:v copy -c:a copy -c:s copy -map 0:0 -map 0:1 -map 1:0 -y '+cmdname+'.mkv'
        print (command)
        subprocess.call(command, shell=True)
        cmdname=''

    elif name in ASSsubtitle:
        for char in name:
            cmdname=cmdname+schar(char)
        command='/usr/local/bin/ffmpeg -i '+cmdname+'.mp4 -i '+cmdname+'.ass -c:v copy -c:a copy -c:s copy -map 0:0 -map 0:1 -map 1:0 -y '+cmdname+'.mkv'
        subprocess.call(command, shell=True)
        cmdname=''

