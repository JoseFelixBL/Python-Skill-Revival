"""
CLI Tool with `argparse`
    Create a command-line tool that takes a word and a URL.
    The tool should fetch the web page and count how many times the word 
    appears on it.
    Use the `argparse` module to handle command-line arguments cleanly.
"""
import argparse
import requests
from bs4 import BeautifulSoup
import re

def create_parser():
    """
    Set the parser so it can read:
        - word  The word to search in the string parts of the web tags
        - link  The web page address to search
    """
    p = argparse.ArgumentParser()
    p.add_argument('word')
    p.add_argument('link')
    return p

def do_parse(p):
    """
    Parse the input, if successful, return a tup(le) with the actual word and link
    """
    try:
        tup = p.parse_args()
    except argparse.ArgumentError as ex:
        print(ex)
    else:
        return tup

def buscar_palabra_en_enlace(palabra, enlace):
    """
    Do the actual search in the web
    """
    # Start BeautifulSoup
    response = requests.get(enlace)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # No tagname and tag-attributes, search in all tags, i.e.:
    # headers_2 = soup.find_all('h2', class_='tagname-titulo', 
    #                           string=re.compile(palabra, re.IGNORECASE))
    tagnames = soup.find_all(string=re.compile(palabra, re.IGNORECASE))
    for tagname in tagnames:
        texto = tagname.get_text()
        print(texto)

parser = create_parser()
argumento = do_parse(parser)
buscar_palabra_en_enlace(argumento.word, argumento.link)
