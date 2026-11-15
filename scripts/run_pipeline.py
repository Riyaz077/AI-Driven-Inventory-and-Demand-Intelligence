import subprocess,sys
subprocess.run([sys.executable,"scripts/prepare_data.py"],check=True)
subprocess.run([sys.executable,"scripts/train_models.py"],check=True)
print("SupplyChainIQ pipeline completed.")
