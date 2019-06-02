import sys
import json

f = open(sys.argv[1])
program = json.loads(f.read())

exec("import " + program["imports"] + "\n" + "g =" + program["main"] + "\ng(" + (sys.argv[2]) + ")")
