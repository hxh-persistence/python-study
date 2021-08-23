#! usr/bin/python
import win32com.client as win32

excel = win32.gencache.EnsureDispatch('Excel.Application')


def test_win32_read():
    wb = excel.Workbooks.Open('D:\\study\\python-study\\test.xlsx')


wb = excel.Workbooks.Add()
