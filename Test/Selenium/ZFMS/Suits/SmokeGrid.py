# encoding: utf-8
import sys
import unittest
import xmlrunner
from args import globalArgs
from Cases.org import user_grid
from Cases.form import table_grid

g = globalArgs


#g.setGlb('WINDOWS','chrome')
if len(sys.argv)>1:
    print "The length of argvs: " + str(len(sys.argv))
    br = sys.argv.pop()
    pf = sys.argv.pop()
    g.setGlb(pf, br)
    print "GET GLOB:" + str(g.getGlb())
else:
    g.setGlb('WINDOWS','firefox')

userTest = unittest.TestLoader().loadTestsFromTestCase(user_grid.ZfmsOrg)
tableTest = unittest.TestLoader().loadTestsFromTestCase(table_grid.ZfmsForm)
gridTest = unittest.TestSuite([userTest, tableTest])
xmlrunner.XMLTestRunner(verbosity=2,output='TestReports').run(gridTest)
#unittest.TextTestRunner(verbosity=2).run(userTest)


