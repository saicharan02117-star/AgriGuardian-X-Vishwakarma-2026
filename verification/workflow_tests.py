"""Synthetic workflow unit tests. NOT a disease-model accuracy evaluation."""
import unittest
def image_gate(w,h,sharpness): return w>=320 and h>=240 and sharpness>=30
def advisory_flow(quality,diagnosis,approval):
    if not quality: return "RECAPTURE"
    if diagnosis is None: return "REVIEW_REQUIRED"
    if not approval: return "AWAIT_APPROVAL"
    return "APPROVED_FOR_MANUAL_ACTION"
class WorkflowTests(unittest.TestCase):
    def test_low_resolution(self): self.assertFalse(image_gate(200,150,80))
    def test_blurry(self): self.assertFalse(image_gate(640,480,10))
    def test_good_quality(self): self.assertTrue(image_gate(640,480,40))
    def test_recapture(self): self.assertEqual(advisory_flow(False,"suspected",False),"RECAPTURE")
    def test_review(self): self.assertEqual(advisory_flow(True,None,False),"REVIEW_REQUIRED")
    def test_approval_gate(self): self.assertEqual(advisory_flow(True,"suspected",False),"AWAIT_APPROVAL")
    def test_approved(self): self.assertEqual(advisory_flow(True,"suspected",True),"APPROVED_FOR_MANUAL_ACTION")
if __name__=="__main__": unittest.main(verbosity=2)
