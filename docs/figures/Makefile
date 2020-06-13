all: arch.png net.png

arch.png: arch.gv
	 dot -T png arch.gv -o arch.png

net.png: net.gv
	 dot -T png net.gv -o net.png

.PHONY: all
