"""Minimal Stage 1 Windows desktop proof. No customer configuration."""
import json
import queue
import sys
import threading
from pathlib import Path
from core import LocalModel, answer, extract


def resources():
    return Path(getattr(sys, '_MEIPASS', Path(__file__).resolve().parents[1]))


def self_test(destination):
    from core import Passage
    import time
    start = time.perf_counter()
    model = LocalModel(resources() / 'models/model.gguf')
    result = answer('What is the warranty period?',
                    [Passage('fixture.pdf', 1, 'The warranty period is 18 months.')], model)
    result['elapsed_seconds'] = time.perf_counter() - start
    Path(destination).write_text(json.dumps(result, indent=2), encoding='utf-8')
    return 0 if '18 months' in result['answer'] else 1


def main():
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk
    root = tk.Tk()
    root.title('PrivateDocs AI — feasibility prototype')
    root.geometry('780x560')
    root.minsize(600, 400)
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill='both', expand=True)
    ttk.Label(frame, text='PrivateDocs AI', font=('Segoe UI', 22, 'bold')).pack(anchor='w')
    ttk.Label(frame, text='Your PDFs stay on this computer. Stage 1 prototype.').pack(anchor='w', pady=8)
    output = tk.Text(frame, wrap='word', height=16, state='disabled')
    question = ttk.Entry(frame)
    events = queue.Queue()
    state = {'passages': [], 'model': None, 'busy': False}
    def show(text):
        output.configure(state='normal')
        output.delete('1.0', 'end')
        output.insert('end', text)
        output.configure(state='disabled')
    def task(fn):
        if state['busy']:
            return
        state['busy'] = True
        add.configure(state='disabled')
        ask.configure(state='disabled')
        show('Working locally…')
        def run():
            try:
                events.put((True, fn()))
            except Exception as exc:
                events.put((False, str(exc)))
        threading.Thread(target=run, daemon=True).start()
    def import_pdf():
        path = filedialog.askopenfilename(filetypes=[('PDF documents', '*.pdf')])
        if path:
            def work():
                state['passages'].extend(extract(path))
                return 'Added ' + Path(path).name + '. Ask a question below.'
            task(work)
    def ask_question():
        q = question.get().strip()
        if not q or not state['passages']:
            messagebox.showinfo('Add a PDF', 'Add a PDF and enter a question first.')
            return
        def work():
            if state['model'] is None:
                state['model'] = LocalModel(resources() / 'models/model.gguf')
            result = answer(q, state['passages'], state['model'])
            return result['answer'] + '\n\n' + '\n'.join(
                f"Source: {s['document']} — PDF page {s['page']}" for s in result['sources'])
        task(work)
    add = ttk.Button(frame, text='Add PDF', command=import_pdf)
    add.pack(anchor='w', pady=8)
    output.pack(fill='both', expand=True, pady=8)
    question.pack(fill='x', pady=8)
    ask = ttk.Button(frame, text='Ask', command=ask_question)
    ask.pack(anchor='e')
    def poll():
        try:
            ok, result = events.get_nowait()
            show(result if ok else 'Unable to complete this operation: ' + result)
            state['busy'] = False
            add.configure(state='normal')
            ask.configure(state='normal')
        except queue.Empty:
            pass
        root.after(100, poll)
    poll()
    root.mainloop()

if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == '--self-test':
        raise SystemExit(self_test(sys.argv[2]))
    main()
