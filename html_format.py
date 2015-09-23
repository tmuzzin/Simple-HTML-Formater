import glob
import lxml.html as lh
from BeautifulSoup import BeautifulSoup as bs
for f in glob.glob("*.html"):
	fread = open(f,'r')
	soup=bs(fread) 
	fread.close()
	prettyHTML=soup.prettify()   #prettify the html
	nf = open(f, 'w')
	nf.write(prettyHTML)
	nf.close()
