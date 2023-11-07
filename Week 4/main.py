import Framework.Brain as B

B.line()
print(f"\nWelcome to the Pentest Framework")
print(f"\nThis framework has been build to run several scripts with time display, to enable or disable script edit them in the json file!")
print("Only use this script on websites with permission!")
print(f"Feel free to experiment with this script!\n")
B.line()
B.website = input("\nWebsite url: ")
print(f"Scans will start on \" {B.website} \"!")

B.ReadScans()
B.StartScans()