SOURCE=presentation.tex
TARGET=$(patsubst %.tex,%,$(SOURCE))
INCLUDEONLYFRAMES=
WEBWIDTH=267
WEBHEIGHT=200
.PHONY : all clean distclean figures current handout dirs

all: dirs screen 

screen: dirs
	#@perl -pi'.orig' -e 's/,compress,handout\]/,compress]/' $(SOURCE);
	rubber -m xelatex -W all -s --into .mk -I . -I pic -I style $(TARGET)
	@mv .mk/$(TARGET).pdf $(TARGET)_screen.pdf
handout: dirs
	#perl -pi'.orig' -e 's/,compress\]/,compress,handout]/' $(SOURCE);
	rubber -W all -s --into .mk -I . -I pic  -I style --pdf $(TARGET)
	mv .mk/$(TARGET).pdf $(TARGET)_handout.pdf
	#pdfnup --paper a4paper --orient landscape --nup 3x2 --frame true --outfile bla.pdf $(TARGET)_handout.pdf
	#mv bla.pdf $(TARGET)_handout.pdf

web: screen
	acroread -toPostScript -expand -size $(WEBWIDTH)x$(WEBHEIGHT) $(TARGET)_screen.pdf
	#acroread -toPostScript -shrink -landscape -size a4 $(TARGET)_handout.pdf
	ps2pdf14 -dPDFSETTINGS=/screen -dAutoFilterxxxImages=false -dDEVICEWIDTHPOINTS=$(WEBWIDTH) -dDEVICEHEIGHTPOINTS=$(WEBHEIGHT) -dFIXEDMEDIA $(TARGET)_screen.ps $(TARGET)_web.pdf
	#ps2pdf14 -dPDFSETTINGS=/screen $(TARGET)_handout.ps $(TARGET)_handout_web.pdf

impressive: dirs
	#impressive-gettransitions $(TARGET).tex
	#impressive --transition None -I presentation.pdf.info -g 1024x768 -e -d 25m -M -u 10 $(TARGET)_screen.pdf
	impressive --transition None -I presentation.pdf.info -e -d 25m -M -u 10 $(TARGET)_screen.pdf
impressive2: dirs
	impressive --cachefile .kjn/cache -c persistent -e -d 25m -M -u 10 --transition None $(TARGET)_screen.pdf
impressive_prepare: screen
	#impressive-gettransitions $(TARGET).tex
	impressive  --transition None -g 1024x768 -I presentation.pdf.info -d 25m -M -u 10 --cachefile .kjn/cache $(TARGET)_screen.pdf

%.eps : %.fig
	fig2dev -L eps $< $@

dirs:
	@mkdir -p .mk 
	@mkdir -p .kjn
	#@cp pic/* .mk

clean:
	rm -rf .mk
	rm -f presentation.tex.orig
distclean:clean
	rm -f $(TARGET).pdf
	rm -f $(TARGET)_*.pdf
	rm -f $(TARGET)_*.ps
install:
	@echo "Installing fonts...."
	mkdir -p ~/.fonts && cp style/ubo_fonts.zip ~/.fonts && cd ~/.fonts && unzip ubo_fonts.zip
	sudo apt-get install --reinstall ttf-mscorefonts-installer
	@echo "Installing rubber module for xelatex...."
	sudo cp rubber/xelatex.py /usr/share/rubber/rubber/rules/latex
testplain:
	cp style/* .
	pdflatex presentation
	bibtex presentation
	pdflatex presentation
	pdflatex presentation
	cd style ; for f in * ; do rm ../$$f ; done 
	#rubber --clean presentation

