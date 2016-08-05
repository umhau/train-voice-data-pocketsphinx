




def delete_last_line_in_file(filename):
    readFile = open(filename)
    lines = readFile.readlines()
    readFile.close()
    w = open(filename,'w')
    w.writelines([item for item in lines[:-1]])
    w.close()



def delete_record(training_data_name, record_number):
    delete = True
    while delete:
        delete = raw_input("Press [enter] to continue.  To delete the last recording, press 1. \n\n")
        try:
            if int(delete) == 1:
                record = "./" + training_data_name + "/" + training_data_name + "_" + str(record_number).zfill(4) + ".wav"
            print("Ready to delete record:" + record)
            confirm = raw_input("Type 'yes' to confirm deletion, any other key to return to deletion prompt.\n")
            
            if confirm == 'yes':
                try:
                    os.remove(record)
                    
                    # .fileids
                    fileids_filename = "./" + training_data_name + "/" +training_data_name + '.fileids'  
                    delete_last_line_in_file(fileids_filename)                        

                    # .transcription
                    transcription_filename = "./" + training_data_name + "/" +training_data_name + '.transcription'
                    delete_last_line_in_file(transcription_filename) 
                    
                    print("Record deleted.")
                    print("")
                    
                except OSError:
                
                    print("\nFile did not exist. No deletion occured. Returning to prompt.\n")
            else:
                delete = True
                
        except ValueError:
        
            if delete:
                delete = True
            else:
                delete = False
    return delete
