import os, unittest, sys
sys.path.insert(0,os.path.join(os.path.dirname(os.path.dirname(__file__)),"scripts"))
from unit_economics import model
class T(unittest.TestCase):
 def test_funnel(self):
  x={"active_merchants":10,"eligible_quotes_per_merchant_month":10,"application_rate":.5,"approval_rate":.5,"funding_rate":.8,"average_financed_ticket":10000,"ballast_take_rate":.02,"fixed_monthly_cost":1000}
  r=model(x); self.assertEqual(r["applications"],50); self.assertEqual(r["funded_transactions"],20); self.assertEqual(r["financed_volume"],200000)
 def test_break_even_exists(self):
  x={"active_merchants":10,"eligible_quotes_per_merchant_month":10,"application_rate":.5,"approval_rate":.5,"funding_rate":1,"average_financed_ticket":10000,"ballast_take_rate":.02,"fixed_monthly_cost":1000}
  self.assertIsNotNone(model(x)["approx_break_even_active_merchants"])
if __name__=="__main__":unittest.main()
