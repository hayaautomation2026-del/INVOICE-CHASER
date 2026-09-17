import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from core import Passage, answer, retrieve, NOT_FOUND

class FakeModel:
    def __init__(self, result): self.result = result
    def select_evidence(self, question, passages): return self.result

class CoreTests(unittest.TestCase):
    def setUp(self):
        self.docs = [Passage('warranty.pdf', 3, 'The warranty period is 18 months.'),
                     Passage('shipping.pdf', 2, 'Shipping takes seven days.')]
    def test_retrieval_source_and_page(self):
        found = retrieve('warranty period', self.docs)
        self.assertEqual((found[0].source, found[0].page), ('warranty.pdf', 3))
    def test_fabricated_quote_rejected(self):
        result = answer('warranty', self.docs, FakeModel({'evidence':[{'id':0,'quote':'Lifetime warranty'}]}))
        self.assertEqual(result['answer'], NOT_FOUND)
    def test_citation_from_index_not_model(self):
        result = answer('warranty', self.docs, FakeModel({'evidence':[{'id':0,'quote':'18 months'}]}))
        self.assertEqual(result['sources'][0]['page'], 3)
    def test_unknown_returns_no_sources(self):
        result = answer('warranty', self.docs, FakeModel({'evidence':[]}))
        self.assertEqual(result, {'answer':NOT_FOUND,'sources':[]})
    def test_invalid_ids_rejected(self):
        for index in [-1, 99, True, '0']:
            result = answer('warranty', self.docs, FakeModel({'evidence':[{'id':index,'quote':'18 months'}]}))
            self.assertFalse(result['sources'])
    def test_empty_library(self):
        self.assertEqual(answer('anything', [], FakeModel(None))['answer'], NOT_FOUND)

if __name__ == '__main__': unittest.main()
