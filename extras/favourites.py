import xbmc
from xbmcgui import Window
from xml.dom.minidom import parseString
import os

class Main:
   # grab the home window
   WINDOW = Window ( 10004 )

   def __init__( self ):
      self._clear_properties()
      self._read_file()
      self._parse_String()
      self._fetch_favourites()
      self.doc.unlink()

   def _clear_properties( self ):
      for count in range( 20 ):
         # clear Property
         self.WINDOW.clearProperty( "favourite.%d.path" % ( count + 1, ) )
         self.WINDOW.clearProperty( "favourite.%d.name" % ( count + 1, ) )

   def _read_file( self ):
      # Set path
      self.fav_dir = 'special://masterprofile//favourites.xml'
      # Check to see if file exists
      if (os.path.isfile( self.fav_dir ) == False):
         self.favourites_xml = '<favourites><favourite name="Can Not Find favourites.xml">-</favourite></favourites>'
      else:
         # read file
         self.fav = open( self.fav_dir , 'r')
         self.favourites_xml = self.fav.read()
         self.fav.close()

   def _parse_String( self ):
      self.doc = parseString( self.favourites_xml )
      self.favourites = self.doc.documentElement.getElementsByTagName ( 'favourite' )

   def _fetch_favourites( self ):
      # Go through each favourites
      self.count = 0
      for self.doc in self.favourites:
         self.fav_path = self.doc.childNodes [ 0 ].nodeValue
         # add return to path if it's not a file path
         if "10024" not in self.fav_path: self.fav_path = self.fav_path.replace( ')', ',return)' )
         # set properties
         self.WINDOW.setProperty( "favourite.%d.path" % ( self.count + 1, ) , self.fav_path )
         self.WINDOW.setProperty( "favourite.%d.name" % ( self.count + 1, ) , self.doc.attributes [ 'name' ].nodeValue )
         self.count = self.count+1

if ( __name__ == "__main__" ):
    Main()
