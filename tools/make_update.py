# 새 버전 배포: python3 tools/make_update.py 2.4.2 path/to/YunaAutoSave.exe "바뀐 점1" "바뀐 점2" ...
# → files/<버전>/YunaAutoSave.exe 복사 + update.json 갱신. 그다음 git add/commit/push 하면
#   설치된 앱들이 12시간 안에(또는 켤 때) 알아서 받아서 쉬는 틈에 바꿔요.
import sys, json, hashlib, shutil, os
ver, exe, notes = sys.argv[1], sys.argv[2], sys.argv[3:]
R = 'jya9696-wq/yuna-autosave'
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(f'{root}/files/{ver}', exist_ok=True)
shutil.copy(exe, f'{root}/files/{ver}/YunaAutoSave.exe')
b = open(exe, 'rb').read()
assert f"APP_VERSION := '{ver}'".encode() in b, 'exe 안의 버전이 다르다'
m = {'version': ver, 'title': '새 버전으로 업데이트됐어요', 'notes': notes,
     'exe': f'https://raw.githubusercontent.com/{R}/main/files/{ver}/YunaAutoSave.exe',
     'sha256': hashlib.sha256(b).hexdigest(), 'size': len(b)}
json.dump(m, open(f'{root}/update.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(m, ensure_ascii=False, indent=1))
