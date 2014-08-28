# IPython log file

range(675226:675321)
range(675226:675321)
arange(675226:675321)
import numpy as np
np.arange(675226:675321)
np.arange(675226,675321)
for x in np.arange(675226,675322:)
for x in np.arange(675226,675322):
    print 'pbs delete_tasks --task-id '+x
    
for x in np.arange(675226,675322):
    print 'pbs delete_tasks --task-id '+str(x)
    
import os
for x in np.arange(675226,675322):
    os.system('pbs delete_tasks --task-id '+str(x))
    
get_ipython().magic(u'logstart')
exit()
