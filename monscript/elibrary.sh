mkdir /home/$USER/eLibrary
echo "voici la elibrary de tous mes rtf, doc, pdf, txt, rar, zip dans elibrary"
xterm -l -hold -e "find /home/$USER/eLibrary -name '*.rtf' -o -name '*.doc' -o -name '*.pdf' -o -name '*.txt' -o -name '*.rar' -o -name '*.zip'"
