#! /usr/bin/env python

# Copyright (c) 2013 Mark Travis <mtravis15432+src@gmail.com>
# All rights reserved. No warranty, explicit or implicit, provided.
#
# This file is part of InfiniSQL (tm). It is available either under the
# GNU Affero Public License or under a commercial license. Contact the
# copyright holder for information about a commercial license if terms
# of the GNU Affero Public License do not suit you.
#
# This copy of InfiniSQL is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# InfiniSQL is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with InfiniSQL. It should be in the top level of the source
# directory in a file entitled "COPYING".
# If not, see <http://www.gnu.org/licenses/>.

import sys

cfgdict = {
  'CMDNONE': 0,
  'CMDOK': 1,
  'CMDNOTOK': 2,
  'CMDGET': 3,
  'CMDSET': 4,
  'CMDANONYMOUSPING': 5, 
  'CMDBADLOGINMESSAGES': 6,
  'CMDSTART': 7,
  'CMDSTOP': 8,
  'CMDLISTENER': 9,
  'CMDCONNECTIONHANDLER': 10,
  'CMDUSERSCHEMAMGR': 11,
  'CMDDEADLOCKMGR': 12,
  'CMDTRANSACTIONAGENT': 13,
  'CMDENGINE': 14,
  'CMDOBGATEWAY': 15,
  'CMDIBGATEWAY': 16,
  'CMDGLOBALCONFIG': 17,
  'CMDLOCALCONFIG': 18,
  'CMDGETTOPOLOGYMGRMBOXPTR': 19,
  'CMDOBGATEWAY': 20,
  'CMDPGHANDLER': 21
}

actortypesdict = {
  'ACTOR_NONE': 0,
  'ACTOR_TOPOLOGYMGR': 1,
  'ACTOR_CONNECTIONHANDLER': 2,
  'ACTOR_TRANSACTIONAGENT': 3,
  'ACTOR_ENGINE': 4,
  'ACTOR_USERSCHEMAMGR': 5,
  'ACTOR_DEADLOCKMGR': 6,
  'ACTOR_OBGATEWAY': 7,
  'ACTOR_IBGATEWAY': 8,
  'ACTOR_LISTENER': 9,
  'ACTOR_PGHANDLER': 10
}

firstactorid = 100

cheader = open('infinisql_cfgenum.h', 'w')

cheader.write('#ifndef CFGENUM_H\n\
#define CFGENUM_H\n\
\n\
/* Automatically generated by gencfgenum.py: do not edit by hand */\n\
\n\
enum cfgenum_e\n\
{\n')

l = 0
for k in cfgdict.keys():
  if l:
    cheader.write(',\n')
  else:
    l = 1
  cheader.write('  ' + k + ' = ' + str(cfgdict[k]))

cheader.write ('\n};\n\n')
 
cheader.write('enum actortypes_e\n\
{\n')

l = 0
for k in actortypesdict.keys():
  if l:
    cheader.write(',\n')
  else:
    l = 1
  cheader.write(' ' + k + ' = ' + str(actortypesdict[k]))


cheader.write('\n};\n\n')

cheader.write('#define FIRSTACTORID ' + str(firstactorid + 1))

cheader.write('\n\
\n\
#endif //CFGENUM_H\n')

cheader.close()

pheader = open('../infinisqlmgr/cfgenum.py', 'w')

pheader.write('#! /usr/bin/env python\n\
\n\
# auto-generated, do not edit by hand\n\
\n\
cfgforwarddict = {\n')

l = 0
for k in cfgdict.keys():
  if l:
    pheader.write(',\n')
  else:
    l = 1
  pheader.write('  \'' + k + '\': ' + str(cfgdict[k]))

pheader.write('\n}\n\n')

pheader.write('cfgreversedict = {\n')

l = 0
for k in cfgdict.keys():
  if l:
    pheader.write(',\n')
  else:
    l =1
  pheader.write('  ' + str(cfgdict[k]) + ': \'' + k + '\'')

pheader.write('\n}\n\n')

pheader.write('actortypesforwarddict = {\n')

l = 0
for k in actortypesdict.keys():
  if l:
    pheader.write(',\n')
  else:
    l = 1
  pheader.write('  \'' + k + '\': ' + str(actortypesdict[k]))

pheader.write('\n}\n\n')

pheader.write('actortypesreversedict = {\n')

l = 0
for k in actortypesdict.keys():
  if l:
    pheader.write(',\n')
  else:
    l =1
  pheader.write('  ' + str(actortypesdict[k]) + ': \'' + k + '\'')

pheader.write('\n}\n\n')

pheader.write('firstactorid = ' + str(firstactorid) + '\n\n')

pheader.close()

