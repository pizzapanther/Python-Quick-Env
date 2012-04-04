#!/usr/bin/env python

import os
import sys
import json

def get_config ():
  jpath = os.path.join(os.environ['HOME'], '.pyenv.json')
  if not os.path.exists(jpath):
    return {}
    
  fh = open(jpath, 'r')
  j = fh.read()
  fh.close()
  config = json.loads(j)
  
  return config
  
def save_config (config):
  jpath = os.path.join(os.environ['HOME'], '.pyenv.json')
  fh = open(jpath, 'w')
  j = fh.write(json.dumps(config, indent=2))
  fh.close()
  
def main ():
  config = get_config()
  cmd = None
  
  if len(sys.argv) == 1 and os.environ.has_key('VIRTUAL_ENV'):
    env_path = os.environ['VIRTUAL_ENV']
    for key, env in config.items():
      if env['env'] == env_path:
        if env.has_key('cd') and env['cd']:
          cmd = 'cd ' + env['cd']
          
    if not cmd:
      cmd = "echo Your in a virtual env, but there is no directory to change to."
      
  if not cmd:
    if len(sys.argv) > 1:
      if sys.argv[1] == 'add' and len(sys.argv) > 2:
        envdir = os.path.join(os.environ['HOME'], 'pyenv')
        if not os.path.exists(envdir):
          os.mkdir(envdir)
          
        venvdir = os.path.join(envdir, sys.argv[2])
        cmd = 'virtualenv "%s"' % venvdir
        
        config[sys.argv[2]] = {'env': venvdir}
        if len(sys.argv) > 3:
          config[sys.argv[2]]['cd'] = sys.argv[3]
          
        save_config(config)
        
      if sys.argv[1] in config.keys():
        env = config[sys.argv[1]]
        venv = os.path.join(env['env'], 'bin', 'activate')
        cmd = "source  %s" % venv
        if env.has_key('cd') and env['cd']:
          cmd += '; cd ' + env['cd']
          
  if cmd:
    print cmd
    
  else:
    print "echo Invalid environment or command."
    