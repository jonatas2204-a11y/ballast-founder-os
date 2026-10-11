import json, os, subprocess, sys, tempfile, unittest
ROOT=os.path.dirname(os.path.dirname(__file__))
SCRIPT=os.path.join(ROOT,"scripts","credit_partner_score.py")
class T(unittest.TestCase):
 def runx(self,x):
  with tempfile.NamedTemporaryFile("w",suffix=".json",delete=False) as f: json.dump(x,f); p=f.name
  try:return json.loads(subprocess.check_output([sys.executable,SCRIPT,p],text=True))
  finally:os.unlink(p)
 def test_unknown_gate_blocks(self):
  x={"name":"x","scores":{k:10 for k in ["architecture_fit","funding_fit","risk_fit","product_fit","integration_fit","commercial_fit","regulatory_fit","servicing_fit","data_fit","pilot_fit"]},"gates":{"supports_multilayer_distribution":"VERIFIED_PUBLIC","funding_source_confirmed":"UNKNOWN","credit_risk_owner_confirmed":"VERIFIED_PUBLIC","servicing_owner_confirmed":"VERIFIED_PUBLIC","regulatory_roles_confirmed":"VERIFIED_PUBLIC"}}
  self.assertEqual(self.runx(x)["verdict"],"INSUFFICIENT EVIDENCE")
 def test_closed_gates_can_priority(self):
  gates={g:"VERIFIED_PUBLIC" for g in ["supports_multilayer_distribution","funding_source_confirmed","credit_risk_owner_confirmed","servicing_owner_confirmed","regulatory_roles_confirmed"]}
  x={"name":"x","scores":{k:9 for k in ["architecture_fit","funding_fit","risk_fit","product_fit","integration_fit","commercial_fit","regulatory_fit","servicing_fit","data_fit","pilot_fit"]},"gates":gates}
  self.assertEqual(self.runx(x)["verdict"],"PRIORITY PARTNER")
if __name__=="__main__":unittest.main()
