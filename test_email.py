import unittest
from email import EmailExtractor

class EmailExtractorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            # email, is_student, is_male, name, surname
            ["norbert.waszkowiak@wat.edu.pl", False, True, "Norbert", "Waszkowiak"],
            ["adrianna.abacka01@student.wat.edu.pl", True, False, "Adrianna", "Abacka"],
            ["wojciech.maziarz@student.wat.edu.pl", True, True, "Wojciech", "Maziarz"],
            ["aleksandra.balcerzak@student.wat.edu.pl", True, False, "Aleksandra", "Balcerzak"],
            ["jerzy.ploch@wat.edu.pl", False, True, "Jerzy", "Ploch"],
            ["joanna.piasecka@wat.edu.pl", False, False, "Joanna", "Piasecka"],
            ["natalia.sobieska@student.wat.edu.pl", True, False, "Natalia", "Sobieska"],
            ["mateusz.florkowski@student.wat.edu.pl", True, True, "Mateusz", "Florkowski"],
            ["adam.patkowski@wat.edu.pl", False, True, "Adam", "Patkowski"],
            ["ewa.lakoma@wat.edu.pl", False, False, "Ewa", "Lakoma"],
            ["jakub.kujawa@student.wat.edu.pl", True, True, "Jakub", "Kujawa"],
            ["marta.markowicz@student.wat.edu.pl", True, False, "Marta", "Markowicz"],
            ["jan.kowalski@student.wat.edu.pl", True, True, "Jan", "Kowalski"],
            ["anna.nowak@student.wat.edu.pl", True, False, "Anna", "Nowak"],
            ["katarzyna.babacka@wat.edu.pl", False, False, "Katarzyna", "Babacka"]]

    def test_is_student(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                is_student = x[1]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(is_student, extractor.is_student())
                
    def test_is_male(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[3]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.get_name())

    def test_get_surname(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                surname = x[4]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(surname, extractor.get_surname())

    def test_get_name(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[3]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.get_name())

if __name__ == '__main__':
    unittest.main()