
pre.html: pre.txt
	python rst2s5_pygments.py --theme small-white pre.txt pre.html
	
clean: pre.html
	rm pre.html
