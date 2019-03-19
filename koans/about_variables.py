from koans_plugs import *


def test_can_assign_to_variable():
    """
        В переменную можно записывать значения. Например, целые.

        При использовании переменной в выражении, Python подставит значение переменной.
    """
    a = 12

    assert a + 3 == 15


def test_can_assign_different_types():
    """
        В одну переменную можно записывать значения разных типов.

        Используется последнее значение.
    """
    a = 12
    a = 5.5
    a = 'Hello'

    assert a == 'Hello'


def test_variables_names_are_case_sensitive():
    """
        Названия переменных регистрозависимые. "a" и "A" – две разные переменные.

        Несмотря на возможность называть переменные заглавными буквами, в Python
        принято использовать строчные.
    """
    a = 12
    A = 5.5

    assert a == 12
    assert A ==5.5


def test_variables_names_can_have_digits():
    """
        В названиях переменных можно использовать числа.

        Главное правило – название переменной не должно начинаться с числа,
        но может им заканчиваться или иметь число посередине.
    """
    value2var = 22
    assert value2var / 2 == 11.0


def test_variables_names_can_have_underscore():
    """
        В названиях переменных можно использовать подчёркивания.

        Это используется, когда в названии переменной несколько слов и нужно отделить
         одно от другого.
    """
    max_students_mount = 50
    assert max_students_mount / 10 == 5.0
