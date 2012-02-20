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
  cmd = None
  
  if os.environ.has_key('VIRTUAL_ENV'):
    env_path = os.environ['VIRTUAL_ENV']
    for key, env in config.items():
      if env['env'] == env_path:
        if env.has_key('cd') and env['cd']:
          cmd = 'cd ' + env['cd']
          
    if not cmd:
      cmd = "echo Your in a virtual env, but there is no directory to change to."
      
  if not cmd and len(sys.argv) == 2:
    if sys.argv[1] in config.keys():
      env = config[sys.argv[1]]
      venv = os.path.join(env['env'], 'bin', 'activate')
      cmd = "source  %s" % venv
      if env.has_key('cd') and env['cd']:
        cmd += '; cd ' + env['cd']
        
  if cmd:
    print cmd
    