import os

opt = "project" if input("[1] project\n[2] post\n> ") == "1" else "post"
pname = input(f"{opt} name url: ").replace(" ", "-")
pdate = input(f"{opt} date: [dd-mm-yy] ").replace(" ", "-").split("-")
fname = f"{pdate[2]}-{pdate[1]}-{pdate[0]}-{pname}"
img = True if input("post contains images? [y/n]") in ["y", "Y"] else False
if img:
    if not fname in os.listdir("images"):
        os.mkdir(f"images/{fname}")
    os.system(f"thunar ./images/{fname}")
os.system(f"touch ./_posts/{'projects' if opt == 'project' else 'blog'}/{fname}.md")

