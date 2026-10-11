import json, os, subprocess, sys, tempfile, unittest
ROOT=os.path.dirname(os.path.dirname(__file__)); SCRIPT=os.path.join(ROOT,"scripts","lead_score.py")
class T(unittest.TestCase):
 def runx(self,x):
  with tempfile.NamedTemporaryFile("w",suffix=".json",delete=False) as f:json.dump(x,f);p=f.name
  try:return json.loads(subprocess.check_output([sys.executable,SCRIPT,p],text=True))
  finally:os.unlink(p)
 def test_high_verified_is_aplus(self):
  x={"company":"x","scores":{"ticket_need":9,"class_ab_fit":9,"scale":8,"decision_access":8,"financing_gap":8,"operational_fit":9},"evidence":{"contact":"VERIFIED_PUBLIC"}}
  self.assertEqual(self.runx(x)["priority"],"A+")
 def test_unknown_contact_not_aplus(self):
  x={"company":"x","scores":{"ticket_need":10,"class_ab_fit":10,"scale":10,"decision_access":10,"financing_gap":10,"operational_fit":10},"evidence":{"contact":"UNKNOWN"}}
  self.assertEqual(self.runx(x)["priority"],"A")
if __name__=="__main__":unittest.main()
