#!/usr/bin/env python

import os
import sys
import json

def main ():
  jpath = os.path.join(os.environ['HOME'], '.pyenv.json')
  fh = open(jpath, 'r')
  j = fh.read()
  fh.close()
  config = json.loads(j)
  
  if sys.argv[1] in config.keys():
    env = config[sys.argv[1]]
    venv = os.path.join(env['env'], 'bin', 'activate')
    cmd = "source  %s" % venv
    if env.has_key('cd') and env['cd']:
      cmd += '; cd ' + env['cd']
      
    print cmd
    