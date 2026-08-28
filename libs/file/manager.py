import os

def createpath(path: str) -> bool:
    try:
        os.makedirs(path,exist_ok=True)
        return True
    except Exception as e:
        return False

def copytopath(source_path: str,target_path: str) -> bool:
    with open(source_path,"rb") as src, open(target_path,"wb") as trs:
        try:
            while chunk := src.read(60000):
                trs.write(chunk)
            return True
        except Exception as e:
            return False
