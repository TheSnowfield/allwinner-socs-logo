BUILDDIR	:= build
TOOLDIR		:= tools
SVGGEN		:= allwinnersoclogo.py
SOCS		:= A10 A13 A10s A20 A23 A31 A31s A33 A40i A50 A63 A64 A100 A133 A523 \
			C100 E200 F10 F13 F15 F18 F20 F23 F25 F1C100A F1C100s F1C200s F1C500 F1C500s F1C600 F1C700 F1C800 F1D100 \
			H2+ H3 H8 H80 H133 H5 H6 H64 H313 H616 H618 \
			R6 R7 R8 R11 R16 R40 R58 R311 R328 R18 R329 R818 R128 \
			T2 T3 T7 T8 T133-S3 T33-S4 T133-I T507 T527 \
			V3 V3s V5 V40 V66 V316 V536 V831 V833 \
			B288 B300 MR100 MR133 S3 VR9 MR813 TV303 \
			D1 D1s

.PHONY: all install clean
.DEFAULT_GOAL:= all

clean:
	@echo "Cleaning build directory"
	@set -e; rm -rf $(BUILDDIR) && mkdir $(BUILDDIR)

all: clean
	@for item in $(SOCS); do \
		export svgfile=allwinner-$$(echo $$item | tr '[:upper:]' '[:lower:]').svg; \
		echo "[SVG] Generating '$$svgfile'"; \
		cd $(TOOLDIR) && python $(SVGGEN) "../$(BUILDDIR)/$$svgfile" "$$item"; \
		cd ..; \
	done
	@echo "Done!"

install: all
	@echo "Copying output files"
	@cp -r ./$(BUILDDIR)/* ./svgs/
