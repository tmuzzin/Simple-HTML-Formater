
import glob
import sys
from tidylib import tidy_document, tidy_fragment

options={
"indent": "auto",
"indent-spaces": 4,
"markup": True,
"output-xml": False,
"input-xml": False,
"show-warnings": True,
"numeric-entities": True,
"quote-marks": True,
"quote-nbsp": True,
"quote-ampersand": False,
"break-before-br": False,
"uppercase-tags": False,
'uppercase-attributes': False
}
try:
    file_type = sys.argv[1]
except:
	file_type = "html"

for f in glob.glob("*." + file_type):
    with open(f) as htmlFragment:
        htmlFragment, errors = tidy_fragment(htmlFragment.read(),options)
        f = open(f,'w')
        f.write(htmlFragment)
