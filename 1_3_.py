input_file  = "1_/1_2_.txt"
output_file = "1_/1_3_.txt"

with open(input_file, "rb") as f:
    data = f.read()

# remove any trailing newline / \n:: completely
data = data.rstrip(b"\n")

# literal replacements only
data = data.replace(b"\t", b"::")
data = data.replace(b"\n", b"\n::")

# remove leading empty line if it exists (i.e. file starts with \n)
if data.startswith(b"\n::"):
    data = data[3:]           # cut the first \n::

with open(output_file, "wb") as f:
    f.write(data)