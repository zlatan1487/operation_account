from operation.operation.utils import utils


def test_encrypt_card_number_no_alpha():
    assert utils.encrypt_card_number("1234567890123456").strip() == "1234 **** **** 3456"
    assert utils.encrypt_card_number("5678123434567890").strip() == "5678 **** **** 7890"
    assert utils.encrypt_card_number("Счет 46765464282437878125") == "Счет 4676 **** **** **** 8125"
    assert utils.encrypt_card_number("Счет 4676546428243787").strip() == "Счет 4676 **** **** 3787"
    assert utils.encrypt_card_number("VisaClassic 4676546428243787").strip() == "VisaClassic 4676 **** **** 3787"
    assert utils.encrypt_card_number("Maestro 4676546428243787").strip() == "Maestro 4676 **** **** 3787"
    assert utils.encrypt_card_number("").strip() == ""


