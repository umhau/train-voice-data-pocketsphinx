
import sys
import string

model_name = raw_input("\nModel name: ")
diff = raw_input("\nWhat should be removed? (Warning: this substring will be removed blindly) \n\n")
print("New file format: " + model_name.replace(diff, '', 1))
yn = raw_input("\nExecute? yes/no ")

if yn!='yes':
    sys.exit()

duties = ['.transcription','.fileids']

for i in duties:
    print("Fixing " + model_name + i + '...')

    filename = model_name + '/' + model_name+i

    readFile = open(filename)
    lines = readFile.readlines()
    readFile.close()

    complete_set = []
    for j in lines:
        line = j.replace(diff, '', 1)
        # line = j.translate(string.maketrans('', ''), diff)
        complete_set.append(line)

    w = open(filename,'w')
    w.writelines(complete_set)
    w.close()

print("Process completed.\n")

