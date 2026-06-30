trial = [1, 2, 3, 4, 5]
paid = [4, 5, 6, 7, 8]

trial_set = set(trial)
paid_set = set(paid)

upgraded = trial_set & paid_set          
leads = trial_set - paid_set            
unique_status = trial_set ^ paid_set    

print("Upgraded (Both):", upgraded)
print("Leads (Trial only):", leads)
print("Unique Status (Not both):", unique_status)