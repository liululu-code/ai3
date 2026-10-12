
from pathlib import Path
import shutil

root_dir = Path(r'F:\download\人工智能3级\01\人工智能训练师三级操作题答案\人工智能训练师三级操作题答案')
for path in root_dir.iterdir():
    if path.is_dir():
        for child in path.iterdir():
            if child.name.endswith('.docx'):
                shutil.copy(child, root_dir / child.name)
