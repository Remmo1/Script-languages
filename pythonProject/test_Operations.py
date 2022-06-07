from unittest import TestCase
import os
from Downlader import download_photo
from Operations import move_file_to, amount_of_files_in
from constst import DEFAULT_FOLDER


class Test(TestCase):

    def setUp(self) -> None:
        self.t_path = '/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/pythonProject/test_folder'

        if not os.path.exists(self.t_path):
            os.mkdir(self.t_path)

            t_p1 = 't_ph1.jpg'
            t_p2 = 't_ph2.jpg'
            t_p3 = 't_ph3.jpg'

            download_photo(t_p1)
            download_photo(t_p2)
            download_photo(t_p3)

            t_p1 = DEFAULT_FOLDER + '/' + t_p1
            t_p2 = DEFAULT_FOLDER + '/' + t_p2
            t_p3 = DEFAULT_FOLDER + '/' + t_p3

            move_file_to(t_p1, self.t_path)
            move_file_to(t_p2, self.t_path)
            move_file_to(t_p3, self.t_path)

    def test_amount_of_files_in(self):
        self.assertEqual(3, amount_of_files_in(self.t_path))
