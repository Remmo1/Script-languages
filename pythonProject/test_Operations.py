from unittest import TestCase
import os

from constst import DEFAULT_FOLDER
from z_operation_classes.Archivizer import Archivizer
from z_operation_classes.Compresser import Compresser
from z_operation_classes.Deleter import Deleter
from z_operation_classes.Downloader import Downloader
from z_operation_classes.Mover import Mover
from z_operation_classes.Raporter import Raporter
from z_operation_classes.Starting import Starter
from z_operation_classes.UserFunctions import Userfunctions


class Test(TestCase):

    def setUp(self) -> None:
        self.t_path = '/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/pythonProject/test_folder'

        if not os.path.exists(self.t_path):
            os.mkdir(self.t_path)

            t_p1 = 't_ph1.jpg'
            t_p2 = 't_ph2.jpg'
            t_p3 = 't_ph3.jpg'

            d = Downloader()
            d.download_photo(t_p1)
            d.download_photo(t_p2)
            d.download_photo(t_p3)

            t_p1 = DEFAULT_FOLDER + '/' + t_p1
            t_p2 = DEFAULT_FOLDER + '/' + t_p2
            t_p3 = DEFAULT_FOLDER + '/' + t_p3

            m = Mover()
            m.move_file_to(t_p1, self.t_path)
            m.move_file_to(t_p2, self.t_path)
            m.move_file_to(t_p3, self.t_path)

    def test_amount_of_files_in(self):
        a = Archivizer
        self.assertEqual(3, a.amount_of_files_in(self.t_path))

    def test_send_to_archive(self):
        pass

    def test_compressing(self):
        pass
