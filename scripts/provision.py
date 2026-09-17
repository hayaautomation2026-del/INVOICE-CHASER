"""Build-time provisioning only. Never called by the shipped application."""
import hashlib
import json
import urllib.request
from pathlib import Path

repo = 'Qwen/Qwen2.5-1.5B-Instruct-GGUF'
filename = 'qwen2.5-1.5b-instruct-q4_k_m.gguf'
root = Path(__file__).resolve().parents[1]
models = root / 'models'
models.mkdir(exist_ok=True)
with urllib.request.urlopen(f'https://huggingface.co/api/models/{repo}?blobs=true', timeout=60) as response:
    metadata = json.load(response)
revision = metadata['sha']
entry = next(x for x in metadata['siblings'] if x['rfilename'] == filename)
expected = entry['lfs']['sha256']
url = f'https://huggingface.co/{repo}/resolve/{revision}/{filename}'
destination = models / 'model.gguf'
if not destination.exists() or hashlib.file_digest(destination.open('rb'), 'sha256').hexdigest() != expected:
    urllib.request.urlretrieve(url, destination)
with destination.open('rb') as file:
    actual = hashlib.file_digest(file, 'sha256').hexdigest()
if actual != expected:
    destination.unlink()
    raise RuntimeError('Model checksum mismatch')
(models / 'manifest.json').write_text(json.dumps({'repository': repo, 'revision': revision,
    'file': filename, 'sha256': actual, 'bytes': destination.stat().st_size,
    'license':'Apache-2.0'}, indent=2), encoding='utf-8')
urllib.request.urlretrieve(f'https://huggingface.co/{repo}/resolve/{revision}/LICENSE', models / 'LICENSE.txt')
print((models / 'manifest.json').read_text())
