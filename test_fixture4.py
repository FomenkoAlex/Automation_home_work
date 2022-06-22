import pytest


@pytest.fixture(scope="class")
#  эта фикстура выполнится 1 раз для всего наборе тестов, независимо от того сколько ее будут вызывать как параметр
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
#  эта фикстура выполнится только тогда, когда ее вызовут как параметр
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
#  эта фикстура выполниться автоматически для каждого теста отдельно, без вызова
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        pass

    def test_second_smiling_faces(self, prepare_faces):
        pass