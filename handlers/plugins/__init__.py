#hacky way to import all handlers from plugins directory
import os
import glob
__all__ = [ os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+"/commander_*.py")]

#@todo, find a way around it