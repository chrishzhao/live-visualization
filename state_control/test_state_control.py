import time
from state_control import ChangeYourBrainStateControl

class ecg_fake():

	def __init__(self):
		self.lead_count = 0
		
	def is_lead_on(self):
		self.lead_count += 1
		if self.lead_count > 5:
			print 'lead on'
			return True
		else:
			print 'lead off'
			return False

	def get_hrv(self):
		return 1

ecg = ecg_fake()
sc = ChangeYourBrainStateControl('blah', None, ecg=ecg, vis_period_sec = .25, baseline_sec = 5, condition_sec = 5, baseline_inst_sec = 2, condition_inst_sec = 2)
sc.tag_in()