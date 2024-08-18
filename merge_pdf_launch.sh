#!/bin/bash
gnome-terminal -- bash -c "
source "$HOME/venvs/pdf_tools/bin/activate"
cd "/home/orlando/MEGA/python_projects/pdf_tools/scripts"
python merge_pdf.py
exec bash"
