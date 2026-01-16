try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    from importlib_metadata import version, PackageNotFoundError  # For Python <3.8

try:
    __version__ = version("chatterbox-tts")
except PackageNotFoundError:
    __version__ = "0.0.0-dev"


from .tts import ChatterboxTTS
from .vc import ChatterboxVC
from .mtl_tts import ChatterboxMultilingualTTS, SUPPORTED_LANGUAGES
