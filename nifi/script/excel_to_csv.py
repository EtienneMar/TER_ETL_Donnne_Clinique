import sys
import json
import pandas as pd
import io

data = sys.stdin.buffer.read()
df = pd.read_csv(data)
df.to_json(sys.stdout.buffer, orient="records")
