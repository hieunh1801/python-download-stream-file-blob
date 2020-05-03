import subprocess
infile = 'C://Users//hieun//OneDrive//Máy tính//download//kimino_namaewa.ts'
outfile = 'kimino_namaewa.mp4'
subprocess.run(['ffmpeg', '-i', infile, outfile])
