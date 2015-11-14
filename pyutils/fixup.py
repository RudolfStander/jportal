import sys, glob, os

copyright = '''\
/// ------------------------------------------------------------------
/// Copyright (c) from 1996 Vincent Risi 
///                           
/// All rights reserved. 
/// This program and the accompanying materials are made available 
/// under the terms of the Common Public License v1.0 
/// which accompanies this distribution and is available at 
/// http://www.eclipse.org/legal/cpl-v10.html 
/// Contributors:
///    Vincent Risi
/// ------------------------------------------------------------------
'''.splitlines()

for file_name in glob.glob('/main/jportal/generators/vlab/crackle/*.java'):
    in_file = open(file_name, 'rt')
    lines = in_file.readlines()
    in_file.close()
    next = False
    for i, line in enumerate(lines):
        n = line.find('/// Copyright (c) from 1996 Vincent Risi')
        if n >= 0:
            next = True
            break
        n = line.find('package')
        if n >= 0:
            j = 0
            for j, line in enumerate(copyright):
                lines.insert(j, '%s\n' % line)
            break
    if next == True:
        continue
    print file_name
    out_file = open(file_name, 'w')
    out_file.writelines(lines)
    break