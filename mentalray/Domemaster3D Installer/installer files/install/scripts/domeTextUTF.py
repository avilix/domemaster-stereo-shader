"""
Dome Text UTF Converter V1
by Andrew Hazelden

The DomeTextUTF script converts text into the UTF8 encoding format

Python text encoding notes:
http://docs.python.org/2.5/lib/standard-encodings.html

Version 1
---------------------
Oct 8, 2013
Initial Version

Practical example:
import domeTextUTF
domeTextUTF.convertTextToUTF('C:/dometext.txt', 'C:/dometext_utf8.txt', 'big5')

"""

#Read the current text file and change the encoding
def convertTextToUTF(filename, savename, encoding):
  #filename = "C:/dometext.txt"
  #savename = "C:/dometext_utf8.txt"
  #encoding = 'big5'
  
  #Read the Maya Generated text file
  file = open(filename, "r")
  filedata = file.read()
  file.close()

  #String converted to UTF-8 Format
  u = unicode(filedata, encoding)
  str_utf8 = u.encode("utf-8")
  
  #Save the converted text to a new UTF-8 text file
  file = open(savename, "w")
  file.write(str_utf8)
  file.close()
  
  print('Converting text file: \"' +  filename + '\" from ' + encoding + ' encoding')
  print('Saved as UTF encoded file \"' + savename + '\"')

