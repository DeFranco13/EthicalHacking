import Framework.Middleman as Middle
import sys

if len(sys.argv) < 2:
        print("Please give a valid url.")
        sys.exit(1)
Middle.StartProject(sys.argv[1])
