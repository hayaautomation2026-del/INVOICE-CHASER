"""Real local model test; failures and measurements are always saved."""
import json
import os
import platform
import socket
import sys
import tempfile
import time
from pathlib import Path
import psutil
from reportlab.pdfgen import canvas
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from core import LocalModel, answer, extract, NOT_FOUND
root = Path(__file__).resolve().parents[1]
evidence = root / 'evidence'
evidence.mkdir(exist_ok=True)
report = {'platform': platform.platform(), 'cpu_count': os.cpu_count(),
          'gpu_layers': 0, 'embedding': 'local sparse TF-IDF, no learned embedding model',
          'network_test': 'Python socket connect denied; native Windows network monitoring still required',
          'tests': []}
# Guard Python network calls during model loading and operation. Not a native traffic audit.
def denied(*args, **kwargs): raise RuntimeError('Network forbidden during core operation')
socket.socket.connect = denied
socket.create_connection = denied
process = psutil.Process()
try:
    started = time.perf_counter()
    model = LocalModel(root / 'models/model.gguf')
    report['load_seconds'] = time.perf_counter() - started
    report['model_bytes'] = (root / 'models/model.gguf').stat().st_size
    with tempfile.TemporaryDirectory() as directory:
        pdf = Path(directory) / 'policy.pdf'
        c = canvas.Canvas(str(pdf))
        for text in ['The warranty period is 18 months. Warranty covers manufacturing defects.',
                     'Shipping takes seven business days. Express delivery is not offered.',
                     'Returns must be requested within 14 days of delivery.']:
            c.drawString(40, 780, text)
            c.showPage()
        c.save()
        passages = extract(pdf)
        cases = [
            ('supported', 'What is the warranty period?', '18 months', 1),
            ('supported', 'How many business days does shipping take?', 'seven', 2),
            ('supported', 'When must returns be requested?', '14 days', 3),
            ('unsupported', 'Who won the football championship?', None, None),
            ('plausible', 'What is the price of extended warranty?', None, None),
            ('plausible', 'What is the return shipping fee?', None, None),
            ('misleading', 'Why does the warranty last five years?', None, None),
        ]
        for category, question, expected, page in cases:
            start = time.perf_counter()
            cpu_before = process.cpu_times()
            result = answer(question, passages, model)
            elapsed = time.perf_counter() - start
            cpu_after = process.cpu_times()
            passed = (expected in result['answer'].lower() and any(s['page'] == page for s in result['sources'])) if expected else result['answer'] == NOT_FOUND
            if category == 'misleading':
                passed = passed or ('18 months' in result['answer'] and 'five years' not in result['answer'])
            report['tests'].append({'category': category, 'question': question, 'passed': passed,
                'result': result, 'seconds': elapsed, 'rss_bytes': process.memory_info().rss,
                'cpu_seconds': cpu_after.user + cpu_after.system - cpu_before.user - cpu_before.system})
    report['passed'] = all(x['passed'] for x in report['tests'])
except Exception as exc:
    report['error'] = repr(exc)
    report['passed'] = False
finally:
    (evidence / 'feasibility.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report, indent=2))
sys.exit(0 if report['passed'] else 1)
