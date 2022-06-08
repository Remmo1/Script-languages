import Operations
import constst
from Operations import compress_file, delete_all

# compress_file('/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/pythonProject/others/covid_test.txt')
# Operations.decompress_file('/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/pythonProject/others/covid_test-compressed.bz2')

#Operations.compress_all_files(constst.OTHERS_FOLDER)
f = Operations.search_for_folders('/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/pythonProject')
for i in f[0]:
    print(i)

print(f[0]['.bin'])
#print(chr(1))
#print(ord(''))

