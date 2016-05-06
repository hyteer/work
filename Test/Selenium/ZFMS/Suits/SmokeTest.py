# encoding: utf-8
import unittest
import xmlrunner
import HTMLTestRunner

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import xmlrunner

from Cases.form import table
from Cases.org import user

userTest = unittest.TestLoader().loadTestsFromTestCase(user.ZfmsOrg)
formTest = unittest.TestLoader().loadTestsFromTestCase(table.ZfmsForm)
smokeTest = unittest.TestSuite([userTest, formTest])
# unittest.TextTestRunner(verbosity=2).run(suite)

xmlrunner.XMLTestRunner(verbosity=2,output='TestReports').run(smokeTest)



'''
outfile = open("C:\ReportZFMS11.html", "w")
runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Test Report',
                description='This demonstrates the report output by Prasanna.Yelsangikar.'
                )

runner.run(smokeTest)
'''

