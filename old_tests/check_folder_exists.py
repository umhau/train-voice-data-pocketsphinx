import os
import errno

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

make_sure_path_exists("./bespoke_training_data")

def how_much_training_data_exists_already():
    import glob
    import re
    
    path = "./bespoke_training_data"
    file_list = glob.glob(path+'/*.wav')
    numbers_list = []
    for i in file_list:
        print i
        numbers_list.append(re.findall(".*arctic_(\d{4})\.wav", i))
    number = int(max(numbers_list)[0])
        
    print("You have made %d recordings." % number)

how_much_training_data_exists_already()



