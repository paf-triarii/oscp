import subprocess
import time

host="10.11.1.136"
port="445"
share="Bob Share"

current_milli_time = lambda: int(round(time.time() * 1000))


def list_folder(folder_name, files_file, max_depth=4):
	cmd = ["smbclient", "\\\\" + host + "\\" + share + "", "-p " + str(port), "-c cd " + folder_name + ";ls;", "-N"]
	stdout,stderr = subprocess.Popen(cmd, 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT).communicate()
	
	if stderr != None and stderr is not "":
		print "There was an error in the execution. Error said: " + str(stderr)
	
	folders = []
	for line in stdout.split("\n")[3:-3]:
		file_name = ' '.join(line.strip().split()[:-5][:-2])
		file_type = line.strip().split()[:-5][-2]
		file_size = line.strip().split()[:-5][-1]
		if file_type is "A" or file_type is "N":
			msg = folder_name + "/" + file_name + " - Size: " + file_size + " bytes"
			print "File found at " + msg
			files_file.write(msg + "\n")
		elif file_type is "D" and max_depth > 0:
			print "Folder found at " + folder_name + "/" + file_name
			folders.append(folder_name + "/" + file_name)
		else:
			print "File not supported found!! File type: " + file_type
		
		
	if max_depth is 0 and len(folders) > 0:
		print "There are more folders to seach, but we have reached max_depth. Try to set a higher value"
	elif max_depth > 0 and len(folders) > 0:
		print "Looking into folders..."
		for folder in folders:
			list_folder(folder,files_file, max_depth-1)

if __name__=="__main__":
	init_time = current_milli_time()
	files_file = None
	try:
		files_file = open("smb_files_list.txt","w") 
		list_folder("/", files_file)
	except Exception as e:
		print "There was an exception: " + str(e)
	finally:
		if files_file is not None:
			files_file.close()
	end_time = current_milli_time()
	
	print "Time elapsed: " + str((end_time - init_time)/1000) + " seconds"
