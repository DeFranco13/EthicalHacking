import Framework.Middleman as Middle
import sys
import Scans.Scan4data as Scan

if len(sys.argv) < 2:
        print("Please give a valid url.")
        sys.exit(1)
Middle.StartProject(sys.argv[1])
