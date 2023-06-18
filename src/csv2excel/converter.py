import os
from typing import Optional
import pandas as pd


def convert(input_file: str, output_file: Optional[str]) -> None:
    if output_file is None:
        if os.path.splitext(input_file) == 1:
            output_file = input_file + ".xlsx"
        else:
            output_file = os.path.splitext(input_file)[0] + ".xlsx"
    df = pd.read_csv(input_file)
    df.to_excel(output_file, index=False)

    return
