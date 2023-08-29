import ipdb

from lib.audition import Audition
from lib.role import Role


role1 = Role('Gaston')
role2 = Role('Lefou')
role3 = Role('Lumiere')
role4 = Role('Cogsworth')
aud1 = Audition(role1, 'james', 'new york', '7')
aud2 = Audition(role2, 'bill', '7', '7')
aud3 = Audition(role1, 'pincho', 'philly', '6')
aud4 = Audition(role1, 'horbreath', 'rocktown', '4')
aud5 = Audition(role1, 'connie', 'porchy', '5')


ipdb.set_trace()
