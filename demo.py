"""
demo.py
created by : longyucheng
2019/5/25
"""

from Cell1D import *

rule = 26           # 0~255
n = 320            # 图片行数

def CellularAutomaton(rule, n):
    cell = Cell1D(rule, n)
    cell.start_single()
    #cell.start_random()
    cell.loop(n-1)
    
    # save img
    viewer = Cell1DViewer(cell)
    viewer.draw()
    plt.savefig('SaveImg/'+str(rule)+'.jpg')
    
    # save eps
    eps = EPSDrawer()
    eps.draw(cell)
    eps.save(filename='EPS/'+str(rule)+'.eps')
    
def CellularAutomatonWrap(rule, n):
    cellWrap = Wrap1D(rule, n)
    #cellWrap.start_single()
    cellWrap.start_random()
    cellWrap.loop(n-1)
    
    # save img
    viewer = Cell1DViewer(cellWrap)
    viewer.draw()
    plt.savefig('SaveWrapImg/'+str(rule)+'.jpg')
    
    # save eps
    eps = EPSDrawer()
    eps.draw(cellWrap)
    eps.save(filename='EPSWrap/'+str(rule)+'.eps')

for each in range(256):
    print('dealing: ', end='')
    print(each)
    
    CellularAutomaton(each, n)
    CellularAutomatonWrap(each, n)

#CellularAutomaton(255, n)
#CellularAutomatonWrap(255, n)



