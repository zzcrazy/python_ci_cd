
import unittest
import service
# 编写子类继承unittest.TestCase
class TestSort(unittest.TestCase):

   # 以test开头的函数将会被测试
   def test_sort(self):
        arr = [3, 4, 1, 5, 6]
        a = service.sort(arr)
        # assert 结果跟我们期待的一样
        self.assertEqual(a, [1, 3, 4, 5,6])

if __name__ == '__main__':
    # 如果在Jupyter下，请用如下方式运行单元测试
    # unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    unittest.main()
    
