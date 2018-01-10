## encoding:utf-8--

from datetime import datetime

CAT = u'''
                  ________________________
          ∧ ∧　  /
    〜′‾‾( ﾟДﾟ) < {}
      UU‾‾U U　  \________________________
'''

time = datetime.now().strftime("%I:%M %p")

print CAT.format("The time is: {}".format(time))