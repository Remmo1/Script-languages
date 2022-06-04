import Operations
import constst
from Operations import compress_file

# compress_file('/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/pythonProject/others/covid_test.txt')
# Operations.decompress_file('/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/pythonProject/others/covid_test-compressed.bz2')

Operations.compress_all_files(constst.OTHERS_FOLDER)
