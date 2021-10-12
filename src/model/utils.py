import unittest

def is_none_value_included(dict_obj):
    if 'None' in dict_obj.values():
        return True
    
    return False


class UtilsTest(unittest.TestCase):
    # FalseのときにFalseを返しているかを確認したい
    def test_is_none_value_included_false(self):
        dict_obj = {'key':'value', 'key2':'value2'}
        expect = False 
        actual = is_none_value_included(dict_obj)
        self.assertEqual(expect, actual)

    # TrueのときにTrueを返しているかを確認したい
    def test_is_none_value_included_true(self):
        dict_obj = {'key':'value', 'key2':'None'}
        expect = True
        actual = is_none_value_included(dict_obj)
        self.assertEqual(expect, actual)


if __name__ == "__main__":
    unittest.main()