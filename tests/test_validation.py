import pandas as pd
import pytest
from src.data.validation import validate_columns, validate_ranges
def test_pasture_score_range():
    frame=pd.DataFrame({"pasture_id":["A"],"date":["2026-01-01"],"condition_score":[6],"notes":[""]})
    validate_columns(frame,"pasture_conditions")
    with pytest.raises(ValueError): validate_ranges(frame,"pasture_conditions")
def test_missing_column_rejected():
    with pytest.raises(ValueError,match="missing required columns"):
        validate_columns(pd.DataFrame({"well_id":["W1"]}),"groundwater")
