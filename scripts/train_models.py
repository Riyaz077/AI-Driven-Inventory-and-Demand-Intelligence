import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.supplychainiq.forecasting import train_and_evaluate
print(train_and_evaluate())
