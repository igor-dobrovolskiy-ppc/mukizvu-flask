from os import walk
import re
import ntpath
from typing import Dict, List, Any, Iterator


class LocalAssetsScanner(object):

    @classmethod
    def scan(cls, localRecDirPath: str = '../../../../untitled folder/!Муки 3Vu/') -> Dict[str, List[str]]:
        res: Dict[str, List[str]] = {}
        for (dirpath, dirnames, filenames) in walk(localRecDirPath):
            dirname = ntpath.basename(dirpath)
            assets = filter(lambda e: e.lower().endswith('.flac') or e.lower().endswith('.mp3'), filenames)
            if re.search(r"^\d\d[_\.]\d\d[_\.]\d\d$", dirname) and any(assets):
                # Debug
                print('{dp} ({dbn}) => {dc} dirs, {fc} files'.format(dp=dirpath, dc=len(dirnames),
                                                                     fc=len(filenames), dbn=dirname))
                res[dirpath] = [a for a in assets if isinstance(a, str)]

        return res
