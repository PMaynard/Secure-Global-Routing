
all: figures/arch.png figures/net.png report.pdf

figures/arch.png: figures/arch.gv
	 dot -T png figures/arch.gv -o figures/arch.png

figures/net.png: figures/net.gv
	 dot -T png figures/net.gv -o figures/net.png

report.pdf: report.md figures/arch.png figures/net.png
	pandoc  --filter pandoc-citeproc report.md -s -o report.pdf

.PHONY: all
